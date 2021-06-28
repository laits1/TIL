weight = eval(input("몸무게(킬로그램) : "))
height = eval(input("키(미터) : "))
BMI = weight / height ** 2
print("당신의 BMI : %.2f" %BMI)

print("당신의 BMI :", format(BMI, '.2f'))