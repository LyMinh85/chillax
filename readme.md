<p align="center">
  <img width="96" align="center" src="assets/images/logo.png" alt="logo">
</p>
  <h1 align="center">
  Chillax
</h1>
<p align="center">
  A cross-platform music player based on Tkinter and CustomTkinter
</p>

<p align="center">

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Python-3.10-blue.svg?color=00B16A" alt="Python 3.10"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Tkinter-8.6-00B16A" alt="Tkinter 8.6"/>
  </a>
    
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/CustomTkinter-5.1.2-00B16A" alt="CustomTkinter 5.1.2"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Win32%20|%20Linux%20|%20macOS-blue?color=00B16A" alt="Platform Win32 | Linux | macOS"/>
  </a>
</p>

## Quick start
### Windows OS
1. If python is not in your system
   - [Install python3.10 or higher version](https://www.python.org/downloads/)

2. Create a venv and install all requirements:
   ```shell
    git clone https://github.com/LyMinh85/chillax.git
    cd chillax
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```
3. Run Chillax App
    ```shell
    python Chillax.py
    ```
   
4. Compile Chillax.py using Pyinstaller
   ```shell
   pyinstaller --clean Chillax.spec
   ```
### Linux OS
1. If python is not in your system
   ```shell
   sudo apt install software-properties-common -y
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt install python3.10
   ```
2. If pip is not in your system
   ```shell
   sudo apt-get install python-pip
   ```
3. If Tkinter and venv are not in your system
   ```shell
   sudo apt install python3.10-venv
   sudo apt-get install python3.10-tk
   ```
4. Create a venv and install all requirements:
    ```shell
    git clone https://github.com/LyMinh85/chillax.git
    cd chillax
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```
5. Run Chillax App
    ```shell
    python3 Chillax.py
    ```
   
### MacOS
1. If python is not in your system
   - [Install python3.10 or higher version](https://www.python.org/downloads/macos/)

2. Create a venv and install all requirements:
   ```shell
    git clone https://github.com/LyMinh85/chillax.git
    cd chillax
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. Run Chillax App
    ```shell
    python Chillax.py
    ```