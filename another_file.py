import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def filter_date(start, stop):
    flag = False
    with open("main_filtered_master_access.log", "a") as new_file:
        with open("main_master_access.log", "r") as file:
            for line in file:
                time = line.split("[")[1].split("]")[0].split(" ")[0]
                if time == start:
                    flag = True
                if time == stop:
                    new_file.write(line)
                    return
                if flag == True:
                    new_file.write(line)


def filter_codes(number):
    with open('filtered_errorFree_access.log', 'a') as new_file:
        with open("filtered_access.log", "r") as file:
            for line in file:
                status_code = line.split('"')[2].split(" ")[1]
                if status_code[0] == number:
                    new_file.write(line)


def count_codes():
    parsed_data = []
    with open("filtered_errorFree_access.log", "r") as file:
        i = 0
        codes = {'2': 0, '3': 0, '4': 0, '5': 0}
        for line in file:
            # time = line.split("[")[1].split("]")[0].split(" ")[0]
            status_code = line.split('"')[2].split(" ")[1]
            codes[status_code[0]] += 1
            i += 1
        print(codes)
        print(i)


def filter_dowork():
    parsed_data = []
    with open('filtered_access.log', 'a') as new_file:
        with open("access.log", "r") as file:
            for line in file:
                if "GET /doWork" in line:
                    new_file.write(line)


def check_dowork():
    parsed_data = []
    with open("filtered_master_access.log", "r") as file:
        prev_time = ""
        data = {}
        for line in file:
            if "GET /doWork" not in line:
                print(line)


def get_doWork():
    with open('doWork.txt', 'a') as new_file:
        with open("filtered_master_access.log", "r") as file:
            for line in file:
                doWork = line.split('"')[1].split(' ')[1].split('/')[2]
                new_file.write(doWork+'\n')


def count_hour():
    hours = {}
    with open("main_master_access.log", "r") as file:
        for line in file:
            time = line.split("[")[1].split("]")[0].split(" ")[0].split(":")[1]
            if time not in hours.keys():
                hours[time] = 1
            else:
                hours[time] += 1
    for hour in hours:
        print(f'{hour}: {hours[hour]}')
    sorted_order = sorted(hours.values())
    print(hours)
    print(sorted_order)
    maxHour = list(hours.keys())[list(hours.values()).index(
        sorted_order[len(sorted_order)-1])]
    print(
        f'Max: {maxHour} with {hours[maxHour]} requests.')


def count_load():
    ips = {}
    with open("main_filtered_master_access.log", "r") as file:
        for line in file:
            ip = line.split("-")[0]
            if ip not in ips.keys():
                ips[ip] = 1
            else:
                ips[ip] += 1
        print(ips)



def check_latency():
    with open("histogram.csv", "w") as new_file:
        new_file.write('datetime,latency\n')
        with open("filtered_errorFree_access.log", "r") as file:
            for line in file:
                time = line.split("[")[1].split("]")[0].split(" ")[0]
                fields = line.split(" ")
                # indicates the number of seconds spent processing the call within doWork within gunicorn.
                real_data = fields[len(fields)-3]
                new_file.write(f'{time},{real_data}\n')
                #print(f'{time} {real_data}')
    file.close()
    new_file.close()


def make_graph():
    df = pd.read_csv('histogram.csv')
    df.head(1)
    df['latency'].plot(kind='hist', bins=500,
                       title='Latency', grid=True, xlim=(0, 0.5))
    plt.xlabel('Latency', fontsize=12)
    plt.ylabel('Counts', fontsize=12)

    for array in df.hist(bins=50):
        for subplot in array:
            subplot.set_xlim((-1, 1))

    plt.show()

# Format 19/Nov/2021:00:03:31
# filter_date('22/Nov/2021:04:58:31', '29/Nov/2021:04:57:08')
make_graph()
