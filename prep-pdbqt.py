#The following code calls the prepare_receptor4.py function from Autodock Tools for all receptor files in pdb format 
#found within a folder.

import os
import subprocess

def prepare_receptor_pdbqt(input_folder, output_folder):
    for pdb_file in os.listdir(input_folder):
        if pdb_file.endswith(".pdb"):
            pdb_path = os.path.join(input_folder, pdb_file)
            # Prepare receptor PDBQT file
            output_pdbqt_path = os.path.join(output_folder, os.path.splitext(pdb_file)[0] + ".pdbqt")
            prepare_receptor_pdbqt_command = [
                "C:/Program Files (x86)/MGLTools-1.5.7/python.exe",  # If your MGLTools/python.exe is found on another location, update the paath
                "C:/Program Files (x86)/MGLTools-1.5.7/Lib/site-packages/AutodockTools/Utilities24/prepare_receptor4.py",  # Same as above
                "-r", pdb_path,
                "-o", output_pdbqt_path,
            ]
            subprocess.call(prepare_receptor_pdbqt_command)

if __name__ == "__main__":
    input_folder = "Path/to/input/Folder"  # Replace with the path to your input folder containing PDB files
    output_folder = "Path/to/output/Folder"  # Replace with the path to your output folder 
    prepare_receptor_pdbqt(input_folder, output_folder)
