from src.utils.utils import *

def main():
    while True:
        option = show_menu(menu.main_menu)
        data = load_file()
        match option:
            case "0":
                show_employee_list(data)
            case "1":
                add_employee(data)
            case "2":
                update_employee(data)
            case "3":
                search_employee(data)
            case "4":
                break
            case _:
                print("\nError Number")


if __name__ == "__main__":
    main()