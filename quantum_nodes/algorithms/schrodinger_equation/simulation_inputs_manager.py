import numpy as np


class SimulationInputsManager:
    """
    This class manages all the user inputs.

    All these methods are taken from field.py.
    Source code : https://github.com/Azercoco/Python-2D-Simulation-of-Schrodinger-Equation/blob/master/field.py
    """

    def __init__(self, dim: int, size: int, center: np.ndarray, n_o_w: np.ndarray,
                 spr: np.ndarray, pot: str, obs: str, fr: int, d: float, dt: float):
        """
        Init method of the class.

        Args:
            dim (int): size of the 2d grid, which corresponds to dim**2 points
            size (int): scale of the simulation
            center (np.ndarray): starting position of the wave packet
            n_o_w (np.ndarray): number of waves that composes the wave packet
            spr (np.ndarray): spreading of the wave packet
            pot (str): boolean expression of the potential (in function of x and y)
            obs (str): boolean expression of the obstacle.s (in function of x and y)
            fr (int): frame rate of the simulation
            d (float): duration of the simulation
            dt (float): simulation time spent for each second of animation

        Raises:
            e: whenever something goes wrong during setPotential() or setObstacle()
        """

        self.dimension = dim
        self.size = size
        self.step = size / dim
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
        self.delta_t = dt / fr

    def hasChanged(self, dim: int, size: int, center: np.ndarray, n_o_w: np.ndarray,
                   spr: np.ndarray, pot: str, obs: str, fr: int, d: float, dt: float):
        """
        Check if node inputs have changed.

        Args:
            dim (int): size of the 2d grid, which corresponds to dim**2 points
            size (int): scale of the simulation
            center (np.ndarray): starting position of the wave packet
            n_o_w (np.ndarray): number of waves that composes the wave packet
            spr (np.ndarray): spreading of the wave packet
            pot (str): boolean expression of the potential (in function of x and y)
            obs (str): boolean expression of the obstacle.s (in function of x and y)
            fr (int): frame rate of the simulation
            d (float): duration of the simulation
            dt (float): simulation time spent for each second of animation

        Returns:
            bool: indicate if node inputs have changed
        """

        new_inputs = [dim, size, center, n_o_w, spr, pot, obs, fr, d, dt / fr]
        current_inputs = [self.dimension, self.size, self.center, self.number_of_waves,
                          self.spreading, self.potential_expr, self.obstacle_expr, self.frame_rate,
                          self.duration, self.delta_t]
        return not(all(new_inputs[i] == current_inputs[i] for i in range(np.size(current_inputs))))

    @classmethod
    def verifyPotentialExpr(cls, expr):
        # x, y = 0, 0
        try:
            eval(expr)
            return True
        except BaseException:
            # unable to evaluate the given potential formula
            # expression set to "0" by default
            raise ValueError("ERROR::SimulationInputsManager::verifyPotentialExpr()\n\
                             Unable to evaluate the given expression")

    def setPotential(self, expr: str):
        """
        Set the potential expression.

        Args:
            expr (str): boolean expression in function of x and y
        """

        if self.verifyPotentialExpr(expr):
            self.potential_expr = expr
        else:
            self.potential_expr = "0"

    @classmethod
    def verifyObstacleExpr(cls, expr):
        # x, y = 0, 0
        try:
            eval(expr)
            return True
        except BaseException:
            # unable to evaluate the given obstacle formula
            # expression set to "False" by default
            raise ValueError("ERROR::SimulationInputsManager::verifyObstacleExpr()\n\
                             Unable to evaluate the given expression")

    def setObstacle(self, expr: str):
        """
        Set the obstacle expression.

        Args:
            expr (str): boolean expression in function of x and y
        """

        if self.verifyObstacleExpr(expr):
            self.obstacle_expr = expr
        else:
            self.obstacle_expr = "False"

    def isObstacle(self, x, y):
        if self.verifyObstacleExpr(self.obstacle_expr):
            return eval(self.obstacle_expr)
        else:
            return False

    def getPotential(self, x, y):
        if self.verifyPotentialExpr(self.potential_expr):
            return eval(self.potential_expr)
        else:
            return 0 + 0j
