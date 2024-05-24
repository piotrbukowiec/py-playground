import datetime

def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit(): return False
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    check_sum = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10
    return check_sum == (10 - int(pesel[-1])) % 10

def get_age_and_gender(pesel):
    if not validate_pesel(pesel): return "Invalid PESEL"
    birth_year = int(pesel[:2])
    birth_month = int(pesel[2:4]) % 20
    birth_day = int(pesel[4:6])
    century = (int(pesel[2:4]) // 20) % 5
    birth_year += [1900, 2000, 2100, 2200, 1800][century]
    today = datetime.date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    gender = "Female" if int(pesel[9]) % 2 == 0 else "Male"
    return f"Age: {age}, Gender: {gender}"

pesel_input = input("Enter PESEL: ")
print(get_age_and_gender(pesel_input))
