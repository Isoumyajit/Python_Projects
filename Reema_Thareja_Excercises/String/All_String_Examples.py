def patter1():
    """
    : Actual summary
    It will take an input row of 6 and print the respective patterns the row number 
    will depend on the row given by the user
        A
        A B
        A B C
        A B C D
        A B C D E
        A B C D E F
    """
    roe_number = int(input("Enter row numbers :: "))
    character = 'A'
    for i in range(1, roe_number + 1):
        for j in range(0, i):
            print(chr(ord(character) + j), end=' ')
        print()


def split_string(data):
    return data.split()


def redisplay_string(data):
    result = ""
    for letter in data:
        if letter in "aeiouAEIOU":
            pass
        else:
            result += letter

    return result


def find_index(data, char):
    for letter in range(0, len(data)):
        if data[letter] == char:
            return letter
        else:
            pass


def count_char_occur(data, char):
    counter = {char: 0}
    for letter in data:
        if char is letter:
            counter[char] += 1

    return counter[char]


def reverse(data):
    result = ""
    for letter in range(len(data)-1, -1, -1):
        result += data[letter]
    return result


if __name__ == "__main__":
    input_choice = int(input("Enter Your choice ::"))
    if input_choice == 1:
        patter1()
    elif input_choice == 2:
        print(split_string(input("Enter the string :: ")))
    elif input_choice == 3:
        print(redisplay_string(input("Enter String :: ")))
    elif input_choice == 4:
        print(find_index(input("Enter String :: "), input("Enter the character :: ")))
    elif input_choice == 5:
        print(count_char_occur(input("Enter the String ::"), input("Enter the character ::")))
    elif input_choice == 6:
        print(reverse(input("Enter the String ::")))