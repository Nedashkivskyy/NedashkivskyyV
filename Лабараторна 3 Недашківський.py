height = int(input("Ваш рост"))
weight = int(input("Ваш вес"))
bmi = (weight/height**2)*10000
bmi2 = round(bmi,2)
print('Ваш индекс массы тела:',bmi2)
if bmi2 < 18.5:
    print('Ваш индекс массы тела ниже нормы')
elif bmi2 > 24.9:
    print('Ваш индекс массы тела выше нормы')
else:
    print('Ваш индекс массы тела в норме')
