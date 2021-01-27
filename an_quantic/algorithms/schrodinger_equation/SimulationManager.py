import numpy as np
from numpy import pi
import scipy.linalg
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg
import sys

from . SimulationDataManager import SimulationDataManager
from . SimulationInputsManager import SimulationInputsManager
from . SimulationCache import SimulationCache

# This is an implementation of the 2D simulation of Schrödinger equation
# This code is just a new architecture to meet our needs (adapted for blender animation nodes)
# All the simulation computation is from Azercoco
# You can find his code here : https://github.com/Azercoco/Python-2D-Simulation-of-Schrodinger-Equation

class SimulationManager:
    def __init__(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
        """
        @parameters : see full details in the corresponding classes.
        --> SimulationInputsManager
        --> SimulationDataManager
        --> SimulationCache
        """
        self.inputs = SimulationInputsManager(dim, size, center, n_o_w, spr, pot, obs, fr, d, dt)
        self.data = SimulationDataManager()
        self.cache = SimulationCache(int(self.inputs.duration * self.inputs.frame_rate) + 1)
        self.__initialize()
        
    def __initialize(self):
        """ 
        Initializes the data needed for the simulation.
        This method is only an implementation of the init() function taken from the source code.
        """
        d = self.data      # data container
        inp = self.inputs  # user inputs container
        d.x_axis = np.linspace(-inp.size/2, inp.size/2, inp.dimension)
        d.y_axis = np.linspace(-inp.size/2, inp.size/2, inp.dimension)
        d.x, d.y = np.meshgrid(d.x_axis, d.y_axis)
        phase = np.exp( 1j*(d.x*inp.number_of_waves[0] + d.y*inp.number_of_waves[1]))
        px = np.exp( - ((inp.center[0] - d.x)**2)/(4*inp.spreading[0]**2))
        py = np.exp( - ((inp.center[1] - d.y)**2)/(4*inp.spreading[1]**2))
        d.wave_function = phase*px*py
        norm = np.sqrt(d.integrate(np.abs(d.wave_function)**2, inp.dimension, inp.step))
        d.wave_function = d.wave_function/norm

        d.laplace_matrix = sp.sparse.lil_matrix(-2*sp.sparse.identity(inp.dimension**2))
        for i in range(inp.dimension):
            for j in range(inp.dimension-1):
                k = i*inp.dimension + j
                d.laplace_matrix[k,k+1] = 1
                d.laplace_matrix[k+1,k] = 1

        d.v_x = np.zeros(inp.dimension**2, dtype='c16')
        for j in range(inp.dimension):
            for i in range(inp.dimension):
                xx, yy = i, inp.dimension*j
                if inp.isObstacle(d.x_axis[j], d.y_axis[i]):
                    d.v_x[xx+yy] = d.potential_wall
                else:
                    d.v_x[xx+yy] = inp.getPotential(d.x_axis[j], d.y_axis[i])

        d.v_y = np.zeros(inp.dimension**2, dtype='c16')
        for j in range(inp.dimension):
            for i in range(inp.dimension):
                xx, yy = j*inp.dimension, i
                if inp.isObstacle(d.x_axis[i], d.y_axis[j]):
                    d.v_y[xx+yy] = d.potential_wall
                else:
                    d.v_y[xx+yy] = inp.getPotential(d.x_axis[i], d.y_axis[j])

        V_x_matrix = sp.sparse.diags([d.v_x], [0])
        V_y_matrix = sp.sparse.diags([d.v_y], [0])
        d.laplace_matrix = d.laplace_matrix/(inp.step**2)

        d.h1 = (1*sp.sparse.identity(inp.dimension**2) - 1j*(inp.delta_t/2)*(d.laplace_matrix))
        d.h1 = sp.sparse.dia_matrix(d.h1)

        d.hx = (1*sp.sparse.identity(inp.dimension**2) - 1j*(inp.delta_t/2)*(d.laplace_matrix - V_x_matrix))
        d.hx = sp.sparse.dia_matrix(d.hx)

        d.hy = (1*sp.sparse.identity(inp.dimension**2) - 1j*(inp.delta_t/2)*(d.laplace_matrix - V_y_matrix))
        d.hy = sp.sparse.dia_matrix(d.hy)

        d.potential_boundary = []
        for i in range(0, inp.dimension):
            for j in range(0, inp.dimension):
                if inp.isObstacle(d.x_axis[j], d.y_axis[i]):
                    adj = d.getAdjPos(i, j, inp.dimension)
                    for xx, yy in adj:
                        if (xx >= 0) and (yy >= 0) and (xx < inp.dimension) and (yy < inp.dimension) and (not inp.isObstacle(d.x_axis[yy], d.y_axis[xx])):
                            d.potential_boundary.append((i, j))
                            
        self.cache.data[0] = d.wave_function     # stores the first frame in the cache
        self.cache._last_computed_frame = 0

    
    def getFrameData(self, frame):
        """
        Returns the data from the requested frame.

        @parameter :
        frame - integer - the requested frame
        """
        try:
            # returns a list of complex numbers rather than
            # a matrix of complex numbers (list of list)
            # the shape of the output is :
            # not formatted : wave_function[i] = [z_i1, z_i2, ... z_in] (shape n * n)
            # formated_output = [z_11, ..., z_1n, z_21, ..., z_2n, ..., z_n1, ..., z_nn] (shape 1 * n)
            frame = self.cache.getFrame(frame, self.data, self.inputs)
            formated_output = frame[0]
            for i in range(1, self.inputs.dimension):
                formated_output = np.concatenate((formated_output, frame[i]))
            return formated_output
        except Exception as e:
            raise e from e
    
    def updateSimulation(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
        """
        Checks if any of the user inputs have changed in order to
        update the parameters of the simulation.
        
        @parameters :
        same as the __init__ method
        """
        if self.inputs.hasChanged(dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
            self.__init__(dim, size, center, n_o_w, spr, pot, obs, fr, d, dt)