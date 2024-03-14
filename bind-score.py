# This file reads the log files found in a folder, creates a list to store the lowest values and shows the best binding scores. 
import os
import re

def parse_text_files(folder_path):
    lowest_values = []  # List to store the lowest values and file names
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            # Initialize variables to store data from the section
            values = []
            parsing_section = False
            
            with open(file_path, 'r') as file:
                for line in file:
                    # Check if the line matches the header format
                    if re.match(r"\s*mode\s+\|\s+affinity\s+\|\s+dist from best mode", line):
                        parsing_section = True
                        continue
                    
                    # Check if we're in the section and the line has numeric values
                    if parsing_section and re.match(r"\s*\d+\s+\S+\s+\S+\s+\S+", line):
                        values = line.strip().split()
                        affinity = float(values[1])  # Get the affinity value from the previous column
                        
                        # Append the affinity value and file name to the list
                        lowest_values.append((affinity, filename))
                        
                        # Stop parsing the section if we have n values. Change n to 9 times the amount of log files in your folder.
                        if len(lowest_values) >= n:
                            break
            
            # Sort the list by affinity in ascending order
            lowest_values.sort(key=lambda x: x[0])
            
            # Keep only the top y values. Update y to the amount of values you want the script to show you.
            lowest_values = lowest_values[:y]
    
    return lowest_values

if __name__ == "__main__":
    folder_path = "path/to/log/folder"  # Replace with the path to your folder containing log text files
    lowest_values = parse_text_files(folder_path)
    
    print("Files with the lowest values:")
    for affinity, filename in lowest_values:
        print(f"Filename: {filename}, Affinity: {affinity}")
