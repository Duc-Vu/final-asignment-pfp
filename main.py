import json
from tabulate import tabulate
from src.utils import *
from src.menu import menu

data_file_path = "./database/data.json"

def show_menu(menu: tuple):
    print()
    for key, value in enumerate(menu):
        print(f"{key}. {value}.")
    return input("Choose the number: ")


def load_file():
    try:
        with open(data_file_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        with open(data_file_path, "w") as f:
            data = {}
            json.dump(data, f, indent= 4)

    return data


def save_file(new_data):
    new_data = sort_employee(new_data)
    with open(data_file_path, "w") as f:
        json.dump(new_data, f, indent=4)


def show_employee_list(data, empIDList=None):
    headers = ["empID", "empName", "Role", "baseSal", "Salary", "Team Name", "Programming Languages", "expYear", "Bonus Rate", "Type"]
    key_list = empIDList or data.keys()
    
    row = [[key, data[key].get("empName",""), data[key].get("role",""), data[key].get("baseSal",""), data[key].get("Salary",""),
            data[key].get("teamName", ""), ", ".join(data[key].get("Programming Language","")), data[key].get("expYear",""), data[key].get("Bonus Rate",""),
            data[key].get("Type","") ] for key in key_list]
    
    print(tabulate(row, headers=headers, tablefmt="grid", colalign=["center"]*len(headers) if len(row) > 0 else None, floatfmt=",.0f"))


def add_employee(data):
    while True:
        option = show_menu(menu.add_employee_menu)
        if option in [str(i) for i in range(len(menu.add_employee_menu)-1)]:
            empID = input("Enter Employee ID: ")
            if empID in data:
                print("\nEmployee ID is exist.")
                continue
            
            empName = input("Enter Employee Name: ").lower()
            
            try:
                baseSal = float(input("Enter Employee Base Salary: "))
            except Exception as e:
                print("\nInvalid Base Salary Format.")
                continue
        
        match option:
            case "0":
                try:
                    expYear = int(input("Enter Employee Experience Year: "))
                except Exception as e:
                    print("\nInvalid Experience Year format.")
                    continue
                
                teamName = input("Enter Employee Team Name: ").lower()
                progLang = input("Enter Employee Programming Languages (Programming Languages 1, Programming Languages 2): ").split(",")
                progLang = [char.strip().lower() for char in progLang]
                dev = Developer("developer", empID, empName, baseSal, teamName, progLang, expYear)
                data[empID] = dev.to_dict()
                save_file(data)
                print("\nAdd Developer Successfully")
            case "1":
                try:
                    bonusRate = float(input("Enter Bonus Rate: "))
                except:
                    print("\nInvalid Bonus Rate format.")
                    continue
        
                typee = input("Enter Type Of Tester [Automation Test - AM / Manual Test - MT]: ").lower()
                if typee not in ["am", "mt"]:
                    print("\nType of Tester should AM or MT.")
                    continue
                
                tester = Tester("tester", empID, empName, baseSal, bonusRate, typee)
                data[empID] = tester.to_dict()
                save_file(data)
                print("\nAdd Tester Successfully")
            case "2":
                teamName = input("Enter Employee Team Name: ").lower()
                isTeamHasLeader = False
                for key in data:
                    if data[key].get("teamName") == teamName and data[key]["role"] == "teamleader":
                        isTeamHasLeader = True
                        break
                    
                if isTeamHasLeader:
                    print("\nTeam is alreally has Team Leader.")
                    continue
                
                try:
                    expYear = int(input("Enter Employee Experience Year: "))
                    bonusRate = float(input("Enter Bonus Rate: "))
                except Exception as e:
                    print("\nInvalid Format.")
                    continue
                    
                progLang = input("Enter Employee Programming Languages (Programming Languages 1, Programming Languages 2): ").split(",")
                progLang = [char.strip().lower() for char in progLang]
                teamleader = TeamLeader("teamleader", empID, empName, baseSal, teamName, progLang, expYear, bonusRate)
                data[empID] = teamleader.to_dict()
                save_file(data)
                print("\nAdd Team Leader Successfully")
            case "3":
                break
            case _:
                print("\nError Number.")


def update_employee(data):
    empID = input("Enter Employee ID: ")
    if empID not in data:
        print("\nEmployee does not exist.")
        return None
    role = data[empID]["role"]
    emp_data = data[empID]
    match role:
        case "developer":
            dev = Developer(emp_data["role"], empID, emp_data["empName"], emp_data["baseSal"], emp_data["teamName"], emp_data["Programming Language"], emp_data["expYear"])
            dev_info_update = dev.update_information()
            if dev_info_update is not None:
                data[empID] = dev.to_dict()
                save_file(data)
                print("\nUpdate Information Succesfully")
            else:
                print("\nUpdate Information Failed")
        
        case "tester":
            tester = Tester(emp_data["role"], empID, emp_data["empName"], emp_data["baseSal"], emp_data["Bonus Rate"], emp_data["Type"])
            tester_info_update = tester.update_information()
            if tester_info_update is not None:
                data[empID] = tester.to_dict()
                save_file(data)
                print("\nUpdate Information Succesfully")
            else:
                print("\nUpdate Information Failed")
                
        case "teamleader":
            teamleader = TeamLeader(emp_data["role"], empID, emp_data["empName"], emp_data["baseSal"], emp_data["teamName"], emp_data["Programming Language"], emp_data["expYear"], emp_data["Bonus Rate"])
            teamleader_info_update = teamleader.update_information(data)
            if teamleader_info_update is not None:
                data[empID] = teamleader.to_dict()
                save_file(data)
                print("\nUpdate Information Succesfully")
            else:
                print("\nUpdate Information Failed")
       
         
def search_employee(data):
    while True:
        option = show_menu(menu.search_employee_menu)
        match option:
            case "0":
                empName = input("Enter Employee Name: ").lower()
                empNameList = []
                for key in data:
                    if data[key]["empName"] == empName:
                        empNameList.append(key)
                if empNameList:
                   show_employee_list(data, empNameList)
                else:
                    print("No Employee is matched.")
            case "1":
                tester_list = {}
                for key, value in data.items():
                    if data[key]["role"] == "tester":
                        tester_list[key] = value
                if tester_list:
                    highest_salary = list(sort_employee(tester_list, reverse=True))[0]
                    show_employee_list(data, [highest_salary,])
                else:
                    print("No Employee is matched.")
            case "2":
                dev_list = []
                languague = input("Enter One Programming Language: ").lower()
                for key in data:
                    if data[key]["role"] in ["developer", "teamleader"] and languague in data[key]["Programming Language"]:
                        dev_list.append(key)
                if dev_list:
                    show_employee_list(data, dev_list)
                else:
                    print("No Employee is matched.")
            case "3":
                break
            case _:
                print("\nError Number")


def sort_employee(data, reverse=False):
    return dict(sorted(data.items(), key=lambda x: (x[1]["Salary"], x[1]["empName"]), reverse=reverse))


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