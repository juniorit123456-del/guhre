import requests

data = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json").json()

tanlov = int(input("1: UZS -> USD  2: USD -> UZS  3: UZS -> RUB  4: RUB -> UZS: "))

match tanlov:
    case 1:
        summa = float(input("Pulni so'mda kiriting: "))
        for val in data:
            if val["Ccy"] == "USD":
                value = float(val["Rate"])
                print(f"{summa} UZS = {round(summa / value, 3)} USD")
                break

    case 2:
        summa = float(input("Pulni USD da kiriting: "))
        for val in data:
            if val["Ccy"] == "USD":
                value = float(val["Rate"])
                print(f"{summa} USD = {round(summa * value, 3)} UZS")
                break

    case 3:
        summa = float(input("Pulni so'mda kiriting: "))
        for val in data:
            if val["Ccy"] == "RUB":
                value = float(val["Rate"])
                print(f"{summa} UZS = {round(summa / value, 3)} RUB")
                break

    case 4:
        summa = float(input("Pulni RUB da kiriting: "))
        for val in data:
            if val["Ccy"] == "RUB":
                value = float(val["Rate"])
                print(f"{summa} RUB = {round(summa * value, 3)} UZS")
                break