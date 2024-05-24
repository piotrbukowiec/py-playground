from datetime import datetime


def decode_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return "Nieprawidłowy PESEL"
    year, month, day, gender_digit = int(pesel[:2]), int(pesel[2:4]), int(pesel[4:6]), int(pesel[9])
    year += 2000 if month > 20 else 1900
    month -= 20 if month > 20 else 0
    birth_date = datetime(year, month, day)
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    gender = 'Kobieta' if gender_digit % 2 == 0 else 'Mężczyzna'
    return age, gender


pesel_input = input("Podaj PESEL: ")
age, gender = decode_pesel(pesel_input)
print(f"Wiek: {age}, Płeć: {gender}")
