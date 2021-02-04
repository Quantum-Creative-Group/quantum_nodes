# Quantum Nodes
Quantum Nodes is an extension of [*Animation Nodes*](https://github.com/JacquesLucke/animation_nodes) for [*Blender*](https://github.com/blender).

Quantum Nodes provides you amazing tools to incorporate quantum computation into your creative process.<br>
It even allows you to send your quantum circuits to real qubits provided by [*IBM*](https://www.ibm.com/quantum-computing/experience).

Built using [*Qiskit*](https://github.com/Qiskit) and [*Anaconda*](https://github.com/Anaconda-Platform)

## Table of contents :bookmark_tabs:
1. Installation
   * [Linux](#linux)
   * [Windows](#windows)
   * [Mac](#mac)
2. [Contribute to our project](#contribute-to-our-project-wrench)

### Installation :computer:
#### Linux
1. [Download everything](#download-everything-linux) (almost)
2. [Prerequisite installations](#prerequisite-installations-linux)
3. [Installation of *Blender* add-ons](#installation-of-blender-addons-linux)

###### Download everything - Linux
* <ins>Download *Blender*</ins><br>

  Using the terminal:
  * `sudo add-apt-repository ppa:thomas-schiex/blender`
  * `sudo apt-get update`
  * `sudo apt-get install blender`<br><br>

  You can do it from the website, but it is not recommended for this tutorial.<br>
  From the website: https://www.blender.org/download/

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_blender_linux.png" alt="Blender website" height="200px"/>
  </p>

* <ins>Download *Anaconda*</ins><br>
  From the website: https://www.anaconda.com/products/individual

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_anaconda_linux_step2.png" alt="Anaconda website, download page" height="200px"/>
  </p>

  Or using the terminal:
  * `cd /tmp`
  * `curl https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh --output anaconda.sh`<br>
  See available versions [here](https://docs.anaconda.com/anaconda/install/hashes/lin-3-64/)
  * (Recommended) Compare your hash: `sha256sum anaconda.sh`<br>
  See official hashes [here](https://docs.anaconda.com/anaconda/install/hashes/lin-3-64/)<br><br>

* <ins>Download *Animation Nodes*</ins><br>
  From the website: https://animation-nodes.com/#download

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_animation_nodes_step1.png" alt="Animation Nodes website" height="100px"/>
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_animation_nodes_linux.png" alt="Animation Nodes website, download page" height="100px"/>
  </p>

* <ins>Download *Quantum Nodes*</ins><br>
  Download it from our repository
  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_quantum_nodes_step2.png" alt="Quantum Nodes repository, download" height="200px"/>
  </p>

###### Prerequisite installations - Linux
* <ins>Install *Blender*</ins>
  * If downloaded using the terminal: it's already done :ok_hand:
  * If downloaded from the website (not recommended here):<br>
  → As [mentioned here](https://docs.blender.org/manual/en/latest/getting_started/installing/linux.html), uncompress the content of the downloaded `.tar.xz` at the desired location (e.g. `~/software` or `usr/local`)

  → Launch it to check if everything went well :wink:
  
* <ins>Install *Anaconda*</ins>
  * Open a new terminal where the file is saved. Then enter: `bash file_name.sh`
  * During the installation:<br>
  → `Do you approve the license terms? [yes|no]` → `yes`<br>
  → You can choose a custom location for the *Anaconda* installation files. However, this tutorial uses the default location (recommended).<br>
  → `Do you wish the installer to initialize Anaconda3?` → `yes`
  * At the end: `source ~/.bashrc`<br><br>

* <ins>*Anaconda* environment and *Blender*</ins><br>
  In this part, we will create a new conda environment and install the necessary packages for *Quantum Nodes*.<br>
  Then, we will tell *Blender* to use our environment instead of the python that comes with by default.<br>

  * Open a new terminal:<br>
  Go where your *Blender* installation files are.<br>
  By default (when installed using the terminal), the files are located here: `cd /usr/share/blender/2.91/`<br>

  * Deactivate the current python version: `mv python _python`<br>

  * Create a new *Anaconda* environment:<br>
  **Warning**: as [mentioned here](https://docs.blender.org/api/current/info_tips_and_tricks.html#bundled-python-extensions), the python version ([major and minor](https://linuxize.com/post/how-to-check-python-version/)) must match the one that *Blender* comes with.<br>
  For *Blender* 2.91.2, python 3.7 is ok.<br>
  → Enter : `conda create --name=blender python=3.7`<br>
  → During the installation, type `y` to proceed when `Proceed ([y]/n) ?` appears.<br>
  → When the installation is finished, enter: `conda activate blender`<br>

  * Link the *Anaconda* environment to *Blender*:<br>
  If you have installed *Anaconda* with the default parameters, as we did in this tutorial, your conda env’ should be installed here: `~/anaconda3/envs/blender/`<br>
  → Enter in the terminal (replace with your custom path): `sudo ln -s ~/anaconda3/envs/blender/ python`<br>
  This creates a junction between the python folder in the *Blender* files and the folder in the *Anaconda* environments files.<br>

  * Install the needed python packages for *Quantum Nodes*:
    ```
    pip install pillow
    pip install scipy
    pip install qiskit
    ```

  * Then, open *Blender*, go to scripting and type in the python console: `import qiskit`<br>
  If *Blender* **does not** find *Qiskit*, you need to follow the next steps:<br>
  → Go here (using the terminal): `cd ~`<br>
  → Enter: `sudo nano .bashrc`<br>
  → Go at the end of the file (using the arrows) and add this in a new line: `export PYTHONNOUSERSITE=True`<br>
  → Close the document : (`ctrl + x` then `y` and `enter`)<br>
  Reopen *Blender*, it should now find *Qiskit*.<br>

###### Installation of *Blender* addons - Linux
* <ins>Preparations</ins>
  * Extract `quantum_nodes` folder from: `quantum-creative-master-quantum_nodes.zip`<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_quantum_nodes_linux_step0.png" alt="Quantum Nodes folders" height="200px"/>
  </p>


  * The problem is that *Gitlab* encapsulates the downloaded folder inside another folder so *Blender* can not see it.
  Zip the extracted folder:<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_quantum_nodes_linux_step01.png" alt="Quantum Nodes zip" height="120px"/>
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_quantum_nodes_linux_step2.png" alt="Quantum Nodes folder" height="120px"/>
  </p>


* <ins>In *Blender*</ins>
  * Open *Blender*<br>
  Go to: `edit > preferences`<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step1.png" alt="Blender, preferences" height="300px"/>
  </p>


   * Go to the add-on panel and click on `install`<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step1.5.png" alt="Blender, preferences, install" height="75px"/>
  </p>


  * Select *Animation Nodes*<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step2.png" alt="Blender, preferences, install add-on" height="300px"/>
  </p>


  * Click on `install add-on`. Don't forget to activate it (click on the checkbox):<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step3.png" alt="Blender, preferences, install add-on" height="125px"/>
  </p>


  * Repeat the three last steps to install *Quantum Nodes*
  
  **The end, enjoy** :blush:

#### Windows
1. [Download everything](#download-everything-windows) (almost)
2. [Prerequisite installations](#prerequisite-installations-windows)
3. [Installation of *Blender* addons](#installation-of-blender-addons-windows) (same as Linux)

###### Download everything - Windows
* <ins>Download *Blender*</ins>: https://www.blender.org/download/

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_blender.png" alt="Blender website" height="200px"/>
  </p>

* <ins>Download *Anaconda*</ins>: https://www.anaconda.com/products/individual

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_anaconda_step2.png" alt="Anaconda website, download page" height="200px"/>
  </p>

* <ins>Download *Animation Nodes*</ins>: https://animation-nodes.com/#download

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_animation_nodes_step1.png" alt="Animation Nodes website" height="100px"/>
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_animation_nodes_step2.png" alt="Animation Nodes website, download page" height="100px"/>
  </p>

* <ins>Download *Quantum Nodes*</ins><br>
  Download it from our repository

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/download_quantum_nodes_step2.png" alt="Quantum Nodes repository, download" height="200px"/>
  </p>

###### Prerequisite installations - Windows
* <ins>Install *Blender*</ins>
  * Double click on the previously downloaded file: `blender-2.91.2-windows64.msi`
  * Follow along the instructions given during the installation.<br>
  You can choose your own location to put the installation files of *Blender*. This tutorial uses the default location.<br>
  * Launch it to check if everything went well :wink:
  
* <ins>Install *Anaconda*</ins>
  * Double click on the previously downloaded file: `Anaconda3-2020.11-Windows-x86_64.exe`
  * Follow along the instructions given during the installation.<br>
  At this step, make sure to uncheck the second option (the text then appears in red):<br><br>

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_anaconda_step1.png" alt="Install Anaconda Windows" height="300px"/>
  </p>

  * Launch the anaconda navigator to check if everything went well :wink:<br><br>

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_anaconda_step2.png" alt="Install Anaconda Windows" height="100px"/>
  </p>

* <ins>*Anaconda* environment and *Blender*</ins><br>
  In this part, we will create a new conda environment and install the necessary packages for Quantum Nodes.<br>
  Then, we will tell *Blender* to use our environment instead of the python that comes with by default.<br>

  * Launch the anaconda prompt in administrator mode (`LEFT SHIFT + right click`):<br><br>
  
  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/create_conda_env_step1.png" alt="Install Anaconda Windows" height="100px"/>
  </p>

  * Go where your *Blender* installation files are (using cd).<br>
  By default, the files are located here : `C:\Program Files\Blender Foundation\Blender 2.91\2.91`<br>
  So enter : `cd C:\Program Files\Blender Foundation\Blender 2.91\2.91`<br>

  * Deactivate the current python version: `rename python _python`<br>

  * Create a new *Anaconda* environment:<br>
  **Warning**: as [mentioned here](https://docs.blender.org/api/current/info_tips_and_tricks.html#bundled-python-extensions), the python version ([major and minor](https://linuxize.com/post/how-to-check-python-version/)) must match the one that *Blender* comes with.<br>
  For *Blender* 2.91.2, python 3.7 is ok.<br>
  → Enter : `conda create --name=blender python=3.7`<br>
  → During the installation, type `y` to proceed when `Proceed ([y]/n) ?` appears.<br>
  → When the installation is finished, enter: `conda activate blender`<br>

  * Link the *Anaconda* environment to *Blender*:<br>
  If you have installed *Anaconda* with the default parameters, as we did in this tutorial, your conda env’ should be installed here : `C:\Users\your_username\anaconda3\envs\blender`<br>
  → Enter (replace with your custom path) : `mklink /j python “C:\Users\your_username\anaconda3\envs\blender”`<br>
  This creates a junction between the python folder in the *Blender* files and the folder in the *Anaconda* environments files.<br>

  * Install the needed python packages for *Quantum Nodes*:
    ```
    pip install pillow
    pip install scipy
    pip install qiskit
    ```
* <ins>Windows environment variables</ins><br>
  * Launch the environment variables manager:<br><br>

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_env_variables_step1.png" alt="Install Anaconda Windows" height="250px"/>
  </p>

  * Then, click on “Environment variables”:<br><br>

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_env_variables_step2.png" alt="Install Anaconda Windows" height="250px"/>
  </p>

  * Click on “edit / modify” (you can either edit the system variables or the current user variables):<br><br>

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_env_variables_step3.png" alt="Install Anaconda Windows" height="250px"/>
  </p>

  * Finally, add the following paths to the variable:<br><br>

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_env_variables_step4.png" alt="Install Anaconda Windows" height="100px"/>
  </p>

  `C:\Program Files\Blender Foundation\Blender 2.91\2.91\python`<br>
  `C:\Program Files\Blender Foundation\Blender 2.91\2.91\python\DLLs`<br>
  `C:\Program Files\Blender Foundation\Blender 2.91\2.91\python\Library\bin`<br>
  
  * Then click on `ok`, `ok`, `ok` to close everything :wink:

###### Installation of *Blender* addons - Windows
* <ins>Preparations</ins>
  * Extract `quantum_nodes` folder from: `quantum-creative-master-quantum_nodes.zip`<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step0.png" alt="Quantum Nodes folders" height="150px"/>
  </p>


  * The problem is that *Gitlab* encapsulates the downloaded folder inside another folder so *Blender* can not see it.
  Zip the extracted folder:<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step01.png" alt="Quantum Nodes zip" height="80px"/>
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step02.png" alt="Quantum Nodes folder" height="80px"/>
  </p>


* <ins>In *Blender*</ins>
  * Open *Blender*<br>
  Go to: `edit > preferences`<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step1.png" alt="Blender, preferences" height="300px"/>
  </p>


   * Go to the add-on panel and click on `install`<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step1.5.png" alt="Blender, preferences, install" height="75px"/>
  </p>


  * Select *Animation Nodes*<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step2.png" alt="Blender, preferences, install add-on" height="300px"/>
  </p>


  * Click on `install add-on`. Don't forget to activate it (click on the checkbox):<br>


  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/install_an_and_qn_step3.png" alt="Blender, preferences, install add-on" height="125px"/>
  </p>


  * Repeat the three last steps to install *Quantum Nodes*
  
  **The end, enjoy** :blush:

#### Mac

Work in progress ...

## Contribute to our project :wrench:

If you want to contribute you can use your favorite IDE our you can use Visual Studio Code that has a very interesting Extension for Blender Development made by Jacques Lucke :

* First you have to clone our repo
* Open Visual Studio Code and install *Blender Development*:

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/blender_dev.png" alt="Blender dev VSCode extension" height="200px"/>
  </p>

* Then you can follow the extension tutorial to set-up the "Blender: Start" directly from VS Code :

  <p align="center">
  <img src="https://gitlab.com/quantum-creative-group/quantum_nodes/-/raw/assets/tuto_blender_dev.png" alt="Blender dev VSCode extension, tutorial" height="450"/>
  </p>

Like this any updates you want to do will be taken into account when you save a file.<br>
You don't have to import again any ZIP file into Blender, the extension does it for you.

