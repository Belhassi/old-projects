class Basketball_Player:
    Num_of_Players = 0
    
    def __init__(self, Hight, Ethnicity, AverageScore):
        self.Hight = Hight
        self.Ethnicity = Ethnicity 
        self.AverageScore = AverageScore

        Basketball_Player.Num_of_Players += 1


Joe = Basketball_Player(201, "Black", 14)
Ahmed = Basketball_Player(190, "White", 15.5)
Mickle = Basketball_Player(154, "White", 17)

print(f"Number of players is : {Basketball_Player.Num_of_Players}")
