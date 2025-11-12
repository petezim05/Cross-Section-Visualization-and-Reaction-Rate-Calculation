# Cross-Section-Visualization-and-Reaction-Rate-Calculation
# NPRE 200 – Computer Project 1
**Author:** Pete Zimmerman  

This project calculates and plots microscopic fission cross sections, flux distributions, reaction rates, and power density for any pair of isotopic JSON files formatted in the ENDF/B-VIII style.

Files must be in .json format

ensure all libraries are up to date
ensure files you wish to imput are stored on the same level as Main.py and ProgramLibrary.py

---
Install Python
Go to https://www.python.org/downloads
 and install Python 3.10 or newer.
On Windows, check the box “Add Python to PATH” during installation.

Download or copy the entire project folder, which should contain:
  Main.py
  ProjectLibrary.py
  requirements.txt
  input files (e.g., U235.json, U238.json, etc.)

Open a terminal (Command Prompt or PowerShell on Windows, Terminal on Mac/Linux)
Use cd to change directory into the folder that contains Main.py.
run: 
  cd path\to\your\project

Install the required Python packages:
numpy
scipy
matplotlib

Run the program
run: 
  python Main.py

Respond to the prompts
 When asked for an isotope file, type its name, for example: U235.json
 Enriched isotope referes to the more fissile Isotope, for Uranium 235 and 238 that would be 235

Check your results
After running, an Output/ folder will appear automatically in the project directory.
It will contain:
  crossSection.png
  flux.png
  reactionRate.png
  powerPerVolume.png
  power_per_vol.txt

If the prompts don’t appear:
  Make sure you are running python Main.py (not ProjectLibrary.py).
  Don’t double-click the file—run it from the terminal instead.
  Ensure you are inside the correct project folder before running the command.


## 📁 Project Structure
