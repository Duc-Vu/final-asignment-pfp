import json
import random
import names

Employee_Numbers = 40

# Danh sách team, vai trò và ngôn ngữ lập trình
teams = ["backend team", "frontend team", "fullstack team", "devops team", 
         "data engineering team", "ai/ml team", "security team"]
roles = ["developer", "tester"]
languages = ["python", "rust", "c++", "java", "go", "javascript", "html", "typescript", 
             "c#", "swift", "kotlin", "sql", "shell/bash", "php", "ruby", "c"]
tester_types = ["am", "mt"]  # Loại của Tester

def calculate_dev_salary(base_sal, exp_year):
    if exp_year >= 5:
        return base_sal + exp_year * 2_000_000
    elif exp_year >= 3:
        return base_sal + exp_year * 1_000_000
    else:
        return base_sal

def calculate_tester_salary(base_sal, bonus_rate):
    return base_sal + (bonus_rate / 100) * base_sal

def calculate_teamleader_salary(dev_salary, bonus_rate):
    return dev_salary + (bonus_rate / 100) * dev_salary

employees = {}
used_teams = set()

# 1️⃣ Chọn trước mỗi team 1 Team Leader
for team in teams:
    emp_id = f"se{19000 + len(employees)}"
    name = names.get_full_name().lower()
    base_salary = random.randint(5_000_000, 50_000_000)
    exp_year = random.randint(1, 10)
    bonus_rate = random.randint(2, 5)
    
    dev_salary = calculate_dev_salary(base_salary, exp_year)
    salary = calculate_teamleader_salary(dev_salary, bonus_rate)

    employees[emp_id] = {
        "role": "teamleader",
        "empName": name,
        "baseSal": float(base_salary),
        "Salary": float(salary),
        "teamName": team,
        "Programming Language": random.sample(languages, random.randint(1, 4)),
        "expYear": exp_year,
        "Bonus Rate": float(bonus_rate)
    }
    used_teams.add(team)

# 2️⃣ Tạo các Developer và Tester còn lại
while len(employees) < Employee_Numbers:
    emp_id = f"se{19000 + len(employees)}"
    role = random.choice(roles)  # Chỉ còn Developer & Tester
    name = names.get_full_name().lower()
    base_salary = random.randint(5_000_000, 50_000_000)
    exp_year = random.randint(1, 10)
    bonus_rate = random.randint(2, 5) if role == "tester" else None

    employee_data = {
        "role": role,
        "empName": name,
        "baseSal": float(base_salary),
    }

    if role == "developer":
        salary = calculate_dev_salary(base_salary, exp_year)
        employee_data.update({
            "teamName": random.choice(teams),
            "Programming Language": random.sample(languages, random.randint(1, 4)),
            "expYear": exp_year,
            "Salary": float(salary)
        })

    elif role == "tester":
        salary = calculate_tester_salary(base_salary, bonus_rate)
        employee_data.update({
            "Bonus Rate": float(bonus_rate),
            "Salary": float(salary),
            "Type": random.choice(tester_types)
        })

    employees[emp_id] = employee_data
employees = dict(sorted(employees.items(), key=lambda x: (x[1]["Salary"], x[1]["empName"]), reverse=False))
# Xuất ra file JSON
with open("database/data.json", "w") as file:
    json.dump(employees, file, indent=4)

print(f"Đã tạo xong {Employee_Numbers} dữ liệu nhân viên và lưu vào database/data.json!")
