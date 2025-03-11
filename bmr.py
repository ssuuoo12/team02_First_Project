class BMRCalculator: # bmr.py
    def __init__(self, gender, age, weight, height, life_style):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height / 100  # cm를 m로 변환
        self.life_style = float(life_style)
        self.expectation_bmr = self.calculate_bmr()

    def calculate_bmr(self):
        """
        기초대사량(BMR) 계산
        bmr = 447.6 + (9.2 * self.weight) + (3.1 * self.height) - (4.3 * self.age)
        bmr = 88.36 + (13.4 * self.weight) + (4.8 * self.height) - (5.7 * self.age)
        """
       
        if self.gender == 1:
            expectation_bmr = 447.6 + (9.2 * self.weight) + (3.1 * self.height) - (4.3 * self.age) * self.life_style
        elif self.gender == 2:
            expectation_bmr = 88.36 + (13.4 * self.weight) + (4.8 * self.height) - (5.7 * self.age) * self.life_style
        else:
            raise ValueError("올바른 성별을 입력하세요")
        
        
        return round(expectation_bmr * self.life_style, 2)
    
    def get_result(self):
        return {
            "expectation_bmr": round(self.expectation_bmr, 2),
        }
    
     