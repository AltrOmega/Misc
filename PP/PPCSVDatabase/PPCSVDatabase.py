import csv
from copy import deepcopy


student_database: dict = {}

def update_student(name:str, surname:str, album_nr:int, dict_db:dict):
    dict_db[album_nr] = [name, surname]

def delete_student(album_nr: int, dict_db:dict):
    del dict_db[album_nr]

def save_dict_to_csv(csv_file_path:str, dict_db:dict):
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for album_nr in dict_db.keys():
            name = dict_db[album_nr][0]
            surname = dict_db[album_nr][1]
            writer.writerow([album_nr, name, surname])

def load_dict_from_csv(csv_file_path: str):
    dict_db = {}

    with open(csv_file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            
            album_nr, name, surname = row
            dict_db[int(album_nr)] = [name, surname]
    return dict_db

def print_dict_as_table(dict_db:dict):
    if len(dict_db.keys()) <= 0:
        print("Baza danych jest pusta")
        return 0

    max_key_length = max(len(str(key)) for key in dict_db.keys())
    max_name_length = max(len(student[0]) for student in dict_db.values())
    max_surname_length = max(len(student[1]) for student in dict_db.values())

    max_key_length = max([max_key_length, 7])
    max_name_length = max([max_name_length, 8])
    max_surname_length = max([max_surname_length, 8])

    header = f"{'Imie'.ljust(max_name_length)} {'Nazwisko'.ljust(max_surname_length)} {'Nr.alb.'.ljust(max_key_length)}"
    print(header)

    for album_nr, student in dict_db.items():
        row = f"{student[0].ljust(max_name_length)} {student[1].ljust(max_surname_length)} {str(album_nr).ljust(max_key_length)}"
        print(row)

if __name__ == "__main__":
    default_csv_file_path = "dict_database.csv"

    while True:
        print("1. Dodaj studenta")
        print("2. Zmień dane studenta")
        print("3. Usuń studenta")
        print("4. Wypisz bazę danych")
        print("5. Zapisz bazę danych do pliku csv")
        print("6. Załaduj bazę danych z pliku csv")
        print("7. Zamnij program bez zapisywania")

        do_ = input("Wykonaj działanie nr: ")

        if do_ == "1":
            name = input("Podaj Imię studenta: ")
            surname = input("Podaj Nazwisko studenta: ")
            album_nr = int(input("Podaj Nr.alb. studenta: "))
            if album_nr in student_database.keys():
                print("\n-----\nStudent z tym numerem albumu już istnienie")
                print("Nic nie zostało zmienione\n-----\n")
            else:
                update_student(name, surname, album_nr, student_database)
                print("\n-----\nDokonano zmiany pomyślnie\n-----\n")

        elif do_ == "2":
            album_nr = int(input("Podaj Nr.alb. studenta którego zmienić: "))
            name = input("Podaj Imię na które je zmienienić imię studenta: ")
            surname = input("Podaj Nazwisko na które je zmienienić nazwisko studenta: ")
            if album_nr in student_database.keys():
                update_student(name, surname, album_nr, student_database)
                print("\n-----\nDokonano zmiany pomyślnie\n-----\n")
            else:
                print("\n-----\nStudent z tym numerem albumu nie istnienie")
                print("Nic nie zostało zmienione\n-----\n")

        elif do_ == "3":
            album_nr = int(input("Podaj Nr.alb. studenta którego usunąć: "))
            if album_nr in student_database.keys():
                delete_student(album_nr, student_database)
                print("\n-----\nDokonano zmiany pomyślnie\n-----\n")
            else:
                print("\n-----\nStudent z tym numerem albumu nie istnienie")
                print("Nic nie zostało zmienione\n-----\n")

        elif do_ == "4":
            print('\n-----')
            print_dict_as_table(student_database)
            print("-----\n")

        elif do_ == "5":
            save_dict_to_csv(default_csv_file_path, student_database)
            print("\n-----\nPomyślnie dokonano zapisu\n-----\n")

        elif do_ == "6":
            student_database = load_dict_from_csv(default_csv_file_path)
            print("\n-----\nPomyślnie dokonano odczytu\n-----\n")
            
        elif do_ == "7":
            break
