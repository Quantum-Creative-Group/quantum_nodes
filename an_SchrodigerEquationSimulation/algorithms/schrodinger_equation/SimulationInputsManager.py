import numpy as np
from numpy import sin, cos, exp, pi, tan, log, sinh, cosh, tanh, sinc, sqrt, cbrt, angle, real, imag, abs, arcsin, arccos, arctan, arcsinh, arccosh, arctanh
from numpy import pi, e

class SimulationInputsManager:
	def __init__(self, dim, size, center, n_o_w, spr, pot, obs):
		self._dimension = dim
		self._size = size
		self._center = center
		self._number_of_waves = n_o_w # (Kx, Ky)
		self._sprawl = spr # étalement
		self._potential_expr = "0"
		self._obstacle_expr = "False"
		self.setPotential(self, expr)
		self.setObstacle(self, expr)

	@classmethod
	def __verifyPotentialExpr(self, expr):
		x, y = 0, 0
		try:
			test = eval(expr)
			return true
		except:
			print("ERROR::SchrödingerEquationSimulation : unable to evaluate the given potential formula '" + expr "'\n"\
				  "Expression set to : '0'")
			return false
	
	@classmethod
	def setPotential(self, expr):
		if(__verifyPotentialExpr(self, expr)):
			self._potential_expr = expr
		else:
			self._potential_expr = "0"

	@classmethod
	def __verifyObstacleExpr(self, expr):
		x, y = 0, 0
		try:
			test = eval(expr)
			return true
		except:
			print("ERROR::SchrödingerEquationSimulation : unable to evaluate the given obstacle formula '" + expr "'\n"\
				  "Expression set to : 'False'")
			return false
	
	@classmethod
	def setObstacle(self, expr):
		if(__verifyObstacleExpr(self, expr)):
			self._obstacle_expr = expr
		else:
			self._obstacle_expr = "False"
	
	@classmethod
	def isObstacle(self, x, y):
		if(__verifyObstacleExpr(self, self._obstacle_expr)):
			return eval(self._obstacle_expr)
		else:
			return False
	
	@classmethod
	def getPotential(self, x, y):
		if(self.__verifyPotentialExpr(self, self._potential_expr)):
			return eval(self._potential_expr)
		else:
			return 0 + 0j
		



# potential_expr = None
# obstacle_expr = None


# def setPotential(expr):
# 	global potential_expr
# 	potential_expr = expr
# 	test_pot_expr()

# def setObstacle(expr):
# 	global obstacle_expr
# 	obstacle_expr = expr
# 	test_obs_expr() 


# def test_pot_expr():
# 	global potential_expr
# 	x = 0
# 	y = 0
# 	try:
# 		a = eval(potential_expr)
# 	except:
# 		print(potential_expr)
# 		print('Erreur de calcul du potentiel : mis à 0 par défaut')
# 		potential_expr = '0'
# 		input('Appuyez sur une touche poour continuer')

# def test_obs_expr():
# 	global obstacle_expr
# 	x = 0
# 	y = 0
# 	try:
# 		a = eval(obstacle_expr)
# 	except e:
		
# 		print('Erreur lors de la definition de l\'obsatcle : Mis à False par défaut')
# 		obstacle_expr = 'False'
# 		input('Appuyez sur une touche poour continuer')


# def isObstacle(x, y):
# 	a = False
# 	try:
# 		a = eval(obstacle_expr)
# 	except:
# 		pass
# 	return a

# def getPotential(x, y):
# 	a = 0 + 0j
# 	try:
# 		a = eval(potential_expr)
# 	except:
# 		pass
# 	return a

