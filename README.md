# CS475 Senior Project - MindGames
Brandon Knotek, Walid Muhammad, and Jack Wilder

## Introduction
This repository contains the code and documentation for our senior research project, which we're calling MindGames. The goal of the project is to explore the viability of neurofeedback as a means for controlling real-time interactive experiences. Such a system would allow individuals with physical disabilities to interact with those experiences in a way that is often impossible using traditional physical control schemes.

To accomplish our goal, we have developed a simple Pac-Man clone in JavaScript. The game is supported by a Flask backend, which communicates with a separate module that is dedicated to handling EEG data. This data is collected using an OpenBCI Cyton board mounted to an OpenBCI Ultracortex headset. As the data is collected, it is filtered and parsed to game commands using Neuropype. Those commands are then sent to the game using the flask-sock extension and JavaScript's built-in WebSocket API. With this setup, users are able to control the game simply by thinking commands, eliminating the need for keyboard interaction.

## Setup
MindGames was built using a Python virtual environment. To run the application on your local machine, it is necessary to first establish a copy of this environment. To accomplish this, first open a terminal instance in the root directory, `\cs475_capstone`. Run the command `python -m venv env`. This creates a subdirectory, `\cs475_capstone\env`, which contains the virtual environment. Note that the root directory contains a `.gitignore` file that tells Git to ignore this subdirectory.

With the virtual environment in place, it must be activated. In Windows PowerShell, this can be accomplished by using the command `env\Scripts\Activate.ps1`. The input line of the terminal should now indicate that the virtual environment has been activated. If this is the first time you've activated the virtual environment (or if new Python packages have been added as dependencies), you must install any package dependencies before running the application. This can be accomplished by using the command `pip install -r requirements.txt`.

With your virtual environment fully set up, you can now run the application with the command `python MindGames\app.py`. Be sure to always activate the virtual environment before running the application.