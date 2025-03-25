from .employee import Employee

class Developer(Employee):
    def __init__(self, role, empID, empName, baseSal, teamName, progLang, expYear):
        super().__init__(role, empID, empName, baseSal)
        self._team_name = teamName
        self._programming_languages = progLang
        self._exp_year = expYear

    def get_salary(self):
        if self._exp_year >= 5:
            return self._baseSal + self._exp_year * 2000000
        elif self._exp_year >= 3:
            return self._baseSal + self._exp_year * 1000000
        else:
            return self._baseSal
        
    def to_dict(self):
        dev_dict = super().to_dict()
        dev_dict.update({
            "teamName": self._team_name,
            "Programming Language": self._programming_languages,
            "expYear": self._exp_year,
        })
        return dev_dict

    def __str__(self):
        return super().__str__() + f"_{self._team_name}_{self._exp_year}"