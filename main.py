import random,csv

def generate_input_data():
    input_data_file_name = "data\\input.csv"

    def get_randomize_jobs(jobs_amount = 6):
        jobs_list = list(range(1, jobs_amount + 1))
        random.shuffle(jobs_list)
        return jobs_list

    def export_list(list,file_name = input_data_file_name):
        with open(file_name,'a' ,newline='') as f:
            writer = csv.writer(f)
            writer.writerow(list)

    jobs_list = get_randomize_jobs()
    export_list(jobs_list)

generate_input_data()