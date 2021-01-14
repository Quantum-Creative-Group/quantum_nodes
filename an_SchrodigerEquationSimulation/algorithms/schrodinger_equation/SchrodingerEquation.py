import numpy as np
from numpy import pi
import scipy.linalg
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg

from . SimulationDataManager import SimulationDataManager
from . SimulationInputsManager import SimulationInputsManager
from . SchrodingerSimulationCache import SchrodingerSimulationCache

class SchrodingerEquation:
    def __init__(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
        self._inputs = SimulationInputsManager(dim, size, center, n_o_w, spr, pot, obs, fr, d, dt)
        self._data = SimulationDataManager()
        self._cache = SchrodingerSimulationCache()
        self.initialize()
        
    def initialize(self):
        d = self._data
        inp = self._inputs
        d._x_axis = np.linspace(-inp._size/2, inp._size/2, inp._dimension)
        d._y_axis = np.linspace(-inp._size/2, inp._size/2, inp._dimension)
        d._x, d._y = np.meshgrid(d._x_axis, d._y_axis)
        phase = np.exp( 1j*(d._x*inp._number_of_waves[0] + d._y*inp._number_of_waves[1]))
        px = np.exp( - ((inp._center[0] - d._x)**2)/(4*inp._sprawl[0]**2))
        py = np.exp( - ((inp._center[1] - d._y)**2)/(4*inp._sprawl[1]**2))
        d._wave_function = phase*px*py
        norm = np.sqrt(d.integrate(np.abs(d._wave_function)**2, inp._dimension, inp._step))
        d._wave_function = d._wave_function/norm

        d._laplace_matrix = sp.sparse.lil_matrix(-2*sp.sparse.identity(inp._dimension**2))
        for i in range(inp._dimension):
            for j in range(inp._dimension-1):
                k = i*inp._dimension + j
                d._laplace_matrix[k,k+1] = 1
                d._laplace_matrix[k+1,k] = 1

        d._v_x = np.zeros(inp._dimension**2, dtype='c16')

        for j in range(inp._dimension):
            for i in range(inp._dimension):
                xx, yy = i, inp._dimension*j
                if inp.isObstacle(d._x_axis[j], d._y_axis[i]):
                    d._v_x[xx+yy] = d._potential_wall
                else:
                    d._v_x[xx+yy] = inp.getPotential(d._x_axis[j], d._y_axis[i])

        d._v_y = np.zeros(inp._dimension**2, dtype='c16')

        for j in range(inp._dimension):
            for i in range(inp._dimension):
                xx, yy = j*inp._dimension, i
                if inp.isObstacle(d._x_axis[i], d._y_axis[j]):
                    d._v_y[xx+yy] = d._potential_wall
                else:
                    d._v_y[xx+yy] = inp.getPotential(d._x_axis[i], d._y_axis[j])

        V_x_matrix = sp.sparse.diags([d._v_x], [0])
        V_y_matrix = sp.sparse.diags([d._v_y], [0])
        d._laplace_matrix = d._laplace_matrix/(inp._step**2)

        d._h1 = (1*sp.sparse.identity(inp._dimension**2) - 1j*(inp._delta_t/2)*(d._laplace_matrix))
        d._h1 = sp.sparse.dia_matrix(d._h1)

        d._hx = (1*sp.sparse.identity(inp._dimension**2) - 1j*(inp._delta_t/2)*(d._laplace_matrix - V_x_matrix))
        d._hx = sp.sparse.dia_matrix(d._hx)

        d._hy = (1*sp.sparse.identity(inp._dimension**2) - 1j*(inp._delta_t/2)*(d._laplace_matrix - V_y_matrix))
        d._hy = sp.sparse.dia_matrix(d._hy)

        for i in range(0, inp._dimension):
            for j in range(0, inp._dimension):
                if inp.isObstacle(d._x_axis[j], d._y_axis[i]):
                    adj = d.getAdjPos(i, j, inp._dimension)
                    for xx, yy in adj:
                        if xx >= 0 and yy >= 0 and xx < inp._dimension and yy < inp._dimension and not inp.isObstacle(d._x_axis[yy], d._y_axis[xx]):
                            d._potential_boundary.append((i, j))
                            
        self._cache._data.append(d._wave_function)
        self._cache._last_computed_frame = 0

    
    def getFrameData(self, frame):
        try:
            return self._cache.getFrame(frame, self._data, self._inputs)
        except:
            print("ERROR::SchrodingerEquation : impossible the get the requested data at frame : " + str(frame))