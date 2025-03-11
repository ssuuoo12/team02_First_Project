class BMRCalculator: # bmr.py
    def __init__(self, gender, age, weight, height, life_style):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height / 100  # cm를 m로 변환
        self.life_style = float(life_style)
        self.expectation_bmr = self.calculate_bmr()

     

