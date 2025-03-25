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
            self.__data[key].get("baseSal", ""), 
            self.__data[key].get("Salary", ""),
            self.__data[key].get("teamName", "").title(), 
            ", ".join(self.__data[key].get("Programming Language", "")).title(), 
            self.__data[key].get("expYear", ""), 
            self.__data[key].get("Bonus Rate", ""),
            self.__data[key].get("Type", "").upper()
        ]
        for key in key_list
        ]
        rows.insert(0, headers)
        
        nums_col = len(headers)
        max_len_list = get_max_colume_len(rows)
        total_table_with = sum(max_len_list) + nums_col - 1
        print("|" + "-" * total_table_with + "|")
        for row in rows:
            for i in range(nums_col):
                print(f"|{str(row[i]).center(max_len_list[i])}", end="")
            print("|")
            print("|" + "-" * total_table_with + "|")

    def update_information_employee(self, role, empID):
        print("\n=== Update or Add Employee Information ===")
        empName = input("Enter Employee Name: ").lower()
                
        try:
            baseSal = float(input("Enter Employee Base Salary: "))
        except Exception as e:
            print("\nInvalid Base Salary Format.")
            return None
        match role:
            case "developer":
                try:
                    expYear = int(input("Enter Employee Experience Year: "))
                except Exception as e:
                    print("\nInvalid Experience Year format.")
                    return None
                
                teamName = input("Enter Employee Team Name: ").lower()
                progLang = input("Enter Employee Programming Languages (Programming Languages 1, Programming Languages 2): ").split(",")
                progLang = [char.strip().lower() for char in progLang]
                dev = Developer("developer", empID, empName, baseSal, teamName, progLang, expYear)
                self.__data[empID] = dev.to_dict()
                self.save_file()
                return True
            case "tester":
                try:
                    bonusRate = float(input("Enter Bonus Rate: "))
                except:
                    print("\nInvalid Bonus Rate format.")
                    return None
        
                typee = input("Enter Type Of Tester [Automation Test - AM / Manual Test - MT]: ").lower()
                if typee not in ["am", "mt"]:
                    print("\nType of Tester should AM or MT.")
                    return None
                
                tester = Tester("tester", empID, empName, baseSal, bonusRate, typee)
                self.__data[empID] = tester.to_dict()
                self.save_file()
                return True
            case "teamleader":
                teamName = input("Enter Employee Team Name: ").lower()
                isTeamHasLeader = False
                for key in self.__data:
                    if self.__data[key].get("teamName") == teamName and self.__data[key]["role"] == "teamleader":
                        isTeamHasLeader = True
                        break
                    
                if isTeamHasLeader:
                    print("\nTeam is alreally has Team Leader.")
                    return None
                
                try:
                    expYear = int(input("Enter Employee Experience Year: "))
                    bonusRate = float(input("Enter Bonus Rate: "))
                except Exception as e:
                    print("\nInvalid Format.")
                    return None
                    
                progLang = input("Enter Employee Programming Languages (Programming Languages 1, Programming Languages 2): ").split(",")
                progLang = [char.strip().lower() for char in progLang]
                teamleader = TeamLeader("teamleader", empID, empName, baseSal, teamName, progLang, expYear, bonusRate)
                self.__data[empID] = teamleader.to_dict()
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
            match option:
                case "0":
                    if self.update_information_employee("developer", empID):
                        print("Add Developer Succesfully")
                case "1":
                    if self.update_information_employee("tester", empID):
                        print("Add Tester Successfully")
                case "2":
                    if self.update_information_employee("teamleader", empID):
                        print("Add Teamleader Successfully")
                case "3":
                    break
                case _:
                    print("\nError Number")
                
    def update_employee(self):
        empID = input("Enter Employee ID: ").lower()
        if empID not in self.__data:
            print("\nEmployee does not exist.")
            return None
        print("\n=== Update New Employee's Information ===")
        role = input("Enter new role [Developer/Tester/TeamLeader]: ").lower()
        if role not in ["developer", "tester", "teamleader"]:
            print("Invalid Role")
            return None
                
        if self.update_information_employee(role, empID):
            print(f"Update Employee {empID.upper()} Successfully")
        
            
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
                        print("\nNo Employee is matched.")
                case "1":
                    tester_list = {}
                    for key, value in self.__data.items():
                        if self.__data[key]["role"] == "tester":
                            tester_list[key] = value
                    if tester_list:
                        highest_salary = list(self.sort_employee(tester_list, reverse=True))[0]
                        self.show_employee_list([highest_salary,])
                    else:
                        print("\nNo Employee is matched.")
                case "2":
                    dev_list = []
                    languague = input("Enter Programming Language: ").lower().split(",")
                    languague = [char.strip().lower() for char in languague]
                    for key in self.__data:
                        if self.__data[key]["role"] in ["developer", "teamleader"] and set(languague).issubset(self.__data[key]["Programming Language"]):
                            dev_list.append(key)
                    if dev_list:
                        self.show_employee_list(dev_list)
                    else:
                        print("\nNo Employee is matched.")
                case "3":
                    break
                case _:
                    print("\nError Number")
                    

    def sort_employee(self, data, reverse=False):
        data = dict(sorted(data.items(), key=lambda x: (x[1]["Salary"], x[1]["empName"]), reverse=reverse))
        return data

