# Genetic-Algorithm
<!-- MMN11 | Operations Management 2 | The Open University -->

This repository contains the implementation of a Genetic Algorithm for solving a job scheduling problem with the objective of minimizing delay cost.

Problem Description
The problem involves scheduling a set of jobs on a single machine. The objective is to minimize the total delay cost.
Follow the instructions below to run the Python code and solve the problem.

# Usage 
Clone the repository to your local machine or download the script file (genetic_algorithm.py).

Prepare the input data:

Create a text file (input.txt) with the job details in a predefined format. Each line should represent a job and include its relevant information.
The format for each line should be: job_id, processing_time, due_date, weight.  

Example:
```
Job1, 5, 10, 3
Job2, 3, 8, 2
Job3, 4, 6, 1
```
Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script using the following command:
```
python genetic_algorithm.py input.txt
```
The script will execute the Genetic Algorithm and output the best job schedule found, along with the corresponding delay cost.

Adjust the algorithm's parameters in the script (if necessary):

Population size: Modify the 'population_size' variable in the script to change the size of the population.
Mutation rate: Adjust the 'mutation_rate' variable to control the rate of mutations in the algorithm.

**Note: Make sure the input file is in the correct format and contains valid job details. The script assumes the input is well-formed and does not perform extensive error checking.**

# Additional Information
The script uses a fitness function based on the delay cost to evaluate the quality of each job schedule.
The algorithm employs selection, crossover, and mutation operations to evolve the population towards better solutions.
The output includes the best job schedule found and the corresponding delay cost.
Feel free to experiment with different input files and algorithm parameters to achieve optimal results.
Please let me know if you need any further assistance.





