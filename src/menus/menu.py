main_menu = (
            "\n=== Employee Management Menu ===",
            "Show the Employee list", 
            "Add Employee", 
            "Update Employee", 
            "Search Employee",
            "Exit"
             )

add_employee_menu = (
                    "\n=== Add Employee Menu ===",
                    "Add Developer", 
                    "Add Tester", 
                    "Add TeamLeader", 
                    "Exit"
                     )

search_employee_menu = (
    "\n=== Search Employee Menu ===",
    "Search By Name",
    "Search Tester Highest Salary",
    "Search Developer By Language",
    "Exit"
)

def show_menu(menu):
    print(menu[0])
    index_menu = enumerate(menu[1:])
    for key, menu in index_menu:
        print(f"{key}. {menu}")
    return input("Choose the number: ")