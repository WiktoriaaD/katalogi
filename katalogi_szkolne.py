#Zarządzanie Katalogami Roków Studiów

# Program operuje na katalogach w bieżącym katalogu roboczym.
# Funkcje programu:

#     Tworzenie katalogu – użytkownik podaje nazwę (np. "Rok_1").
#     Wyświetlenie listy katalogów.
#     Edycja (zmiana nazwy katalogu).
#     Usunięcie katalogu.
#     Wyjście z programu.
import os
import shutil

def add_directory(name):
    os.makedirs(name)

def show_directory():
    directory=[d for d in os.listdir('.') if
    os.path.isdir(d)]
    print(directory)


def delete_directory(directory):
    if not os.path.exists(directory):
        print("Katalog nie istnieje")
        return
    
    else:
        choice=input("Katalos istnieje. Czy na pewno chcesz usunac? (T/N)")
        if choice=="T":
            shutil.rmtree(directory)
            print(f"Katalog {directory} zostal usuniety.")
        else:
            print("Katalog nie zostal usuniety.")

def rename_directory(directory,new_name):
    if os.path.exists(directory):
        os.rename(directory,new_name)
        print("Nazwa katalogu zostala zmieniona.")
    else:
        print("Katalog nie istnieje.")

if __name__=="__main__":
    while True:
        print("\n1.Dodaj kataolg")
        print("2.Pokaz katalogi")
        print("3.Usun katalog")
        print("4.Zmiana nazwy katalogu")
        print("5.Zakoncz program")
        option=input("Podaj opcje: ")
        if option == "1":
            name=input("Podaj nazwe katalogu: ")
            add_directory(name)
        elif option == "2":
            show_directory()
        elif option=="3":
            directory=input("Podaj nazwe katalogu: ")
            delete_directory(directory)
        elif option=="4":
            directory=input("Podaj nazwe katalogu do zmiany: ")
            new_name=input("Podaj nowa nazwe: ")
            rename_directory(directory,new_name)
        elif option=="5":
            break