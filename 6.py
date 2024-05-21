from pickle import FALSE
class PasswordError(Exception):
    pass
class LengthError(PasswordError):
    pass
class LetterError(PasswordError):
    pass
class DigitError(PasswordError):
    pass
class SequenceError(PasswordError):
    pass

def check_password(password):
    try:
        if len(password) < 9:
            return LengthError("Длина пароля меньше 9 символов")

        if password.islower() or password.isupper():
            return LetterError("Пароль должен содержать символы разного регистра.")

        if not any(c.isdigit() for c in password):
            return DigitError("Пароль должен содержать хотя бы одну цифру.")

        prohibited_combinations = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
        for combo in prohibited_combinations:
            if combo in password.lower():
                return SequenceError("Пароль содержит запрещенную последовательность символов.")

        return "ok"
    except AssertionError as e:
        print ("Ошибка: " + e.__class__.__name__)
        return False
    except Exception as e:
        print ("Ошибка: " + e)
        return False

def ctrl_break():
    print("Bye-Bye")
    exit()

while True:
    password = input("Введите пароль: ")
    if password.lower() == "ctrl+break":
          ctrl_break()
    result = check_password(password)
    if result == ("ok"):
        print ("ok")
        break