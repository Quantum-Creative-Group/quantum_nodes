import numpy as np
from numpy import sin, cos, exp, pi, tan, log, sinh, cosh, tanh, sinc, sqrt, cbrt, angle, real, imag, abs, arcsin, arccos, arctan, arcsinh, arccosh, arctanh
from numpy import pi, e

# This class Manages all the user inputs
# All these methods are taken from field.py
# source code : https://github.com/Azercoco/Python-2D-Simulation-of-Schrodinger-Equation/blob/master/field.py

class SimulationInputsManager:
	def __init__(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
		"""
		@parameters :
		dim 	- integer 	- size of the 2d grid, which corresponds to dim**2 points 
		size 	- integer 	- scale of the simulation
		center 	- vector 2d - starting position of the wave packet
		n_o_w 	- vector 2d - number of waves that compose the wave packet
		spr 	- vector 2d - spreading of the wave packet
		pot 	- string 	- boolean expression of the potential (in function of x and y)
		obs 	- string 	- boolean expression of the obstacle.s (in function of x and y)
		fr 		- integer 	- frame rate of the simulation
		d 		- float 	- duration of the simulation
		dt 		- float 	- simulation time spent for each second of animation
		"""
		self._dimension = dim
		self._size = size
		self._step = size/dim
		self._center = center
		self._number_of_waves = n_o_w
		self._spreading = spr
		try:
			self.setPotential(pot)
			self.setObstacle(obs)
		except Exception as e:
			raise e from e
		self._frame_rate = fr
		self._duration = d
		self._delta_t = dt/fr

	def hasChanged(self, dim, size, center, n_o_w, spr, pot, obs, fr, d, dt):
		"""
		Returns true if any of the inputs have changed, false otherwise
		@parameters :
		same as __init__ method
		"""
		new_inputs = [dim, size, center, n_o_w, spr, pot, obs, fr, d, dt/fr]
		current_inputs = [self._dimension, self._size, self._center, self._number_of_waves,\
						  self._spreading, self._potential_expr, self._obstacle_expr, self._frame_rate,\
						  self._duration, self._delta_t]
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
		if(self.__verifyPotentialExpr(expr)):
			self._potential_expr = expr
		else:
			self._potential_expr = "0"

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
		if(self.__verifyObstacleExpr(expr)):
			self._obstacle_expr = expr
		else:
			self._obstacle_expr = "False"
	
	def isObstacle(self, x, y):
		if(self.__verifyObstacleExpr(self._obstacle_expr)):
			return eval(self._obstacle_expr)
		else:
			return False
	
	def getPotential(self, x, y):
		if(self.__verifyPotentialExpr(self._potential_expr)):
			return eval(self._potential_expr)
		else:
			return 0 + 0j

