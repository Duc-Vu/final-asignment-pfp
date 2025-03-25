import json
import os
from ..models import *
from ..menus import menu

class EmployeeManagement():
    def __init__(self, data, file_path):
        self.__data = data
        self.__file_path= file_path
        
        self.save_file()
         
    def save_file(self):
        self.__data = self.sort_employee(self.__data)
        with open(self.__file_path, "w") as f:
            json.dump(self.__data, f, indent=4)

    def show_employee_list(self, empIDList=None):
        
        def get_max_colume_len(all_rows):
            max_len_list = []
            nums_col = len(all_rows[0])
            for col_idx in range(nums_col):
                max_len = max([len(str(row[col_idx])) for row in all_rows])
                max_len_list.append(max_len + 2)

            return max_len_list
            
        
        headers = ["empID", "empName", "Role", "baseSal", "Salary", "Team Name", "Programming Languages", "expYear", "Bonus Rate", "Type"]
        key_list = empIDList or self.__data.keys()
        
        rows = [[
            key.upper(), 
            self.__data[key].get("empName", "").title(), 
            self.__data[key].get("role", "").title(), 
            round(self.__data[key].get("baseSal", "")), 
            round(self.__data[key].get("Salary", "")),
            self.__data[key].get("teamName", "").title(), 
            ", ".join(self.__data[key].get("Programming Language", "")).title(), 
            self.__data[key].get("expYear", ""), 
            self.__data[key].get("Bonus Rate", ""),
            self.__data[key].get("Type", "").upper()
        ]
        for key in key_list
        ]
        rows.insert(0, headers)
        
        max_len_list = get_max_colume_len(rows)
        
        lines_separator = "|" + "+".join(["-" * i for i in max_len_list]) + "|"
        print(lines_separator)
        
        for row in rows:
            for i in range(len(headers)):
                print(f"|{str(row[i]).center(max_len_list[i])}", end="")
            print("|")
            print(lines_separator)

    def update_information_employee(self, role, empID, func="Update"):
        print(f"\n=== {func} Employee's Information ===")
        
        empName = input("Enter Employee Name: ").strip().lower()
        if not empName:
            if func == "Update" and empID in self.__data:
                empName = self.__data[empID].get("empName", "").lower()
            else:
                print("\nEmployee's Name must not be blank.")
                return
        
        try:
            baseSal_input = input("Enter Employee Base Salary: ").strip()
            baseSal = float(baseSal_input) if baseSal_input else float(self.__data.get(empID, {}).get("baseSal", 0))
        except ValueError:
            print("\nInvalid Base Salary Format.")
            return
                  
        if role in ["developer", "teamleader"]:
            try:
                expYear_input = input("Enter Employee Experience Year: ").strip()
                expYear = int(expYear_input) if expYear_input else int(self.__data.get(empID, {}).get("expYear", 0))
            except ValueError:
                print("\nInvalid Experience Year format.")
                return
            teamName = input("Enter Employee Team Name: ").strip().lower() or self.__data.get(empID, {}).get("teamName", "").lower()
            if role == "teamleader":
                if teamName == "":
                    print("\nTeamLeader must have a team")
                    return
                isTeamHasLeader = any(emp["role"] == "teamleader" and emp["teamName"] == teamName and key != empID for key, emp in self.__data.items())
                if isTeamHasLeader:
                    print("\nTeam already has a Team Leader.")
                    return
            progLang_input = input("Enter Employee Programming Languages (comma separated): ")
            progLang = progLang_input.strip().split(",") if progLang_input else self.__data.get(empID, {}).get("Programming Language", [])
            progLang = [char.strip().lower() for char in progLang]
        
        if role in ["tester", "teamleader"]:
            try:
                bonusRate_input = input("Enter Bonus Rate: ").strip()
                bonusRate = float(bonusRate_input) if bonusRate_input else float(self.__data.get(empID, {}).get("Bonus Rate", 0))
            except ValueError:
                print("\nInvalid Bonus Rate format.")
                return
        
        if role == "tester":
            typee = input("Enter Type Of Tester [Automation Test - AM / Manual Test - MT]: ").strip().lower() or self.__data.get(empID, {}).get("Type", "").lower()
            if typee not in ["am", "mt"]:
                print("\nType of Tester should be AM or MT.")
                return
            self.__data[empID] = Tester("tester", empID, empName, baseSal, bonusRate, typee).to_dict()
        
        elif role == "developer":
            self.__data[empID] = Developer("developer", empID, empName, baseSal, teamName, progLang, expYear).to_dict()
        
        elif role == "teamleader":
            self.__data[empID] = TeamLeader("teamleader", empID, empName, baseSal, teamName, progLang, expYear, bonusRate).to_dict()
        
        self.save_file()
        return True

    def add_employee(self):
        while True:
            print("\n=== Add Employee Menu ===")
            option = menu.show_menu(menu.add_employee_menu)
            if option in [str(i) for i in range(len(menu.add_employee_menu)-1)]:
                empID = input("Enter Employee ID: ").lower()
                if empID in self.__data:
                    print("\nEmployee ID is exist.")
                    continue
                elif empID == "":
                    print("\nEmployee ID invalid format")
                    continue
            match option:
                case "0":
                    if self.update_information_employee("developer", empID, "Add"):
                        print("\nAdd Developer Succesfully")
                case "1":
                    if self.update_information_employee("tester", empID, "Add"):
                        print("\nAdd Tester Successfully")
                case "2":
                    if self.update_information_employee("teamleader", empID, "Add"):
                        print("\nAdd Teamleader Successfully")
                case "3":
                    break
                case _:
                    print("\nError Number")
                
    def update_employee(self):
        empID = input("Enter Employee ID: ").lower()
        if empID not in self.__data:
            print("\nEmployee does not exist.")
            return None
        print("\nPress Enter to keep the current value, or type a new one.")
        role = input("Enter new role [Developer/Tester/TeamLeader]: ").lower() or self.__data[empID].get("role")
        if role not in ["developer", "tester", "teamleader"]:
            print("\nInvalid Role")
            return None
                
        if self.update_information_employee(role, empID):
            print(f"\nUpdate Employee {empID.upper()} Successfully")
        
            
    def search_employee(self):
        while True:
            print("\n=== Search Employee Menu ===")
            option = menu.show_menu(menu.search_employee_menu)
            match option:
                case "0":
                    empName = input("Enter Employee Name: ").lower()
                    empNameList = []
                    for key in self.__data:
                        if set(empName.split(" ")).issubset(self.__data[key]["empName"].split(" ")):
                            empNameList.append(key)
                    if empNameList:
                        self.show_employee_list(empNameList)
                    else:
                        print("\nNo Employee is matched")
                case "1":
                    tester_list = {}
                    for key, value in self.__data.items():
                        if self.__data[key]["role"] == "tester":
                            tester_list[key] = value
                    if tester_list:
                        highest_salary = list(self.sort_employee(tester_list, reverse=True))[0]
                        self.show_employee_list([highest_salary,])
                    else:
                        print("\nNo Employee is matched")
                case "2":
                    dev_list = []
                    languague = input("Enter Programming Language (comma separated): ").lower().split(",")
                    languague = [char.strip().lower() for char in languague]
                    for key in self.__data:
                        if self.__data[key]["role"] in ["developer", "teamleader"] and set(languague).issubset(self.__data[key]["Programming Language"]):
                            dev_list.append(key)
                    if dev_list:
                        self.show_employee_list(dev_list)
                    else:
                        print("\nNo Employee is matched")
                case "3":
                    break
                case _:
                    print("\nError Number")
          
          
    def sort_employee(self, data, reverse=False):
        data = dict(sorted(data.items(), key=lambda x: (x[1]["Salary"], x[1]["empName"]), reverse=reverse))
        return data

