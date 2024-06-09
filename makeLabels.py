import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

# Read plant names from a file
def read_plant_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        plants = [line.strip() for line in file.readlines()]
    return plants

# Function to run OpenSCAD command
def run_openscad(plant_name):
    output_file = os.path.join(output_dir, f"{plant_name.replace(' ', '')}Label.stl")
    command = ["openscad", "-o", output_file, "-D", f'text="{plant_name}"', "GardenLabel.scad"]
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating {output_file}: {e}")

# Function to open PrusaSlicer with all STL files using Flatpak
def open_prusaslicer(files):
    command = ["flatpak", "run", "com.prusa3d.PrusaSlicer"] + files
    try:
        subprocess.run(command, check=True)
        print("PrusaSlicer opened with all STL files")
    except subprocess.CalledProcessError as e:
        print(f"Error opening PrusaSlicer: {e}")

# Define paths
output_dir = "output"
plant_file = "plants.txt"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read plant names from file
garden_plants = read_plant_names(plant_file)

# Run commands in parallel
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(run_openscad, garden_plants)

# Gather all the generated STL files
stl_files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith('.stl')]

# Open PrusaSlicer with all the generated STL files using Flatpak
open_prusaslicer(stl_files)
