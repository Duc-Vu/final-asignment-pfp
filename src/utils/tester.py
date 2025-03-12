from .employee import Employee

class Tester(Employee):
    def __init__(self, role, empID, empName, baseSal, bonusRate, typee):
        super().__init__(role, empID, empName, baseSal)
        self.__bonus_rate = bonusRate
        self.__type = typee
        
    def get_salary(self) -> float:
        return self._baseSal + (self.__bonus_rate / 100) * self._baseSal
    
    def update_information(self):
        update_info = super().update_information()
        if update_info is None:
            return None
        
        try:
            self.__bonus_rate = float(input("Enter New Bonus Rate: "))
        except:
            print("\nInvalid Bonus Rate format.")
            return None
        
        self.__type = input("Enter Type Of Tester: ")
        return update_info + (self.__bonus_rate, self.__type)
    
    def to_dict(self):
        tester_dict = super().to_dict()
        tester_dict.update({
            "Bonus Rate": self.__bonus_rate,
            "Type": self.__type
        })
        return tester_dict