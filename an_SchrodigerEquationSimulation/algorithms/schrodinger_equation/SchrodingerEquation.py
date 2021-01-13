import numpy as np
from numpy import pi
import scipy.linalg
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg
import time, sys
from SimulationInputsManager import SimulationInputsManager
from SimulationDataManager import SimulationDataManager

class SchrodingerEquation:
	def __init__(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
		self._inputs = SimulationInputsManager(dim, size, center, n_o_w, spr, pot, obs)
		self._data = SimulationDataManager()
		self._frame_rate = fr
		self._duration = d
		self._delta_t = dt
		self._cache = None

	@classmethod
	def initialize(self):
		d = self._data		# data container
		inp = self._inputs	# inputs container
		d._x_axis = np.linspace(-inp._size/2, inp._size/2, d._dimension)
		d._y_axis = np.linspace(-inp._size/2, inp._size/2, d._dimension)
		d._x, d._y = np.meshgrid(d._x_axis, d._y_axis)

		phase = np.exp( 1j*(d._x*d._number_of_waves[0] + d._y*d._number_of_waves[1]))
		px = np.exp( - ((d._centre[0] - d._x)**2)/(4*d._sprawl[0]**2))
		py = np.exp( - ((d._centre[1] - d._y)**2)/(4*d._sprawl[1]**2))
		d._wave_function = phase*px*py
		norm = np.sqrt(d.integrate(np.abs(d._wave_function)**2, d._dimension, inp._step))
		d._wave_function = d._wave_function/norm

		d._laplace_matrix = sp.sparse.lil_matrix(-2*sp.sparse.identity(d._dimension**2))
		for i in range(d._dimension):
			for j in range(d._dimension-1):
				k = i*d._dimension + j
				d._laplace_matrix[k,k+1] = 1
				d._laplace_matrix[k+1,k] = 1

		d._v_x = np.zeros(d._dimension**2, dtype='c16')

		for j in range(d._dimension):
			for i in range(d._dimension):
				xx, yy = i, d._dimension*j
				if inp.isObstacle(d._x_axis[j], d._y_axis[i]):
					d._v_x[xx+yy] = inp._potential_wall
				else:
					d._v_x[xx+yy] = inp.getPotential(d._x_axis[j], d._y_axis[i])

		d._v_y = np.zeros(d._dimension**2, dtype='c16')

		for j in range(d._dimension):
			for i in range(d._dimension):
				xx, yy = j*d._dimension, i
				if inp.isObstacle(d._x_axis[i], d._y_axis[j]):
					d._v_y[xx+yy] = inp._potential_wall
				else:
					d._v_y[xx+yy] = inp.getPotential(d._x_axis[i], d._y_axis[j])

		V_x_matrix = sp.sparse.diags([d._v_x], [0])
		V_y_matrix = sp.sparse.diags([d._v_y], [0])
		d._laplace_matrix = d._laplace_matrix/(inp._step**2)

		d._h1 = (1*sp.sparse.identity(d._dimension**2) - 1j*(self._delta_t/2)*(d._laplace_matrix))
		d._h1 = sp.sparse.dia_matrix(d._h1)

		d._hx = (1*sp.sparse.identity(d._dimension**2) - 1j*(self._delta_t/2)*(d._laplace_matrix - V_x_matrix))
		d._hx = sp.sparse.dia_matrix(d._hx)

		d._hy = (1*sp.sparse.identity(d._dimension**2) - 1j*(self._delta_t/2)*(d._laplace_matrix - V_y_matrix))
		d._hy = sp.sparse.dia_matrix(d._hy)

		for i in range(0, d._dimension):
			for j in range(0, d._dimension):
				if inp.isObstacle(d._x_axis[j], d._y_axis[i]):
					adj = d.getAdjPos(i, j, d._dimension)
					for xx, yy in adj:
						if xx >= 0 and yy >= 0 and xx < d._dimension and yy < d._dimension and not inp.isObstacle(d._x_axis[yy], d._y_axis[xx]):
							d._potential_boudnary.append((i, j))
	
	@classmethod
	def processFrame(self, frame):
		d = self._data		# data container
		inp = self._inputs	# inputs container
		vector_selon_x = d.xConcatenate(d._wave_function, d._dimension) 	

		vector_derive_y_selon_x = d.xConcatenate(d.dySquare(d._wave_function, d._dimension, inp._step), d._dimension)
		U_selon_x = vector_selon_x + (1j*self._delta_t/2)*(vector_derive_y_selon_x - d._v_x*vector_selon_x)
		U_selon_x_plus = scipy.sparse.linalg.spsolve(d._hx, U_selon_x)

		d._wave_function = d.xDeconcatenate(U_selon_x_plus, d._dimension)

		vector_selon_y = d.yConcatenate(d._wave_function, d._dimension) 	
		vector_derive_x_selon_y = d.yConcatenate(d.dxSquare(d._wave_function, d._dimension, inp._step), d._dimension)
		U_selon_y = vector_selon_y  + (1j*self._delta_t/2)*(vector_derive_x_selon_y - d._v_y*vector_selon_y)
		U_selon_y_plus = scipy.sparse.linalg.spsolve(d._hy, U_selon_y)

		d._wave_function = d.yDeconcatenate(U_selon_y_plus, d._dimension)