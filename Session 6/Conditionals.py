#conditional statements
age = int(input('How old are you?'))
if age >= 21:
    print('Your age is', age)
    print('Your age is ' + str(age)+ '.')
    print('Yes, you can.')
elif age >=6:
    print('Your age is',age)
    print('You are a teenager. No you cannot.')
else:
    print('Your age is', age)
    print('No, not allowed.')
'''
if age >= 6 and age <18:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#nested
x=1
y=2
if x==y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
'''

#BMI
weight= (input('what is your weight?'))
height= (input('what is your height?'))
weight = float(weight)
height = float(height)
BMI = weight/ (height * height)
if BMI <= 18.5:
    print("your bmi is %.1f. You are underweight." % BMI)
elif 18.5 < BMI <= 25:
    print("Your BMI is %.1f. You are normal weight." % BMI)
elif 25 < BMI <= 29.9:
    print("Your BMI is %.1f. You are overweight." % BMI)
else:
    print("your BMI is %.1f. You are obese." % BMI)
        


