try:
    num = input("Введіть число:")
    num = int(num)
    print("Ваше число", num)
except ValueError:
    print(" Число неправильне")
