# rzxconvert
Script to Automate the Conversion of .rzx Files to .mp4 Using RetroArch (Fuse Core)

This script automates the process of converting ZX Spectrum .rzx files into .mp4 video files.
It uses RetroArch with the Fuse core to playback the .rzx files and record the output.

Requirements:
- RetroArch installed with the Fuse core
- Python 3.x installed
- RetroArch executable path and core path correctly configured

Usage:
1. Modify the paths for RetroArch, the Fuse core, and the input/output folders.
2. Run the script to automatically process all .rzx files in the specified input folder.
3. The output video files will be saved in the specified output folder.

Options:
- --record for specifying the output file format (e.g., .mp4)
- --video-record-scale to scale the resolution (e.g., 2 for 2x)
- --verbose for verbose output (debugging purposes)

Zip file contains the Python script and a sample Retroarch Config file that has the video output settings preconfigured to the right quality.
