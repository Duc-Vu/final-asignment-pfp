from .employee import Employee

class Tester(Employee):
    def __init__(self, role, empID, empName, baseSal, bonusRate, typee):
        super().__init__(role, empID, empName, baseSal)
        self.__bonus_rate = bonusRate
        self.__type = typee
        
    def get_salary(self):
        return self._baseSal + (self.__bonus_rate / 100) * self._baseSal
    
    def to_dict(self):
        tester_dict = super().to_dict()
        tester_dict.update({
            "Bonus Rate": self.__bonus_rate,
            "Type": self.__type
        })
        return tester_dict