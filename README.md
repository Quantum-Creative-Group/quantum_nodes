# Quantum Creative
Project of a Blender add-on in Python 3 using Qiskit.

## Installation On Linux
### Animation Nodes
Follow these steps to use Animation Nodes :

* First download Animation Nodes from the official website : https://animation-nodes.com/
* Install it in Blender Preferences Panel (go to Edit/Preferences/Add-Ons) :

![Preferences Panel image](assets/readme_pictures/preferences_panel.png)


### Quantum Creative
#### Prerequisite

Qiskit and PIL have to be installed on your machine and Blender has to use your version of Python Anaconda. If it is not done yet you can follow the step by step tutorial :

* Install Anaconda 3.8 from the official website : https://www.anaconda.com/products/individual

* Then install the required libraries :

```
conda activate

pip install numpy
pip install qiskit
pip install pillow
```

* Go to /usr/share/blender/*blender-version*/ and open a terminal :

```
sudo ln -s ~/anaconda3/ . && sudo mv anaconda3 python
```
It's ready ! Blender is now using Anaconda 3 with your libraries to run.

* Download the ZIP file from Gitlab (you can download from "master" but a version with more content but a little bit less stable is available on the "dev" branch)
* Copy the content of quantum-creative/an_quantic/sockets in /home/*username*/.config/blender/2.91/scripts/addons/animation_nodes/sockets

![Animation Nodes Folder image](assets/readme_pictures/animation_nodes_folder.png)

* Then do the same as Animation Nodes and install our extension in Blender

* Finally, you can find our extension in the Animation Nodes Panel and start messing around with it ! More nodes and features will be available in next updates. 

![Animation Nodes Quantum Menu image](assets/readme_pictures/quantum_menu.png)
