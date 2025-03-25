main_menu = (
            "Show the Employee list", 
            "Add Employee", 
            "Update Employee", 
            "Search Employee",
            "Exit"
             )

add_employee_menu = (
                    "Add Developer", 
                    "Add Tester", 
                    "Add TeamLeader", 
                    "Exit"
                     )

search_employee_menu = (
    "Search By Name",
    "Search Tester Highest Salary",
    "Search Developer By Language",
    "Exit"
)

def show_menu(menu):
    index_menu = enumerate(menu)
    for key, menu in index_menu:
        print(f"{key}. {menu}")
    return input("Choose the number: ")