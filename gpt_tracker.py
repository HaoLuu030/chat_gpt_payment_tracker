import csv
import os

file_name = "gpt_tracker.csv"
COLS = ['name', 'month', 'year', 'paid']


def create_new_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=COLS)
        writer.writeheader()

def ensure_file_exist(file_name):
    if (not os.path.isfile(file_name)):
        create_new_file(file_name)

def read_n_lines(file_name, num_of_lines):
    ensure_file_exist(file_name)
    with open(file_name, 'r', newline="") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if i > num_of_lines - 1:
                break
            print(row)
    
def add_entry(file_name, num_of_lines=1):
    ensure_file_exist(file_name)
    with open(file_name, 'a', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COLS)
        for _ in range(num_of_lines):
            name = input("Enter name: ").strip()
            month = input("Enter month: ").strip()
            year = input("Enter year: ").strip()
            paid = input("Did they pay? ").strip()
            entry = {
                "name": name,
                "month": month,
                "year": year,
                "paid": paid
            }
            writer.writerow(entry)
            print(f"{name}, {month}, {year}, {paid} added")

def read_by_category(file_name):
    if (not os.path.isfile(file_name)):
        create_new_file(file_name)
    category = input("'n' = name, 'm' = month, 'y' = year, 'p' = paid: ")
    categories = {
        'n': "name",
        'm': "month",
        'y': "year",
        'p': "paid"
    }
    if category not in categories:
        print("Invalid category")
        return
    column = categories[category]
    value = input(f"Enter {column}: ")
    found = False
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row[column] == value:
                print(row)
                found = True
    if (not found):
        print("No entry found")


def main() -> None:
    while True:
        print("\nChat GPT tracker")
        print("a - Add entries")
        print("r - Read entries")
        print("c - Search by category")
        print("q - Quit")
        mode = input("Choose an option: ").strip()
        if (str.lower(mode) == 'a'):
            num_of_lines = int(input("How many lines: "))
            add_entry(file_name, num_of_lines)
        elif (str.lower(mode) == 'r'):
            num_of_lines = int(input("How many lines: ")) 
            read_n_lines(file_name, num_of_lines)
        elif (str.lower(mode) == 'c'):
            read_by_category(file_name)
        elif (str.lower(mode) == 'q'):
            print("So far...")
            break
        else:
            print("Invalid Option")


main()