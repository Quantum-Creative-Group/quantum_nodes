import numpy as np
from numpy import pi
import scipy.linalg
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg
import sys

# This class is used to store all the computed frames
# and to determine the ones that need to be computed
# when the user is asking the data for a specific frame

class SimulationCache:
    def __init__(self, max_frame):
        """
        @parameter :
        max_frame - integer - the length of the simulation, in frames
        """
        self._data = np.empty((max_frame), np.ndarray)
        self._last_computed_frame = None
    
    def __processFrame(self, d, inp):
        """
        Computes the next frame.
        This method is only an implementation of the plot_animation() function taken from the source code.
         
        @parameters : 
        d   - SimulationDataManager
        inp - SimulationInputsManager
        """
        vector_selon_x = d.xConcatenate(d._wave_function, inp._dimension)
        vector_derive_y_selon_x = d.xConcatenate(d.dySquare(d._wave_function, inp._dimension, inp._step), inp._dimension)
        U_selon_x = vector_selon_x + (1j*inp._delta_t/2)*(vector_derive_y_selon_x - d._v_x*vector_selon_x)
        U_selon_x_plus = scipy.sparse.linalg.spsolve(d._hx, U_selon_x)

        d._wave_function = d.xDeconcatenate(U_selon_x_plus, inp._dimension)

        vector_selon_y = d.yConcatenate(d._wave_function, inp._dimension)
        vector_derive_x_selon_y = d.yConcatenate(d.dxSquare(d._wave_function, inp._dimension, inp._step), inp._dimension)
        U_selon_y = vector_selon_y  + (1j*inp._delta_t/2)*(vector_derive_x_selon_y - d._v_y*vector_selon_y)
        U_selon_y_plus = scipy.sparse.linalg.spsolve(d._hy, U_selon_y)

        d._wave_function = d.yDeconcatenate(U_selon_y_plus, inp._dimension)
    

    def getFrame(self, frame, d, inp):
        """
        Returns the requested data at the given frame.
        Manages the situations where several frames need to be
        calculated in order to return the requested data.

        @parameters :
        frame   - integer - index of the frame
        d       - SimulationDataManager
        inp     - SimulationInputsManager
        """
        if(frame >= 0):
            if(frame <= self._last_computed_frame):
                # the frame has already been computed
                return self._data[frame]
            elif(frame <= inp._frame_rate * inp._duration):
                # the frame is in the scope of the simulation
                # but has not been computed yet
                frames_to_compute = frame - self._last_computed_frame
                try:
                    for frame in range(frames_to_compute):
                        self.__processFrame(d, inp)
                        self._last_computed_frame += 1
                        self._data[self._last_computed_frame] = d._wave_function
                except Exception as e:
                    print(sys.exc_info())
                    raise e from e
                return self._data[frame]
            else:
                # the requested frame is not in the scope of the simulation
                # return the last computed frame by default
                return self._data[self._last_computed_frame]
        else:
            # the requested frame is negative
            raise IndexError("ERROR::SimulationCache::getFrame() frame index out of range\nData for frame n°" + str(frame) + " unavailable")