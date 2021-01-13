import numpy as np
from numpy import sin, cos, exp, pi, tan, log, sinh, cosh, tanh, sinc, sqrt, cbrt, angle, real, imag, abs, arcsin, arccos, arctan, arcsinh, arccosh, arctanh
from numpy import pi, e

class SimulationInputsManager:
	def __init__(self, dim, size, center, n_o_w, spr, pot, obs):
		self._dimension = dim
		self._size = size
		self._step = size/dim
		self._center = center
		self._number_of_waves = n_o_w # (Kx, Ky)
		self._sprawl = spr # étalement
		self._potential_expr = "0"
		self._obstacle_expr = "False"
		self.setPotential(pot)
		self.setObstacle(obs)

	@classmethod
	def __verifyPotentialExpr(self, expr):
		x, y = 0, 0
		try:
			test = eval(expr)
			return True
		except:
			print("ERROR::SchrödingerEquationSimulation : unable to evaluate the given potential formula '" + expr + "'\n"\
				  "Expression set to : '0'")
			return False
	
	@classmethod
	def setPotential(self, expr):
		if(self.__verifyPotentialExpr(expr)):
			self._potential_expr = expr
		else:
			self._potential_expr = "0"

	@classmethod
	def __verifyObstacleExpr(self, expr):
		x, y = 0, 0
		try:
			test = eval(expr)
			return True
		except:
			print("ERROR::SchrödingerEquationSimulation : unable to evaluate the given obstacle formula '" + expr + "'\n"\
				  "Expression set to : 'False'")
			return False
	
	@classmethod
	def setObstacle(self, expr):
		if(self.__verifyObstacleExpr(expr)):
			self._obstacle_expr = expr
		else:
			self._obstacle_expr = "False"
	
	@classmethod
	def isObstacle(self, x, y):
		if(self.__verifyObstacleExpr(self._obstacle_expr)):
			return eval(self._obstacle_expr)
		else:
			return False
	
	@classmethod
	def getPotential(self, x, y):
		if(self.__verifyPotentialExpr(self._potential_expr)):
			return eval(self._potential_expr)
		else:
			return 0 + 0j

