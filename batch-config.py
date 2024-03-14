#This script reads receptor.pdbqt files found in a folder and creates config files from a template (see config-template.txt).
#On your template file, the word 'template' will be replaced with the filename of the receptor.

import os

def copy_and_rename_template(template_path, new_name):
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    new_file_name = new_name + os.path.splitext(template_path)[1] 
    with open(new_file_name, 'w') as new_file:
        new_file.write(template_content)

    return new_file_name

def replace_arguments_in_file(file_path, old_name, new_name):
    with open(file_path, 'r') as file:
        file_content = file.read()

    new_content = file_content.replace(old_name, new_name)

    with open(file_path, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    template_file_path = "path/to/template.txt" # Write the path where your template.txt is located
    new_files_folder = "path/to/receptor/folders" # Write the path where your receptor files are located 
    output_folder = "path/to/output/folder" # Write the path where you want your config files to be saved

    for new_file in os.listdir(new_files_folder):
        if new_file.endswith(".pdbqt"):
            new_file_path = os.path.join(new_files_folder, new_file)
            new_name = os.path.splitext(new_file)[0]

            copied_file_path = copy_and_rename_template(template_file_path, new_name)
            replace_arguments_in_file(copied_file_path, "template", new_name)

            new_file_path = os.path.join(output_folder, os.path.basename(copied_file_path))
            os.rename(copied_file_path, new_file_path)
