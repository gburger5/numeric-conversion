dictionary = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    "g": 16,
}


def menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")




def hex_char_decode(digit):
    my_list = list(digit)
    new_list = []
    for c in my_list:
        if c == "x":
            continue
        if c in dictionary:
            new_list.append(dictionary[c])
    new_list.reverse()
    count = 0
    answer = []
    for i in new_list:
        decode = i * 16 ** count
        answer.append(decode)
        count += 1
    sums = sum(answer)
    return sums


def hex_string_decode(hex):
    my_list = list(hex)
    new_list = []
    for c in my_list:
        if c == "x":
            continue
        if c in dictionary:
            new_list.append(dictionary[c])
    new_list.reverse()
    count = 0
    answer = []
    for i in new_list:
        decode = i * 16**count
        answer.append(decode)
        count += 1
    sums = sum(answer)
    return sums



def binary_string_decode(binary):
    bin_list = list(binary)
    new_list_2 = []
    for v in bin_list:
        if v == "b":
            continue
        if v in dictionary or v == 0:
            new_list_2.append(dictionary[v])
    new_list_2.reverse()
    count_2 = 0
    answer_2 = []
    for b in new_list_2:
        decode_2 = b * 2**count_2
        answer_2.append(decode_2)
        count_2 += 1
    sums_2 = sum(answer_2)
    return sums_2


def main():
    test = True
    while test is True:
        menu()
        choice = int(input("Please enter an option:"))
        if choice == 1:
            hex = input("Please enter the numeric string to convert:"+ " ")
            hex_result = hex_string_decode(hex)
            print(f"Result: {hex_result}")
        if choice == 2:
            binary = input("Please enter the numeric string to convert:" + " ")
            bin_result = binary_string_decode(binary)
            print(f"Result: {bin_result}")
        if choice == 4:
            test = False
            print("Goodbye!")


if __name__ == "__main__":
    main()
