# This script calls vina.exe to run the molecular docking assay based on the instructions given on the config files given in
# a folder.

import os
import subprocess

def run_vina_with_config(vina_executable, config_file):
    # Define command to run AutoDock Vina with the specified config file
    command = [vina_executable, '--config', config_file]
    
    # Run AutoDock Vina
    subprocess.run(command)

if __name__ == "__main__":
    vina_executable = "C:/Program Files (x86)/The Scripps Research Institute/Vina/vina.exe"  # Adjust to the correct path if necessary
    config_folder = "path/to/config/folder" # Your config folder must not contain other types of .txt files or it will result in failure.

    # Iterate through configuration files in the specified folder
    for config_file in os.listdir(config_folder):
        if config_file.endswith(".txt"):
            config_file_path = os.path.join(config_folder, config_file)
            
            # Run AutoDock Vina for each configuration file
            run_vina_with_config(vina_executable, config_file_path)
