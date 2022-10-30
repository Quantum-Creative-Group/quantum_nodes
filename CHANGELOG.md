# Change log

## [0.1.2] - 2022-10-30

Updated code and repository to new hosting platform (switched from Gitlab to Github).

<details><summary>Details</summary>

### Added

* Add first elements for Gitlab --> Github migration ([#2](https://github.com/Quantum-Creative-Group/quantum_nodes/pull/3))

### Fixed

* Update resources to Github ([#3](https://github.com/Quantum-Creative-Group/quantum_nodes/pull/3)) 
* [CI/CD] Fixed wrong name for master branch in workflow (b29383024240ec89568b5281de5a0b21e300549e)
* [Docs] Updated CHANGELOG (2de3256d3f3302830f518c6879df8f1642abd185)
* [Docs] Updated manual documentation (4bae25676c203ed56287a7d492f37c372bb52b60)
* Update documentation ([#4](https://github.com/Quantum-Creative-Group/quantum_nodes/pull/4))

</details>

## [0.1.1] - 2022-06-28

Fixes one bug (partially). This release is created to test the new CI/CD pipeline
and to update the installation tutorial in the documentation.

<details><summary>Details</summary>

### Fixed

- Error on creating new Bloch Sphere (!34)

</details>

------------------------------------------------------------------------------------------

## [0.1.0] - 2021-04-28

First release of the add-on.
This version implements the first nodes.
See the *added* section for more details.

<details><summary>Details</summary>

### Added

#### Nodes

* **Quantum gates**
  * Single qubit gates
    * Hadamard gate (H)
    * I gate (Id)
    * S gate (S)
    * SDG gate (SDG)
    * T gate (T)
    * TDG gate (TDG)
    * X gate (X)
    * Y gate (Y)
    * Z gate (Z)
  * R gates
    * RX gate (RX)
    * RY gate (RY)
    * RZ gate (RZ)
  * C gates
    * CH gate (CH)
    * CX gate (CX)
    * CY gate (CY)
    * CZ gate (CZ)
    * CCX gate (CCX)
    * CSWAP gate (CSWAP)
  * SWAP gate (SWAP)

* **Quantum circuits initialization**
  * Classical register
  * Quantum register
  * Quantum circuit

* **Outputs**
  * Visualization
    * Bloch sphere
    * Histogram
    * State city (*3D model still WIP*)
  * Circuit output
    * Get count
    * IBM output (*still WIP*)
    * Output state
    * Measure

* **James Wootton [QuantumBlur](https://github.com/qiskit-community/QuantumBlur)**
  * QuantumBlur input
  * QuantumBlur output

* **Numpy complex128**
  * Split complex128

* **Azercoco [2D simulation of Schrödinger equation](https://github.com/Azercoco/Python-2D-Simulation-of-Schrodinger-Equation)**
  * Schrödinger equation simulation

#### Sockets

* Classical register
* Quantum register
* Quantum circuit
* Quantum count
* Numpy long complex (complex128)

#### Visualization

* Bloch sphere
* Histogram

#### UI

* Quantum nodes menu (references all the nodes)
* Quantum nodes panel (references all the nodes, visualization tools and IBM connection)

#### Demo add-on

* Add a new mesh panel
  * Add a new mesh
  * Subdivide a mesh

* Demo panel
  * Select a new target
  * Delete the current target
  * Settings
    * Select axis
    * Select qubit
    * Add a gate (H, X or Y)
  * Visualize the circuit
  * Reset circuits
  * Apply quantum algorithm
  * Duplicate creation
  * Advanced (redirection to the animation nodes editor)
  * 'Need help ?' button
  * 'Creation gallery' button

### Fixed

### Changed

</details>