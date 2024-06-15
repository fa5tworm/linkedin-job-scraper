

The LinkedIn Job Scraper is a powerful tool for extracting job information from LinkedIn. To make it more user-friendly, we can create a GUI executable that can be run on a Linux system. This guide will walk you through the steps to create an executable GUI for the LinkedIn scraper using Git Clone and PyInstaller.

**Creating an Executable GUI for LinkedIn Scraper on Linux**


**Prerequisites**

* Ensure Python and pip are installed on your system.
* Install Git if you haven't already: `sudo apt-get install git` (for Ubuntu-based systems) or `sudo yum install git` (for RPM-based systems).

**Step 1: Clone the Repository**

* Open a terminal and run: `git clone https://github.com/fa5tworm/linkedin-job-scraper.git`
* Navigate to the cloned repository: `cd linkedin-job-scraper`

**Step 2: Install Required Packages**

* Install the required packages using pip: `pip install tkinter pandas requests beautifulsoup4 geonamescache`

**Step 3: Freeze the Script using PyInstaller**

* Install PyInstaller: `pip install pyinstaller pyinstaller-hooks-contrib`
* Freeze the script using PyInstaller: `pyinstaller --onefile --windowed linkedin.py`
This will create a `dist` folder containing the executable file.

**Step 4: Run the Executable**

* Navigate to the `dist` folder and run the executable file: `cd dist` and then `./linkedin`
The GUI should now appear, and you can interact with it to extract LinkedIn job info.

**Tips and Variations**

* **Add an Icon to Your Executable**: Use the `--icon` option with PyInstaller: `pyinstaller --onefile --windowed --icon=icon.ico linkedin.py`
* **Create a Standalone Executable**: Use the `--bundle` option: `pyinstaller --onefile --windowed --bundle linkedin.py`
* **Create a 32-bit Executable on a 64-bit System**: Use the `--platform` option: `pyinstaller --onefile --windowed --platform=linux32 linkedin.py`
Remember to adjust the script and PyInstaller options according to your specific needs.

Note: Make sure to replace `linkedin.py` with the actual script file name if it's different.