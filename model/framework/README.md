# **MODEL EOS74BO**

This repository contains the code for the QSAR models for Kinetic Aqueous Solubility endpoints. To use the application locally, you can either use [Git](https://git-scm.com/) to clone the respository, or you can simply download a ZIP file (by clicking the green "Code" button on the top right corner) and then unzip it. The next steps are described below.

`https://github.com/ersilia-os/eos8ykt.git`

#
## **Installing required software**

1. Install [anaconda or miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html#)

Python is also required but it is included with either installation of conda or miniconda.

#
## **Steps to run the application**
A conda environment is used to run the application. You only have complete the steps once.
#
### **With conda**
1. Open your Anaconda terminal
2. Create environment
    ```
    conda env create --prefix <name-of-env> -f environment.yml
    ```
    - Wait for the envitonment to be created
3. Type `conda activate <name-of-env>` and hit Enter
4. Change directory to model/checkpoints
5. Type `python main.py ../input.csv ../<outout-file>.csv` and hit Enter
6. To close the application, hit `Ctrl + c` or `Cmd + c` in the Terminal and then type `conda deactivate` and hit Enter to close the conda environment


- For Windows and Linux machines
    1. Type `conda env create --prefix ./env -f environment.yml` and hit Enter
    2. Wait several minutes for the envitonment to be created
    3. For Windows machines only, type `pip install typed-argument-parser` and hit Enter
  - For Mac machines
    1. Type `conda env create --prefix ./env -f environment_mac.yml` and hit Enter
    2. Wait several minutes for the envitonment to be created

## Running the application

1. If you're doing this immediately after completing the steps above, skip to step 4
2. Open your terminal
  - If you're on Windows, open Anaconda Prompt (window -> Anaconda3 -> Anaconda Prompt)
  - If you're on Mac or Linux, open your terminal
3. Change the working directory ([windows](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands) or [Mac and Linux](https://www.geeksforgeeks.org/cd-command-in-linux-with-examples/)) to where you have ADME_RLM and then go into the server directory
4. Type `conda activate ./env` and hit Enter

<!-- Python 3.8.16 -->