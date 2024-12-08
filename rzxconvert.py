"""
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

Author: Paul Tempest
Date: 7 December 2024
"""


import os
import subprocess

# Paths
retroarch_path = r"F:\Launchbox\Emulators\RetroArch\retroarch.exe"  # Path to RetroArch executable
fuse_core_path = r"F:\Launchbox\Emulators\RetroArch\cores\fuse_libretro.dll"  # Path to Fuse core
rzx_folder = r"C:\RZX"  # Folder containing .rzx files
output_folder = r"C:\RZXOutput"  # Folder to save recorded videos

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate through .rzx files and record them
for file_name in os.listdir(rzx_folder):
    if file_name.endswith(".rzx"):
        rzx_path = os.path.join(rzx_folder, file_name)
        video_name = os.path.splitext(file_name)[0] + ".mp4"
        output_path = os.path.join(output_folder, video_name)

        print(f"\nProcessing: {file_name}")
        print(f"RZX Path: {rzx_path}")
        print(f"Output Path: {output_path}")

        # Command for RetroArch recording
        record_command = [
            retroarch_path,
            "-L", fuse_core_path,
            rzx_path,
            "--record", output_path
        ]

        # Print the command for debugging
        print(f"Running Command: {' '.join(record_command)}")

        try:
            subprocess.run(record_command, check=True)
            print(f"Successfully recorded {file_name} to {output_path}")
        except FileNotFoundError:
            print("Error: RetroArch executable or core not found. Check the paths.")
        except subprocess.CalledProcessError as e:
            print(f"Error during recording: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

print("\nAll recordings complete!")
