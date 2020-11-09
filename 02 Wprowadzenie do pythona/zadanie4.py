def funkcja4(temperature_type):
    a = input("Wybierz temperature: 0-Celsjusz 1-Fahrenheit, 2- Rankine, 3-Kelvin")
    a = int(a)
    if a == 0:
        print(temperature_type)
    elif a == 1:
        temperature_type = temperature_type * (9/5 + 32)
        print(temperature_type)
    elif a == 2:
        temperature_type = (temperature_type + 273.15) * 9/5
        print(temperature_type)
    else:
        temperature_type = temperature_type + 273.15
        print(temperature_type)

funkcja4(15)