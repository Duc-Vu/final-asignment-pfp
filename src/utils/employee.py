from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, role, empID, empName, baseSal):
        self._role = role
        self._empID = empID
        self._empName = empName
        self._baseSal = baseSal

    @abstractmethod
    def get_salary(self):
        pass
    
    @abstractmethod
    def update_information(self):
        self._empName = input("Enter New Employee Name: ").lower()
        try:
            self._baseSal = float(input("Enter New Employee Base Salary: "))
        except Exception as e:
            print("\nInvalid Base Salary Format.")
            return None
        
        self._role = input("Enter New Role [Developer/Tester/TeamLeader]: ").lower()
        if self._role not in ["developer", "tester", "teamleader"]:
            print("\nInvalid Role")
            return None
        
        return (self._empName, self._baseSal, self._role)
    
    @abstractmethod
    def to_dict(self):
        return {"role": self._role,
                "empName": self._empName,
                "baseSal": self._baseSal,
                "Salary": self.get_salary()}

    def __str__(self) -> str:
        return f"{self._empID}_{self._empName}_{self._baseSal}"