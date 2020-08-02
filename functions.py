# ScriptName: functions.py
# Author: Louis Sullivan 119363083

# Q1
def to_english(n):
    if sign(n):
        return positive_num(n).capitalize()
    else:
        minus = n * -1
        return "Minus" + " " + positive_num(minus)


def sign(s):
    if s < 0:
        return False
    return True


def positive_num(n):
    modulus_n = n % 10
    int_n = n // 10
    divide_n = n / 10
    n_ten = divide_n % 10
    int_tens = int_n * 10
    hundreds = n // 100
    mod_hundred = n % 100
    modulus_tens = int_n % 10
    big_tens = modulus_tens * 10
    int_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                15: "fifthteen",16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    ten_dict = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
                90: "ninety"}
    if n in int_dict:
        return int_dict[n]
    elif len(str(n)) == 2 and n % 10 == 0:
        return ten_dict[n]
    elif len(str(n)) == 2 and n % 10 != 0:
        return ten_dict[int_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and n % 100 == 0:
        return int_dict[hundreds] + " " + "hundred"
    elif len(str(n)) == 3 and n / 10 == 11:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + int_dict[mod_hundred]
    elif len(str(n)) == 3 and n % 10 == 0 and 11 <= divide_n <= 19:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[mod_hundred]
    elif len(str(n)) == 3 and n % 100 != 0 and n_ten == 0:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and n % 10 == 0:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens]
    elif len(str(n)) == 3 and 21 <= mod_hundred <= 29:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and 31 <= mod_hundred <= 39:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and 41 <= mod_hundred <= 49:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and 51 <= mod_hundred <= 59:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and 61 <= mod_hundred <= 69:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and 71 <= mod_hundred <= 79:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and 81 <= mod_hundred <= 89:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and 91 <= mod_hundred <= 99:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
    elif 11 <= mod_hundred <= 19:
        return int_dict[hundreds] + " " "hundred" + " " + "and" + " " + int_dict[mod_hundred]
    elif 1 <= modulus_n <= 9:
            return int_dict[hundreds] + " " "hundred" + " " + "and" + " " + int_dict[modulus_n]
    elif 1 <= modulus_n <= 9 and n / 10 == 0:
            return int_dict[hundreds] + " " "hundred" + " " + "and" + " " + int_dict[modulus_n]
    elif len(str(n)) == 3 and n % 100 != 0:
        return int_dict[hundreds] + " " + "hundred" + " " + "and" + " " + ten_dict[big_tens] + " " + int_dict[modulus_n]
# Q2
def sort_a_list(s):
    for num in range(len(s) - 1, 0, -1):
        for i in range(num):
            if s[i] > s[i + 1]:
                current_index = s[i]
                s[i] = s[i + 1]
                s[i + 1] = current_index
            elif s[i + 1] == s[i]:
                s.remove(s[i + 1])
    return s


# Q3
def ascii_difference(m, n):
    empty_list = []
    if len(m) == 0:
        for i in range(len(n)):
            ascii_n = ord(str(n[i]))
            empty_list.append(ascii_n)
        return empty_list, empty_list
    elif len(n) == 0:
        for i in range(len(m)):
            ascii_m = ord(str(m[i]))
            empty_list.append(ascii_m)
        return empty_list, empty_list
    elif len(m) > len(n):
        for i in range(len(n)):
            val_m = ord(str(m[i]))
            val_n = ord(str(n[i]))
            add_ascii = val_m + val_n
            empty_list.append(add_ascii)
        for i in range(len(m)-len(n)):
            extra_m = ord(str(m[i]))
            empty_list.append(extra_m)
        return empty_list, big_m_list(m, n)
    elif len(n) > len(m):
        for i in range(len(m)):
            val_m = ord(str(m[i]))
            val_n = ord(str(n[i]))
            add_ascii = val_m + val_n
            empty_list.append(add_ascii)
        for i in range(len(n)-len(m)):
            extra_n = ord(str(n[i]))
            empty_list.append(extra_n)
        return empty_list, big_n_list(m, n)
    else:
        return list1(m, n), list2(m, n)


def list1(x, y):
    ascii_add_list = []
    for i in range(len(x)):
        val_m = ord(str(x[i]))
        val_n = ord(str(y[i]))
        add_ascii = val_m + val_n
        ascii_add_list.append(add_ascii)
    return ascii_add_list


def list2(a, b):
    ascii_take_list = []
    for i in range(len(b)):
        value_m = ord(str(a[i]))
        value_n = ord(str(b[i]))
        if value_m > value_n:
            take_ascii = value_m - value_n
        else:
            take_ascii = value_n - value_m
        ascii_take_list.append(take_ascii)
    return ascii_take_list


def big_m_list(a, b):
    ascii_take_list = []
    for i in range(len(b)):
        value_m = ord(str(a[i]))
        value_n = ord(str(b[i]))
        if value_m > value_n:
            take_ascii = value_m - value_n
        else:
            take_ascii = value_n - value_m
        ascii_take_list.append(take_ascii)
    for i in range(len(a)-len(b)):
        extra_m = ord(str(a[i]))
        ascii_take_list.append(extra_m)
    return ascii_take_list


def big_n_list(a, b):
    ascii_take_list = []
    for i in range(len(a)):
        value_m = ord(str(a[i]))
        value_n = ord(str(b[i]))
        if value_m > value_n:
            take_ascii = value_m - value_n
        else:
            take_ascii = value_n - value_m
        ascii_take_list.append(take_ascii)
    for i in range(len(b)-len(a)):
        extra_n = ord(str(b[i]))
        ascii_take_list.append(extra_n)
    return ascii_take_list