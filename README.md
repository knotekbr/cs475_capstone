# CS475 Senior Project - MindGames
Brandon Knotek, Walid Muhammad, and Jack Wilder
Repository available at: https://github.com/knotekbr/cs475_capstone

## Introduction
This repository contains the code and documentation for our senior research project, which we're calling MindGames. The goal of the project is to explore the viability of neurofeedback as a means for controlling real-time interactive experiences. Such a system would allow individuals with physical disabilities to interact with those experiences in a way that is often impossible using traditional physical control schemes.

To accomplish our goal, we developed a simple Pac-Man clone using JavaScript, HTML, and CSS. The game is supported by a Flask backend and an EEG processing pipeline that was built using NeuroPype Pipeline Designer. EEG data is collected using an OpenBCI Cyton biosensing board mounted to an OpenBCI Ultracortex headset. As the data is collected, it is fed to the processing pipeline where it is filtered and classified into game commands. Those commands are then sent to the game via the backend using Flask's flask-sock extension and JavaScript's built-in WebSocket API. With this setup, users are able to control the game simply by thinking commands, eliminating the need for keyboard interaction.

## Directory Structure
- `\EEG_Pipelines` - EEG processing pipeline variants
- `\EEG_Recordings` - EEG data that was recorded during training sessions
- `\Images` - Images that were produced while working on the project
    - `\Diagrams` - Diagrams of various system components
    - `\Screenshots` - Screenshots of system components in action
- `\MindGames` - MindGames application directory
    - `\static` - Static resources used by the Pac-Man frontend
        - `\css` - Frontend style sheets
        - `\img` - Frontend images
        - `\js` - Frontend JavaScript
            - `\entities` - JavaScript classes related to game entities
    - `\templates` - Frontend webpages
- `\Presentations` - Project presentations that were given during and after development

## Setup
### Additional Software
- FTDI Virtual VCP driver (required for EEG integration)
    - Enables serial data input from OpenBCI RFDuino USB dongle
    - Available at https://ftdichip.com/drivers/vcp-drivers/
- OpenBCI_LSL (required for EEG integration)
    - Creates an LSL broadcast of raw EEG data from the OpenBCI Cyton biosensing board
    - Available at https://github.com/openbci-archive/OpenBCI_LSL
- NeuroPype Suite (required for EEG integration)
    - Includes NeuroPype Pipeline Designer, which is required to open and run the EEG processing pipeline
    - Available at https://www.neuropype.io/ (license required, free for academic use)
- LabRecorder (recommended)
    - Used to record EEG/marker data during training sessions
    - Available at https://github.com/labstreaminglayer/App-LabRecorder/releases
- OpenBCI GUI (optional)
    - Provides a GUI for visualizing raw EEG data output from OpenBCI hardware
    - Available at https://openbci.com/downloads

### Hardware
The hardware listed here reflects what was used during the development of this project, and the setup instructions are written with respect to it. Other hardware options are available, but may require configuration changes and additional software downloads. However, some sort of EEG hardware is required for EEG integration.

- OpenBCI DIY Neurotechnologist's 8-Channel Starter Kit
    - Includes Cyton Biosensing Board, RFDuino USB dongle, Ultracortex Mark IV headset, and EEG electrodes
    - All-in-one package for recording EEG data and broadcasting it to a computer for processing
    - Available at https://shop.openbci.com/products/d-i-y-neurotechnologists-starter-kit

### Virtual Environment
MindGames was built using a Python virtual environment (VE). To run the application on your local machine, it is necessary to first establish a copy of this environment. To accomplish this, first open a terminal instance in the root directory, `\cs475_capstone`. Run the command `python -m venv env`. This creates a subdirectory, `\cs475_capstone\env`, which contains the virtual environment. Note that the root directory contains a `.gitignore` file that tells Git to ignore this subdirectory.

With the VE in place, it must be activated. In Windows PowerShell, this can be accomplished by using the command `env\Scripts\Activate.ps1`. The input line of the terminal should now indicate that the VE has been activated. If this is the first time you've activated the VE (or if new Python packages have been added as dependencies), you must install any package dependencies before running the application. This can be accomplished by using the command `pip install -r requirements.txt`.

Make sure that the VE is activated in any terminal instances before following the remaining setup instructions.

### EEG Integration
#### Hardware Setup
Power on the Cyton board and wait a few seconds while it initializes. Next plug the RFDuino USB dongle into your computer, ensuring that the black switch on the side is in the position closest to the computer.

#### OpenBCI LSL Streaming
With the hardware setup completed and OpenBCI_LSL downloaded, open a terminal instance in the `\OpenBCI_LSL` subdirectory and run the command `python openbci_lsl.py --stream`. Once the stream is intitialized and the console prompts you for more input, enter the command `/loc FC5,FC1,CP5,CP1,CP2,CP6,FC2,FC6` to tell the streaming module the locations of the electrodes. These location names are taken from a modified version of the international 10-20 system known as the 10-10 system. Finally, to begin broadcasting raw EEG data, use the command `/start`. This terminal instance can be minimized, but must remain open.

#### Recording Training Data
Once the EEG LSL broadcast has started, open a second terminal instance in the `\MindGames` subdirectory. Start the training module by running the command `python training2.py`, but do not press Enter to start training.

Open LabRecorder by running the executable that was included in the download. Under "Record from Streams", ensure that "openbci_eeg" and "openbci_markers" are selected ("openbci_aux" does not need to be selected). Select a Study Root (the directory where the recording will be saved), and enter a file name for the recording by unchecking the BIDS box. When you're ready to start training, click the Start button.

Return to the terminal instance where you started the training module, and press Enter to start the training session. After a few seconds, the training module will begin instructing you to complete movements. Follow the module's instructions until training is complete, then return to LabRecorder and click the Stop button.

#### Pipeline Configuration
First, ensure that the NeuroPype server is online by running the `NeuroPype (Academic)` application that is included in the NeuroPype suite. Then run the accompanying `Pipeline Designer (Academic)` application. When prompted, open the pipeline located at `\EEG_Pipelines\MotorImageryTest4.pyp`. Double click the "Import XDF" node at the top left of the pipeline and set "Filename" to the path of the training data file that you recorded. Close the node settings popup and click the blue Pause button at the bottom left of Pipeline Designer to begin pipeline execution. Allow the pipeline to configure itself using the training data you provided.

### Running the Application
With a terminal instance open in the `\MindGames` subdirectory, run the command `python app.py` to initalize the Flask backend. If you have completed the EEG integration setup, the backend will automatically begin receiving commands from the processing pipeline. The application can be run without any EEG integration, in which case it will just function as a normal game of Pac-Man.

Open a browser and navigate to `localhost:5000` or the IP address that was provided by Flask during initialization. You should now be able to play Pac-Man by clicking the Start Game button. The four arrows at the top left of the UI light up to indicate the most recent directional input received (either from the keyboard or from the processing pipeline). Demo Mode can be activated to disable contact damage with the ghost, which is useful when trying to get a feel for moving Pac-Man using EEG integration.