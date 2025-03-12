from .employee import Employee

class Developer(Employee):
    def __init__(self, role, empID, empName, baseSal, teamName, progLang, expYear):
        super().__init__(role, empID, empName, baseSal)
        self._team_name = teamName
        self._programming_languages = progLang
        self._exp_year = expYear

    def get_salary(self) -> float:
        if self._exp_year >= 5:
            return self._baseSal + self._exp_year * 2000000
        elif self._exp_year >= 3:
            return self._baseSal + self._exp_year * 1000000
        else:
            return self._baseSal
        
    def update_information(self):
        update_info = super().update_information()
        if update_info is None:
            return None
        
        try:
            self._exp_year = int(input("Enter New Employee Experience Year: "))
        except Exception as e:
            print("\nInvalid Experience Year format.")
        
        self._programming_languages = input("Enter New Employee Programming Languages (Programming Languages 1, Programming Languages 2): ").split(",")
        self._programming_languages = [char.strip().lower() for char in self._programming_languages]
        self._team_name = input("Enter New Employee Team Name: ").lower()
        return update_info + (self._team_name, self._programming_languages, self._exp_year)
        
    def to_dict(self):
        dev_dict = super().to_dict()
        dev_dict.update({
            "teamName": self._team_name,
            "Programming Language": self._programming_languages,
            "expYear": self._exp_year,
        })
        return dev_dict

    def __str__(self) -> str:
        return super().__str__() + f"_{self._team_name}_{self._exp_year}"