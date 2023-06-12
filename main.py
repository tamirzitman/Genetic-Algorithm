import random,csv

# Files:
vectors_initial_data = "data\\vectors_initial_data.csv"
jobs_data = "data\\jobs_data.csv"

nutation_interval = 2
nutation_counter = 0

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

def get_hybrid_mask_list(jobs_amount=10):
    #output optional example: [1,0,0,0,1,0,0,1,0,1]
    mask_list = []
    for _ in range(jobs_amount):
        mask_list.append(random.choice([0, 1]))
    return mask_list


########################################## Need to rewrite:###########################################################################
def encode_jobs_vector(jobs_list):
    encoded_vector = []

    for i, job in enumerate(jobs_list):
        count = sum(1 for j, prev_job in enumerate(jobs_list[:i]) if prev_job > job)
        encoded_vector.append(count)

    return encoded_vector

# def decode_jobs_vector(encoded_list):

###
# Gets the user input for the amount of initial vectors to start with:

# vectors = int(input("Specify how many job vectors you want to add: "))
# generate_input_data(vectors)
###

############################## TESTS ##############################
# Example usage - get_total_days_late()

ranJobs = get_randomize_jobs()
print(f"Jobs random list: {ranJobs}")

# print(f"Days late: {get_total_days_late(ranJobs)}")

encoded_list = encode_jobs_vector([2,1,6,4,5,3])
print(f"Encoded list: {encoded_list}")

