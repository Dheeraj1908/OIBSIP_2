

"""Dheeraj Naik, Project: BMI Calculator"""


class Bmi():
    
    def __init__(self,wgt,ht):
        self.wgt = wgt
        self.ht = ht

    def Bmi_calc(self,choice):
        self.choice = choice
        if(choice == "cm"):
            cvt = self.ht/100
        elif(choice == "m"):
            return self.wgt/self.ht**2
        else:
            print("input is not valid!")
        return self.wgt/cvt**2
    
    def Catg(self):
        if(bmi<=18.5):
            print("Type: Underweight")
        elif(18.5<bmi<=24.9):
            print("Type: Normal Weight")
        elif(25.0<=bmi<=29.9):
            print("Type: Pre-Obesity")
        elif(30.0<=bmi<=34.9):
            print("Type: Obesity Class-I")
        elif(35.0<=bmi<=39.9):
            print("Type: Obesity Class-II")
        elif(bmi>40):
            print("Type: Obesity Class-III")
            


ps = Bmi(float(input("Enter your weight in kg:")),float(input("Enter your height in m or cm:")))
print("Your Weight:",ps.wgt,"Kg",",","Your Height(m or cm):",ps.ht)

bmi = ps.Bmi_calc(str(input("Which did you mention m or cm:")))
print("Body Mass Index(BMI):",bmi)

ps.Catg()