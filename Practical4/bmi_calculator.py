#1.iuput weight and height
#2.turn into float and calculate BMI
#3.output BMI
#4.output if underweight, normal weight or obese

a=input("weight in kg:")   #1.iuput weight and height
b=input("height in m:")
BMI=float(a)/(float(b)**2)   #2.turn into float and calculate BMI

print("Your BMI is: ",BMI)    #3.output BMI
if BMI<18.5:                                               #4.output if underweight, normal weight or obese
    print("I'm sorry, but You are Underweight")
elif 18.5<=BMI<30:  
    print("Great! Yoe are Normal weight")
elif 30<=BMI:
    print("I'm sorry, but You are Obese")
