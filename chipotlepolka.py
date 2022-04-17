import csv

#parse csv file
save_list = []

def parse_csv():
    with open () as f:
        for line in f:
            save_list.append(line.strip().split(','))


    return save_list


