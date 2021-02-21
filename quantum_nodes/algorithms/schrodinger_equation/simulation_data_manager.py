import numpy as np

class SimulationDataManager:
	"""This class manages all the data needed to compute the next frame.
	All these methods are taken from util.py.
	Source code : https://github.com/Azercoco/Python-2D-Simulation-of-Schrodinger-Equation/blob/master/util.py
	"""
	def __init__(self):
		self.x_axis, self.y_axis = None, None
		self.v_x, self.v_y = None, None
		self.wave_function = None
		self.potential_wall = 1e10
		self.potential_boundary = None
		self.laplace_matrix = None
		self.h1, self.hx, self.hy = None, None, None
		self.x, self.y = None, None

	@classmethod
	def xConcatenate(cls, MM, N):
		result = []
		for j in range(N):
			for i in range(N):
				result.append(MM[i][j])	
		return np.array(result, dtype='c16')

	@classmethod
	def xDeconcatenate(cls, vector, N):
		result = np.zeros((N, N), dtype='c16')
		for j in range(N):
			for i in range(N):
				result[i][j] = vector[N*j + i]
		return result

	@classmethod
	def yConcatenate(cls, MM, N):
		result = []
		for i in range(N):
			for j in range(N):
				result.append(MM[i][j])	
		return np.array(result, dtype='c16')

	@classmethod
	def yDeconcatenate(cls, vector, N):
		result = np.zeros((N, N), dtype='c16')
		for i in range(N):
			for j in range(N):
				result[i][j] = vector[N*i + j]
		return result

	@classmethod
	def dxSquare(cls, MM, N, step):
		result = np.zeros((N, N), dtype='c16')
		for j in range(N):
			result[0][j] = MM[1][j] - 2*MM[0][j]
			for i in range(1, N-1):
				result[i][j] = MM[i+1][j] + MM[i-1][j] - 2*MM[i][j]
			result[N-1][j] = MM[N-2][j] - 2*MM[N-1][j]
		return result / (step**2)

	@classmethod
	def dySquare(cls, MM, N, step):
		result = np.zeros((N, N), dtype='c16')
		for j in range(N):
			result[j][0] = MM[j][1] - 2*MM[j][0]
			for i in range(1, N-1):
				result[j][i] = MM[j][i+1] + MM[j][i-1] - 2*MM[j][i]
			result[j][N-1] = MM[j][N-2] - 2*MM[j][N-1]
		return result / (step**2)

	@classmethod
	def applyObstacle(cls, MM, N, mesh_x, mesh_y, sim_inputs):
		for i in range(N):
			for j in range(N):
				if sim_inputs.isObstacle(mesh_x[i][j], mesh_y[i][j]):
					MM[i][j] = 0 + 0j
		return MM

	@classmethod
	def getAdjPos(cls, x, y, N):
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
	def integrate(cls, MM, N, step):
		a, air = 0, step*step/2
		for i in range(N-1):
			for j in range(N-1):
				AA, AB, BA, BB = MM[i][j], MM[i][j+1], MM[i+1][j], MM[i+1][j+1]
				a += air*(AA+AB+BA)/3
				a += air*(BB+AB+BA)/3
		return a