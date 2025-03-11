a=input("weight in kg:")
b=input("height in m:")
BMI=float(a)/(float(b)**2)

print("Your BMI is: ",BMI)
if BMI<18.5:
    print("I'm sorry, but You are Underweight")
elif 18.5<=BMI<25:  
    print("Great! Yoe are Normal weight")
elif 25<=BMI<30:
    print("I'm sorry, but You are Obese")