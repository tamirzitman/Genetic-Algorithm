import os
from utility import (
    set_input_data,
    read_csv_to_array,
    get_ranked_array,
    get_best_solution,
    get_rank_sum_of__ranked_array,
    get_cum_dist_array,
    get_new_generation,
    export_list
)
from constants import constants

# Ensures data directory exists
directory = os.path.dirname(constants["VECTORS_INITIAL_DATA"])
if not os.path.exists(directory):
    os.makedirs(directory)

# Gets the user input for the amount of initial vectors to start with:
vectors = int(input("Specify how many job vectors you want to add: "))
if vectors!=0 : set_input_data(fresh_list=[],random_vectors=vectors)

generation_counter = 0
prv_days_late = constants["HIGH_INT"]
previos_solution ={'vector': [], 'days_late': prv_days_late}

output_result_data = []
while generation_counter < constants["MAX_GENERATIONS"]:
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
    export_list(item,constants["OUTPUT_PATH"])