# Genetic-Algorithm
<!-- MMN11 | Operations Management 2 | The Open University -->

This repository contains the implementation of a Genetic Algorithm for solving a job scheduling problem with the objective of minimizing delay cost.

The problem involves scheduling a set of jobs on a single machine. The objective is to minimize the total delay cost.
Follow the instructions below to run the Python code and solve the problem.

# Usage
Clone the repository to your local machine or download the script file (genetic_algorithm.py).

Prepare the input data:

Create/clone the csv jobs data file, to data/jobs_data.csv with the job details in a predefined format.
Each line should represent a job and include its relevant information.
The format for each line should be: job_id, process_time, delivery_time.

Example:
```
job_id,process_time,delivery_time
1,2,11
2,4,20
3,5,21
```
Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script using the following command:
```
python genetic_algorithm.py
```
The script will execute the Genetic Algorithm and output the best job schedule found, where the best soultion is at the end od the output.

Adjust the algorithm's variables at the top of the script (if necessary):

Population size: Modify the 'population_size' variable in the script to change the size of the population.
Mutation rate: Adjust the 'mutation_rate' variable to control the rate of mutations in the algorithm.

**Note: Make sure the input file is in the correct format and contains valid job details. The script assumes the input is well-formed and does not perform extensive error checking.**

# Additional Information
The algorithm employs selection, crossover, and mutation operations to evolve the population towards better solutions.
The output includes the best job schedule found.
Feel free to experiment with different input files and algorithm parameters to achieve optimal results.