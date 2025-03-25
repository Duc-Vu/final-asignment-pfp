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
    def to_dict(self):
        return {"role": self._role,
                "empName": self._empName,
                "baseSal": self._baseSal,
                "Salary": self.get_salary()}

    def __str__(self) -> str:
        return f"{self._empID}_{self._empName}_{self._baseSal}"