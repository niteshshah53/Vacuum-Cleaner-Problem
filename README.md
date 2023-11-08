
# Vacuum Cleaner Problem
This project involves a cleaning robot that moves through a given map to clean designated areas based on provided instructions. The robot is capable of cleaning empty spaces (' ') on the map and avoids obstacles represented by 'X'.

Installation
Clone the repository using the following command:


git clone https://github.com/your-username/Vacuum-Cleaner-Problem.git
Navigate to the project directory:


cd cleaning-robot
Install the required dependencies using pip:


pip install -r requirements.txt
Usage
Place the input files in the example-problems directory.

Run the main script to process the input files and generate the corresponding output files in the testing directory.

python vaccum_cleaning.py
The script processes the input files in the example-problems directory and writes the output to the testing directory.

Input Files
The input files should follow the naming convention problem_a_00.txt to problem_a_19.txt.
Each input file should contain a map with instructions, representing the cleaning path for the robot.
The map should use the characters 'X' to represent obstacles and ' ' to represent empty spaces.
The starting position of the robot should be marked with 'S' in the map.
Output Files
The script generates output files following the naming convention solution_a_00.txt to solution_c_19.txt.
The output files contain information about the cleaning process, including the spaces left uncleaned or the message "GOOD PLAN" if all areas have been cleaned.
Notes
The robot's movements are based on the instructions provided in the input files.
If the robot encounters an obstacle ('X'), it will remain in its current position.
If the robot reaches the boundary of the map, it will reappear on the opposite side.
Ensure the input files are properly formatted and contain valid instructions for the robot.
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
