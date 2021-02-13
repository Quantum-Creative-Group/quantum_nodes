import numpy as np
from numpy import pi
import scipy.linalg
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg
import sys

class SimulationCache:
    """This class is used to store all the computed frames
    and to determine the ones that need to be computed
    when the user is asking the data for a specific frame.
    """
    def __init__(self, max_frame):
        """        
        :param max_frame: the length of the simulation, in frames
        :type max_frame: int
        """
        self.data = np.empty((max_frame), np.ndarray)
        self.last_computed_frame = None

    def processFrame(self, d, inp):
        """Compute the next frame.
        This method is only an implementation of the plot_animation() function taken from the source code.

        :param d: Simulation data manager
        :type d: SimulationDataManager
        :param inp: Simulation inputs manager
        :type inp: SimulationInputsManager
        """
        vector_selon_x = d.xConcatenate(d.wave_function, inp.dimension)
        vector_derive_y_selon_x = d.xConcatenate(d.dySquare(d.wave_function, inp.dimension, inp.step), inp.dimension)
        U_selon_x = vector_selon_x + (1j*inp.delta_t/2)*(vector_derive_y_selon_x - d.v_x*vector_selon_x)
        U_selon_x_plus = scipy.sparse.linalg.spsolve(d.hx, U_selon_x)

        d.wave_function = d.xDeconcatenate(U_selon_x_plus, inp.dimension)

        vector_selon_y = d.yConcatenate(d.wave_function, inp.dimension)
        vector_derive_x_selon_y = d.yConcatenate(d.dxSquare(d.wave_function, inp.dimension, inp.step), inp.dimension)
        U_selon_y = vector_selon_y  + (1j*inp.delta_t/2)*(vector_derive_x_selon_y - d.v_y*vector_selon_y)
        U_selon_y_plus = scipy.sparse.linalg.spsolve(d.hy, U_selon_y)

        d.wave_function = d.yDeconcatenate(U_selon_y_plus, inp.dimension)
    
    def getFrame(self, frame, d, inp):
        """Return the requested data at the given frame.
        Manages the situations where several frames need to be
        calculated in order to return the requested data.

        :param frame: index of the frame
        :type frame: int
        :param d: Simulation data manager
        :type d: SimulationDataManager
        :param inp: Simulation inputs manager
        :type inp: SimulationInputsManager
        :raises e: whenever something wrong happends during the frame computation
        :raises IndexError: frame index out of range
        :return: requested data at the given frame
        :rtype: 2d numpy array of numpy.complex128
        """
        if (frame >= 0):
            if (frame <= self.last_computed_frame):
                # the frame has already been computed
                return self.data[frame]
            elif (frame <= inp.frame_rate * inp.duration):
                # the frame is in the scope of the simulation
                # but has not been computed yet
                frames_to_compute = frame - self.last_computed_frame
                try:
                    for frame in range(frames_to_compute):
                        self.processFrame(d, inp)
                        self.last_computed_frame += 1
                        self.data[self.last_computed_frame] = d.wave_function
                except Exception as e:
                    print(sys.exc_info())
                    raise e from e
                return self.data[frame]
            else:
                # the requested frame is not in the scope of the simulation
                # return the last computed frame by default
                return self.data[self.last_computed_frame]
        else:
            # the requested frame is negative
            raise IndexError("ERROR::SimulationCache::getFrame() frame index out of range\nData for frame n°" + str(frame) + " unavailable")