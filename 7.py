class PhoneFormatException(Exception):
    pass

def check_phone(phone):
    try:
        phone = "".join(phone.split())

        if phone[0] == "+":
          country_code = phone[1:4]
          if country_code not in ["+359", "+55", "+1", "+7"]:
              raise PhoneFormatException("Неверный код страны")
          phone = phone.replace(country_code, " ")
        elif phone.find("+7") != 0 and phone.find("8") != 0:
            raise PhoneFormatException("неверный формат")

        if not all(phone.split("-")):
            raise PhoneFormatException("неверный формат")
        else:
            phone = phone.replace("-", "")
            start_bt = phone.find("(")
            end_bt = phone.find(")")

        if start_bt > -1:
            if end_bt < start_bt or not phone[start_bt + 1:end_bt].isdigit() or not phone.count("(") == 1 or not phone.count(")") == 1:
                raise PhoneFormatException("неверный формат")
        else:
            if end_bt > -1:
                raise PhoneFormatException("неверный формат")

        phone = phone.replace("(", "")
        phone = phone.replace(")", "")

        if phone.find("8") == 0:
            phone = "+7" + phone[1:]

        if not phone[1:].isdigit() or not len(phone[1:]) == 11:
            raise PhoneFormatException("неверное количество цифр")

        operator_code = int(phone[2:5])
        if (910 <= operator_code <= 919 or 980 <= operator_code <= 989):
            return f"МТС: {phone}"
        elif (920 <= operator_code <= 939):
            return f"Мегафон: {phone}"
        elif (902 <= operator_code <= 906 or 960 <= operator_code <= 969):
            return f"Билайн: {phone}"

        return phone
    except (ValueError, IndexError, PhoneFormatException) as e:
        return e

try:
    print(check_phone(input("Введите номер телефона: ")))
except KeyboardInterrupt:
    print("\nПрограмма завершена пользователем.")