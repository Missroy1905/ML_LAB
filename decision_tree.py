import csv 
import math 
from collections import counter 
def load_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return headers[:1], data
attributes, dataset = load_csv("play_tennis.csv")
        