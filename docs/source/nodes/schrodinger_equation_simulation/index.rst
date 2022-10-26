2D Schrödinger equation simulation
==================================


Description
***********

|   This node is an implementation of a 2D simulation of the `Schrödinger equation <https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation>`_.
|   **Important to know**:

* The node outputs the state of the simulation at the current frame.
* All the simulation data are stored for each frame.
  Whenever a parameter changes, all the data for the current simulation are deleted.
* The simulation depends on all the previous frames. So if you suddenly ask for a frame that 
  was not already computed and that is "far" from the last computed frame, the simulation 
  can take a few seconds to compute this frame (since it has to compute all the previous frames). 


Outputs
*******

*   |   **Output**: 2d grid of complex numbers. The grid is formatted this way: 

    .. raw:: html

        <pre>
        [z_11, ..., z_1n, z_21, ..., z_2n, ..., z_n1, ..., z_nn]<br>
         ^ ----------- ^, ...   ..., ...   ..., ^ ----------- ^<br>
            n numbers        ...        ...        n numbers
        </pre>

    |   This output is fully equivalent to a n*n matrix.

*   |   **Offset**: size of the 2d grid.
    |   This offset can help you to naviguate through all the data as if it was a matrix.


Inputs
******

* Time-related parameters
    * **Frame rate**: frame rate of the simulation.
    * **Duration**: duration of the simulation.
    * **Δt**: simulation time spent for each second of animation.

* Precision-related parameters.
    * **Dimension**: size of the 2d grid.
    * **Scale**: scale of the simulation.

* Wave packet-related parameters
    * **Center**: starting position of the wave packet.
    * **Number** of waves: number of waves that compose the wave packet.
    * **Spreading**: spreading of the wave packet.

* **Potential**: boolean expression of the potential (in function of x and y).
* **Obstacle**: boolean expression of the obstacle.s (in function of x and y).


More information
****************

This node is made possible thanks to `Azercoco <https://github.com/Azercoco>`_ and his implementation of the simulation,
`see the projet on github <https://github.com/Azercoco/Python-2D-Simulation-of-Schrodinger-Equation>`_.