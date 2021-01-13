import numpy as np
from numpy import pi
import os

class SimulationDataManager:
	def __init__(self):
		self._x_axis, self._y_axis = None, None
		self._v_x, self._v_y = None, None
		self._wave_function = None
		self._potential_wall = 1e10
		self._potential_boundary = None
		self._laplace_matrix = None
		self._h1, self._hx, self._hy = None, None, None
		self._x, self._y = None, None

	@classmethod
	def xConcatenate(self, MM, N):
		result = []
		for j in range(N):
			for i in range(N):
				result.append(MM[i][j])	
		return np.array(result, dtype='c16')

	@classmethod
	def xDeconcatenate(self, vector, N):
		result = np.zeros((N, N), dtype='c16')
		for j in range(N):
			for i in range(N):
				result[i][j] = vector[N*j + i]
		return result

	@classmethod
	def yConcatenate(self, MM, N):
		result = []
		for i in range(N):
			for j in range(N):
				result.append(MM[i][j])	
		return np.array(result, dtype='c16')

	@classmethod
	def yDeconcatenate(self, vector, N):
		result = np.zeros((N, N), dtype='c16')
		for i in range(N):
			for j in range(N):
				result[i][j] = vector[N*i + j]
		return result

	@classmethod
	def dxSquare(self, MM, N, step):
		result = np.zeros((N, N), dtype='c16')
		for j in range(N):
			result[0][j] = MM[1][j] - 2*MM[0][j]
			for i in range(1, N-1):
				result[i][j] = MM[i+1][j] + MM[i-1][j] - 2*MM[i][j]
			result[N-1][j] = MM[N-2][j] - 2*MM[N-1][j]
		return result / (step**2)

	@classmethod
	def dySquare(self, MM, N, step):
		result = np.zeros((N, N), dtype='c16')
		for j in range(N):
			result[j][0] = MM[j][1] - 2*MM[j][0]
			for i in range(1, N-1):
				result[j][i] = MM[j][i+1] + MM[j][i-1] - 2*MM[j][i]
			result[j][N-1] = MM[j][N-2] - 2*MM[j][N-1]
		return result / (step**2)

	@classmethod
	def applyObstacle(self, MM, N, mesh_x, mesh_y, sim_inputs):
		for i in range(N):
			for j in range(N):
				if sim_inputs.isObstacle(mesh_x[i][j], mesh_y[i][j]):
					MM[i][j] = 0 + 0j
		return MM

	@classmethod
	def getAdjPos(self, x, y, N):
		res = []
		res.append((x-1,y))
		res.append((x+1,y))
		res.append((x, y - 1))
		res.append((x,y+1))
		res.append((x - 1,y+1))
		res.append((x - 1,y-1))
		res.append((x + 1,y+1))
		res.append((x+1, y+1))
		return res

	@classmethod
	def integrate(self, MM, N, step):
		a, air = 0, step*step/2
		for i in range(N-1):
			for j in range(N-1):
				AA, AB, BA, BB = MM[i][j], MM[i][j+1], MM[i+1][j], MM[i+1][j+1]
				a += air*(AA+AB+BA)/3
				a += air*(BB+AB+BA)/3
		return a