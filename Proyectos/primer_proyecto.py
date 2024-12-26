import csv


def read_csv(file_path):
    with open(file_path, mode= 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


