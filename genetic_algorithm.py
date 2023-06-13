import random,csv,sys,os

# Script Variables:
mutation_rate = 5 # precentage of soulutions to be mutate
population_size = 100

def get_hybrid_mask_list(jobs_amount=10):
    mask_list = []
    for _ in range(jobs_amount):
        mask_list.append(random.choice([0, 1]))
    return mask_list

hybrid_mask = get_hybrid_mask_list() #For example: [1,0,0,0,1,0,0,1,0,1]


# Files and directory:
vectors_initial_data = "data\\vectors_initial_data.csv"

# Ensures data directory exists
file_path = vectors_initial_data
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Get the command-line arguments
arguments = sys.argv

if(arguments):
    jobs_data = arguments[0]
else:
    jobs_data = "data\\jobs_data.csv"


def get_randomize_jobs(jobs_amount=10):
    jobs_list = list(range(1, jobs_amount + 1))
    random.shuffle(jobs_list)
    return jobs_list

def generate_input_data(vectors=1):

    def export_list(list,file_name = vectors_initial_data):
        with open(file_name,'a' ,newline='') as file:
            writer = csv.writer(file)
            writer.writerow(list)

    for _ in range(vectors):
        jobs_list = get_randomize_jobs()
        export_list(jobs_list)

def read_csv_to_array(file_path=vectors_initial_data):
    array_of_dicts = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            array_of_dicts.append({"jobs": [int(job_id) for job_id in row], "rank": None})
    return array_of_dicts


def get_job_process_time(job_id):
    with open(jobs_data, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['job_id']) == job_id:
                return int(row['process_time'])

    return None  # Return None if job ID is not found

def get_job_delivery_time(job_id):
    with open(jobs_data, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['job_id']) == job_id:
                return int(row['delivery_time'])

    return None  # Return None if job ID is not found

def get_total_days_late(jobs_order_list):
    days_late = 0
    curr_process_time = 0
    for job_id in jobs_order_list:
        process_time = get_job_process_time(job_id)
        delivery_time = get_job_delivery_time(job_id)

        curr_process_time += process_time

        diff = curr_process_time - delivery_time

        if diff > 0: days_late += diff
    return days_late

######################### continue from here ################
def add_rank_to_arrays(arrays):
    ranked_arrays = []

    # for arr_object in arrays:

    return ranked_arrays


def encode_jobs_vector(jobs_list):
    encoded_vector = []

    #First job index spot is for job number 1:
    ind = 1

    for _ in jobs_list:
        cell_encoded_value = 0
        # Inner loop:
        for job_id in jobs_list:
            if(job_id > ind ):
                cell_encoded_value = cell_encoded_value + 1
            elif(job_id == ind):
                break #Inner loop

        encoded_vector.append(cell_encoded_value)
        ind = ind + 1

    return encoded_vector

def decode_jobs_vector(encoded_list):
    decoded_jobs_list = []

    # Starting from the end of the list
    job_id = len(encoded_list)

    for i in reversed(encoded_list):
        decoded_jobs_list.insert(i,job_id)
        job_id = job_id-1

    return decoded_jobs_list

def get_mutate_list(jobs_list):
    # Generate two distinct random indices
    index1, index2 = random.sample(range(len(jobs_list)), 2)
    # Swap the values at the random indices
    jobs_list[index1], jobs_list[index2] = jobs_list[index2], jobs_list[index1]
    return jobs_list

###
# Gets the user input for the amount of initial vectors to start with:

# vectors = int(input("Specify how many job vectors you want to add: "))
# generate_input_data(vectors)

main_arr = read_csv_to_array()
print(f"Before{main_arr}")
# add_rank_to_arrays(main_arr)
# print(f"After{main_arr}")


###

############################## TESTS ##############################
# Example usage - get_total_days_late()

# ranJobs = get_randomize_jobs()
# print(f"Jobs random list: {ranJobs}")

# print(f"Days late: {get_total_days_late(ranJobs)}")

# encoded_list = encode_jobs_vector([2,1,6,4,5,3])
# print(f"Encoded list: {encoded_list}")
## Expect > Encoded list: [1, 0, 3, 1, 1, 0]


# decoded_list = decode_jobs_vector(encoded_list)
# print(f"Decoded list: {decoded_list}")
## Expect > Decoded list: [2, 1, 6, 4, 5, 3]

