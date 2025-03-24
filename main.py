from src.employees_management.employees_management import EmployeeManagement 
from database.loader import *
from src.menus.menu import *
 
def main():
    while True:
        data = load_file()
        option = show_menu(main_menu)
        em = EmployeeManagement(data, file_path)
        match option:
            case "0":
                em.show_employee_list()
            case "1":
                em.add_employee()
            case "2":
                em.update_employee()
            case "3":
                em.search_employee()
            case "4":
                break
            case _:
                print("\nError Number")

if __name__ == "__main__":
    main()