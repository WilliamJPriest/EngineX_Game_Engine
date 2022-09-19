#! /bin/bash

pip install -r requirements.txt
pip install -U pyinstaller
zenity --info --title="Installation complete" --text="Installation complete!" --no-wrap
notify-send "Starting EngineX Hub"
python3 ./hub