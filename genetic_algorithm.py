import random,csv,os,math
from operator import itemgetter


# Script Variables:
as_is_ratio = (1/3)
hybrid_ratio = (2/3)
mutation_rate = 5 # precentage of soulutions to be mutate
jobs_amount = 10
max_generations = 20
no_imporve_threshold = 5

def get_hybrid_mask_list(jobs_amount=jobs_amount):
    mask_list = []
    for _ in range(jobs_amount):
        mask_list.append(random.choice([0, 1]))
    return mask_list

hybrid_mask = get_hybrid_mask_list() #For example: [1,0,0,0,1,0,0,1,0,1]


# Files and directory:
vectors_initial_data = "data\\vectors_initial_data.csv"
output_path = "data\\output_best_vectors.csv"
jobs_data = "data\\jobs_data.csv"

# Ensures data directory exists
directory = os.path.dirname(vectors_initial_data)
if not os.path.exists(directory):
    os.makedirs(directory)


def get_vector_array_by_id(vector_id, file_name=vectors_initial_data):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        row_id = 1
        for row in reader:
            if row_id == vector_id:
                int_arr = list(map(int, row))
                return int_arr
            row_id += 1
    return []  # Return an empty list if the vector_id is not found

def get_randomize_jobs(jobs_amount=jobs_amount):
    jobs_list = list(range(1, jobs_amount + 1))
    random.shuffle(jobs_list)
    return jobs_list

def export_list(data_list,file_name = vectors_initial_data,clean_csv=False):
        operation = 'a' # append
        if clean_csv: operation = 'w'
        with open(file_name, operation ,newline='') as file:
            writer = csv.writer(file)
            if data_list:
                writer.writerow(data_list)

def set_input_data(fresh_list,random_vectors,clean_list = False):

    if clean_list and fresh_list:
        #clean the exsiting list:
        export_list(data_list= "",clean_csv=True)
        #popuate with fresh list
        for jobs_list in fresh_list:
            export_list(jobs_list)
        return

    if random_vectors:
        for _ in range(random_vectors):
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


def read_csv_to_array(file_path=vectors_initial_data):
    # return array with items such as: {'jobs': [10, 2, 9, 5, 4, 1, 8, 6, 3, 7], 'day_late': 189}
    array_of_dicts = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        vector_id = 1
        for row in csv_reader:
            int_arr = list(map(int, row))
            day_late = get_total_days_late(int_arr)
            array_of_dicts.append({"jobs": [int(job_id) for job_id in row], "day_late": day_late,"vector_id": vector_id})
            vector_id += 1
    return array_of_dicts


def get_ranked_array(array_of_lists):
    ranked_array = []

    # From highest value of day_late to the lowest value
    new_array = sorted(array_of_lists, key=itemgetter('day_late'),reverse=True)

    cur_day_late =new_array[0]["day_late"]
    rank = 1
    for item in new_array:
        if(item["day_late"] != cur_day_late):
            rank += 1
        ranked_array.append({"vector_id": item["vector_id"], "rank": rank})
        cur_day_late = item["day_late"]

    return ranked_array

def get_best_solution(ranked_array):
    vector_id = ranked_array[-1]["vector_id"]
    vector = get_vector_array_by_id(vector_id)
    return {"vector":vector,"days_late":get_total_days_late(vector)}

def get_rank_sum_of__ranked_array(rank_array_of_lists):
    sum = 0
    for item in rank_array_of_lists:
        sum += item["rank"]
    return sum

def get_cum_dist_array(rank_array_of_lists,rank_sum):
    cum_dist_array = []
    low_prob = 0
    high_prob = 0
    for item in rank_array_of_lists:
        high_prob += (item["rank"]/rank_sum)
        cum_dist_array.append({"vector_id": item["vector_id"], "low_prob": low_prob ,"high_prob": high_prob})
        low_prob = high_prob

    return cum_dist_array

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

def get_hybrid_vector(vector0,vector1):
    hybrid_vector = []

    encode0_list = encode_jobs_vector(vector0)
    encode1_list = encode_jobs_vector(vector1)

    for (en0_job, en1_job,current_parent) in zip(encode0_list,encode1_list,hybrid_mask):
        chosen_job_to_append = en0_job
        if current_parent == 1:
            chosen_job_to_append = en1_job

        hybrid_vector.append(chosen_job_to_append)

    return decode_jobs_vector(hybrid_vector)

def get_mutate_list(jobs_list):
    # Generate two distinct random indices
    index1, index2 = random.sample(range(len(jobs_list)), 2)
    # Swap the values at the random indices
    jobs_list[index1], jobs_list[index2] = jobs_list[index2], jobs_list[index1]
    return jobs_list

def get_choosen_vector(cum_distributed_array,only_vector = False):
    random_prob = random.random()
    ran_choosen_item = next(item for item in cum_distributed_array if item["low_prob"] < random_prob< item["high_prob"])
    choosen_vector = get_vector_array_by_id(ran_choosen_item["vector_id"])
    if only_vector:
        return choosen_vector
    return {"vector_id":ran_choosen_item["vector_id"], "vector":choosen_vector}

def test_vector_id_in_list_of_lists(vector_id,array_of_arrays):
    for array in array_of_arrays:
        if get_vector_array_by_id(vector_id) == array : return True
    return False

def get_new_generation(cum_distributed_array,as_is_ratio = as_is_ratio ,hybrid_ratio = hybrid_ratio,mutation_rate = mutation_rate):
    new_gen_array = []
    total_vectors = len(cum_distributed_array)

    as_is_vectors_amount = math.ceil(as_is_ratio * total_vectors)
    hybrid_vectors_amount = math.ceil(hybrid_ratio * total_vectors)

    while( as_is_vectors_amount + hybrid_vectors_amount > total_vectors):
        as_is_vectors_amount -= 1

    mutation_amount = math.ceil(mutation_rate/100 * total_vectors)

    while( as_is_vectors_amount + hybrid_vectors_amount):

        vector_dict = get_choosen_vector(cum_distributed_array)
        vector = vector_dict["vector"]
        if as_is_vectors_amount > 0:
            vector_id = vector_dict["vector_id"]
            # Make sure the choosen one is not already in the new_gen
            exsits = test_vector_id_in_list_of_lists(vector_id,new_gen_array)

            if not exsits:
                new_gen_array.append(vector)
                as_is_vectors_amount -= 1
            continue

        if hybrid_vectors_amount > 0:
            vec0 = vector
            vec1 = get_choosen_vector(cum_distributed_array,True)
            hybrid_vec = get_hybrid_vector(vec0,vec1)
            new_gen_array.append(hybrid_vec)
            hybrid_vectors_amount -= 1
            continue

    # random mutation:
    while mutation_amount > 0:
        ran_vector = random.choice(new_gen_array) #.items()?
        # Mutate the selected random vector
        mutate_vector = get_mutate_list(ran_vector)

        # Update the mutated sublist back to the new_gen_array
        index = new_gen_array.index(ran_vector)
        new_gen_array[index] = mutate_vector

        mutation_amount -= 1
        continue

    return new_gen_array

###
# Gets the user input for the amount of initial vectors to start with:

vectors = int(input("Specify how many job vectors you want to add: "))
if vectors!=0 : set_input_data(fresh_list=[],random_vectors=vectors)

generation_counter = 0
prv_days_late = 100000000000
previos_solution ={'vector': [], 'days_late': prv_days_late}

output_result_data = []
while generation_counter < max_generations:
    main_arr = read_csv_to_array()
    # print(f"Original Array: {main_arr}")

    ranked = get_ranked_array(main_arr)
    # print(f"Ranked Array: {ranked}")

    if generation_counter !=0:
        previos_solution = best_solution
        prv_days_late = best_solution["days_late"]

    best_solution = get_best_solution(ranked)
    if previos_solution != best_solution and prv_days_late >= best_solution["days_late"]:
        print(f"best_solution: {best_solution}")
        output_result_data.append(best_solution["vector"])
    else:
        best_solution = previos_solution


    rank_sum = get_rank_sum_of__ranked_array(ranked)
    # print(f"Rank Sum: {rank_sum}")

    cum_distributed = get_cum_dist_array(ranked,rank_sum)
    # print(f"Cumulative Distributed array: {cum_distributed}")

    new_gen_array = get_new_generation(cum_distributed)
    # print(f"New Generation array: {new_gen_array}")

    set_input_data(fresh_list = new_gen_array,clean_list=True,random_vectors=0)
    generation_counter += 1

for item in output_result_data:
    export_list(item,output_path)