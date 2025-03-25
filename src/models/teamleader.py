from .developer import Developer

class TeamLeader(Developer):
    def __init__(self, role, empID, empName, baseSal, teamName, progLang, expYear, bonusRate):
        super().__init__(role, empID, empName, baseSal, teamName, progLang, expYear)
        self.__bonus_rate = bonusRate
        
    def get_salary(self):
        return super().get_salary() + (self.__bonus_rate / 100) * super().get_salary()
    
    def to_dict(self):
        team_leader_dict = super().to_dict()
        team_leader_dict.update({
            "Bonus Rate": self.__bonus_rate
        })
        return team_leader_dict