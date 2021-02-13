import numpy as np
from numpy import sin, cos, exp, pi, tan, log, sinh, cosh, tanh, sinc, sqrt, cbrt, angle, real, imag, abs, arcsin, arccos, arctan, arcsinh, arccosh, arctanh
from numpy import pi, e

class SimulationInputsManager:
	"""This class manages all the user inputs.
	All these methods are taken from field.py.
	Source code : https://github.com/Azercoco/Python-2D-Simulation-of-Schrodinger-Equation/blob/master/field.py
	"""
	def __init__(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
		"""
		:param dim: size of the 2d grid, which corresponds to dim**2 points
		:type dim: int
		:param size: scale of the simulation
		:type size: int
		:param center: starting position of the wave packet
		:type center: vector 2d
		:param n_o_w: number of waves that composes the wave packet
		:type n_o_w: vector 2d
		:param spr: spreading of the wave packet
		:type spr: vector 2d
		:param pot: boolean expression of the potential (in function of x and y)
		:type pot: string
		:param obs: boolean expression of the obstacle.s (in function of x and y)
		:type obs: string
		:param fr: frame rate of the simulation
		:type fr: int
		:param d: duration of the simulation
		:type d: float
		:param dt: simulation time spent for each second of animation
		:type dt: float
		:raises e: whenever something goes wrong during setPotential() or setObstacle()
		"""
		self.dimension = dim
		self.size = size
		self.step = size/dim
		self.center = center
		self.number_of_waves = n_o_w
		self.spreading = spr
		try:
			self.setPotential(pot)
			self.setObstacle(obs)
		except Exception as e:
			raise e from e
		self.frame_rate = fr
		self.duration = d
		self.delta_t = dt/fr

	def hasChanged(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
		"""Check if the node inputs have changed.
		Parameters : same as the __init__ method.
		"""
		new_inputs = [dim, size, center, n_o_w, spr, pot, obs, fr, d, dt/fr]
		current_inputs = [self.dimension, self.size, self.center, self.number_of_waves,\
						  self.spreading, self.potential_expr, self.obstacle_expr, self.frame_rate,\
						  self.duration, self.delta_t]
		return not(all(new_inputs[i] == current_inputs[i] for i in range(np.size(current_inputs))))

	@classmethod
	def __verifyPotentialExpr(cls, expr):
		x, y = 0, 0
		try:
			test = eval(expr)
			return True
		except:
			# unable to evaluate the given potential formula
			# expression set to "0" by default
			raise ValueError("ERROR::SimulationInputsManager::__verifyPotentialExpr()\nUnable to evaluate the given expression")
	
	def setPotential(self, expr):
		"""Set the potential expression.

		:param expr: boolean expression in function of x and y
		:type expr: string
		"""
		if self.__verifyPotentialExpr(expr):
			self.potential_expr = expr
		else:
			self.potential_expr = "0"

	@classmethod
	def __verifyObstacleExpr(cls, expr):
		x, y = 0, 0
		try:
			test = eval(expr)
			return True
		except:
			# unable to evaluate the given obstacle formula
			# expression set to "False" by default
			raise ValueError("ERROR::SimulationInputsManager::__verifyObstacleExpr()\nUnable to evaluate the given expression")
	
	def setObstacle(self, expr):
		"""Set the obstacle expression.

		:param expr: boolean expression in function of x and y
		:type expr: string
		"""
		if self.__verifyObstacleExpr(expr):
			self.obstacle_expr = expr
		else:
			self.obstacle_expr = "False"
	
	def isObstacle(self, x, y):
		if self.__verifyObstacleExpr(self.obstacle_expr):
			return eval(self.obstacle_expr)
		else:
			return False
	
	def getPotential(self, x, y):
		if self.__verifyPotentialExpr(self.potential_expr):
			return eval(self.potential_expr)
		else:
			return 0 + 0j

