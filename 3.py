RomanNumbers = {'M': 1000, 'CM': 900, 'D': 500,
'CD': 400, 'C': 100, 'XC': 90,
'L': 50, 'XL': 40, 'X': 10,
'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

one = 5
two = 4
three = 0

def int_to_roman(num):
    roman = ''
    for symbol, value in RomanNumbers.items():
        while num >= value:
            roman += symbol
            num -= value
    return roman

def roman():
    global three
    three = one + two
    roman_one = int_to_roman(one)
    roman_two = int_to_roman(two)
    roman_three = int_to_roman(three)

    print(f"{roman_one} + {roman_two} = {roman_three}")

roman()