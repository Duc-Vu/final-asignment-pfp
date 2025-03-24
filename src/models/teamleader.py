from .developer import Developer

class TeamLeader(Developer):
    def __init__(self, role, empID, empName, baseSal, teamName, progLang, expYear, bonusRate):
        super().__init__(role, empID, empName, baseSal, teamName, progLang, expYear)
        self.__bonus_rate = bonusRate
        
    def get_salary(self) -> float:
        return super().get_salary() + (self.__bonus_rate / 100) * super().get_salary()
    
    def update_information(self, data):
        update_info = super().update_information()
        if update_info is None:
            return None
        
        isTeamHasLeader = any(
        emp_data.get("teamName") == self._team_name and 
        emp_data["role"] == "teamleader" and 
        emp_id != self._empID
        for emp_id, emp_data in data.items()
        )
        
        if isTeamHasLeader:
            print("\nTeam is alreally has Team Leader.")
            return None
        
        try:
            self.__bonus_rate = float(input("Enter New Bonus Rate: "))
        except Exception as e:
            print("\nInvalid Bonus Rate Format.")
            return None
        
        return update_info + (self.__bonus_rate,)
    
    def to_dict(self):
        team_leader_dict = super().to_dict()
        team_leader_dict.update({
            "Bonus Rate": self.__bonus_rate
        })
        return team_leader_dict