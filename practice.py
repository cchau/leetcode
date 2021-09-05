from typing import List, Any


def print_num(x):
    for i in range(x):
        print(i)


def is_odd(x):
    return x % 2 != 0


def print_odd(x):
    for i in range(x):
        if is_odd(i):
            print(i)


def maximum(data):
    max = data[0]
    for a in data:
        if a >= max:
            max = a
    return max


def minimum(data):
    min = data[0]
    for a in data:
        if a <= min:
            min = a
    return min


def find_sum(num, sum):
    for i in range(len(num)):
        b = sum - num[i]
        for j in range(len(num)):
            if num[j] == b:
                return [i, j]


def flip(num):
    a = [0]
    while num != 0:
        a.append(num % 10)
        num = (num // 10)

    result = 0
    while a:
        result = result + a.pop(0) * (10 ** len(a))

    return result


def is_palindrome(num):
    if num < 0:
        return False
    if flip(num) == num:
        return True
    else:
        return False


def morse_encoder(text):
    book = {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            }
    splitter = [c for c in text]
    trans = ''
    for i in splitter:
        trans = trans + book[i.upper()]
    return trans


def morse_decoder(text):
    book = {'.-': 'A',
            '-...': 'B',
            '-.-.': 'C',
            '-..': 'D',
            '.': 'E',
            '..-.': 'F',
            '--.': 'G',
            '....': 'H',
            '..': 'I',
            '.---': 'J',
            '-.-': 'K',
            '.-..': 'L',
            '--': 'M',
            '-.': 'N',
            '---': 'O',
            '.--.': 'P',
            '--.-': 'Q',
            '.-.': 'R',
            '...': 'S',
            '-': 'T',
            '..-': 'U',
            '...-': 'V',
            '.--': 'W',
            '-..-': 'X',
            '-.--': 'Y',
            '--..': 'Z',
            }
    splitter = (text.split())
    trans = ''
    for i in splitter:
        trans = trans + book[i]
    return trans


def roman_decoder(text):
    book = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
    splitter: List[Any] = [c for c in text]
    trans = 0
    i = 0
    while i < len(splitter):
        if book[splitter[i]] < book[splitter[i + 1]]:
            trans = book[splitter[i + 1]] - book[splitter[i]]
            i = i + 2
        else:
            trans = book[splitter[i]]
            i = i + 1

    return trans


fibonacci_cache = {0: 1, 1: 1}


def fibonacci(x):
    if x in fibonacci_cache:
        return fibonacci_cache[x]
    else:
        fibonacci_num = fibonacci(x - 2) + fibonacci(x - 1)
        fibonacci_cache[x] = fibonacci_num
        return fibonacci_num


solution = []


def stair(num, taken):
    if num == 0:
        solution.append(taken)
        return
    elif num == 1:
        solution.append(taken + [1])
        return
    else:
        stair(num - 2, taken + [2])
        stair(num - 1, taken + [1])


def print_stack(arr):
    stack = []
    for i in arr:
        stack.append(i)
    while stack:
        print(stack.pop())


def print_queue(arr):
    stack = []
    for i in arr:
        stack.append(i)
    while stack:
        print(stack.pop(0))


open_brackets = {'(': ')', '{': '}', '[': ']', }
close_brackets = {')': '(', '}': '{', ']': '['}


def check_wellform(arr):
    stack = []
    for c in arr:
        if c in open_brackets:
            stack.append(c)
        elif c in close_brackets:
            close_bracket_for_last_open = open_brackets[stack.pop()]
            if close_bracket_for_last_open != c:
                raise TypeError('Incorrect format')


def permutate_string(data):
    permutations = []
    permutate_helper(data, [], permutations)
    return permutations


def permutate_helper(choice, taken, permutations):
    if len(choice) == 0:
        permutations.append(taken)
        return
    else:
        for i in range(len(choice)):
            new_arr = choice[:i] + choice[i + 1:]
            permutate_helper(new_arr, taken + [choice[i]], permutations)


import random


def num_gen(integer):
    num_list = []
    for i in range(1, integer):
        if i % random.randint(1, 3) == 0:
            num_list.append(i)
            if len(num_list) == integer // 3:
                return num_list
    return num_list


def find_longest_sub_string(string):
    string_list = [c for c in string]
    longest_sub_string = []
    for i in range(len(string_list)):
        taken = set([])
        taken.add(string_list[i])
        sub_string = [string_list[i]]
        for j in range(i + 1, len(string_list)):
            letter = string_list[j]
            if letter not in taken:
                taken.add(letter)
                sub_string.append(letter)
            else:
                if len(sub_string) > len(longest_sub_string):
                    longest_sub_string = []
                    longest_sub_string = longest_sub_string + sub_string
                break
        if len(sub_string) > len(longest_sub_string):
            longest_sub_string = []
            longest_sub_string = longest_sub_string + sub_string

    return len(longest_sub_string), ''.join(longest_sub_string)


def longest_sub_string_sliding_window(string):
    string_list = [c for c in string]
    longest_sub_string = []
    substring = []
    taken = set([])
    for i in range(len(string_list)):
        if string_list[i] not in taken:
            taken.add(string_list[i])
            substring.append(string_list[i])
        elif len(substring) > len(longest_sub_string):
            longest_sub_string = []
            for j in substring:
                longest_sub_string = longest_sub_string + [j]
            substring.pop(0)
            substring.append(string_list[i])
        else:
            substring.pop(0)
            substring.append(string_list[i])
    return len(longest_sub_string), ''.join(longest_sub_string)


def string_to_integer(str):
    string_list = [c for c in str]
    negative_t_or_f = 1
    result = 0
    if ord(string_list[0]) == 45:
        negative_t_or_f = negative_t_or_f * -1
        string_list.pop(0)
    for i in range(len(string_list)):
        value = ord(string_list[i])
        if value - ord('0') > 9:
            raise ValueError
        result = result + (value - ord('0')) * (10 ** (len(string_list) - (i + 1)))
    result = result * negative_t_or_f
    return result


def test(x):
    string_list = [c for c in x]
    longest_sub_string = []
    substring = []
    taken = []
    for i in range(len(string_list)):
        if string_list[i] not in taken:
            taken.append(string_list[i])
            substring.append(string_list[i])
            if len(string_list) - string_list.index(string_list[i]) - 2 == -1 or string_list.index(string_list[i]) == 0:
                if len(substring) > len(longest_sub_string):
                    longest_sub_string = []
                    longest_sub_string = longest_sub_string + substring
        elif len(substring) > len(longest_sub_string):
            longest_sub_string = []
            longest_sub_string = longest_sub_string + substring
            substring.pop(0)
            if string_list[i] in substring:
                substring.remove(string_list[i])
            substring.append(string_list[i])
            taken.pop(0)
        else:
            substring.append(string_list[i])
            substring.pop(0)
    return len(longest_sub_string)

def twoSum(num_list, target):
    addend_list = []
    for i in range(len(num_list)):
        x = int(str(num_list[i]))
        new_num_list = num_list[:i] + num_list[i + 1:]
        for j in range(len(new_num_list)):
            y = int(str(new_num_list[j]))
            if x + y == target and addend_list == []:
                k = num_list.index(y)
                addend_list.append(i)
                addend_list.append(k)
    return addend_list


def twoSum_2(num_list, target):
    addend_list = []
    for i in range(len(num_list)):
        x = int(str(num_list[i]))
        if x + max(num_list) < target:
            z = 0
        else:
            for j in range(len(num_list)):
                y = int(str(num_list[j]))
                if x + y == target and addend_list == [] and j != i:
                    addend_list.append(i)
                    addend_list.append(j)
    return addend_list

def findMedianSortedArray(nums1, nums2=[]):
    merged_array = nums1 + nums2
    merged_array = sorted(merged_array)
    median = 0

    for i in merged_array:
        if len(merged_array) == 2:
            median = float((merged_array[0] + merged_array[1])/2)
            break
        elif len(merged_array) == 1:
            median = float(merged_array[0])
            break
        else:
            merged_array.pop(0)
            merged_array.pop(-1)
    return median

def findMedianSortedArray_2(nums1, nums2=[]):
    merged_array = nums1 + nums2
    merged_array = sorted(merged_array)
    median = 0
    position = len(merged_array) / 2
    middle = int(position)

    if position % 2 == 0 :
        middle = middle - 1
        front = middle + 1
        median = (merged_array[middle] + merged_array[front])/2
    elif position % 2 == 1.5 or position % 2 == 0.5:
        median = merged_array[middle]
    elif position % 2 == 1:
        front = middle - 1
        median = (merged_array[middle] + merged_array[front])/2
    median = float(median)
    return median


def longestPalindrome(s):
    string_list = [c for c in s]
    longest_sub_string = []
    palindrome = ''
    string_is_one_letter = 0

    for i in range(len(string_list)):
        sub_string = [string_list[i]]
        for j in range(i + 1, len(string_list)):
            letter = string_list[j]
            sub_string.append(letter)
            if letter == string_list[i]:
                reversed_list = []
                for s in sub_string:
                    reversed_list = [s] + reversed_list
                if reversed_list == sub_string:
                    if len(sub_string) > len(longest_sub_string):
                        longest_sub_string = []
                        longest_sub_string = longest_sub_string + sub_string

    if len(sub_string) > len(longest_sub_string) and sub_string[0] == sub_string[-1]:
        for i in sub_string:
            palindrome = palindrome + i
    else:
        for i in longest_sub_string:
            palindrome = palindrome + i

    return palindrome


def string_to_int(num_str):
    str_list = [c for c in num_str]
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', ' ']
    symbols_in_string = []
    positive_or_negative = 1
    number = ' '
    for i in range(len(str_list)):
        if str_list[i] == '-':
            positive_or_negative = -1
            if len(number) != 0 and len(symbols_in_string) != 0:
                if str_list[i - 1] != 0:
                    return 0
            symbols_in_string.append(str_list[i])
        elif str_list[i] == '+':
            if positive_or_negative == -1:
                break
            elif len(number) != 0 and len(symbols_in_string) != 0:
                    return 0
            symbols_in_string.append(str_list[i])
        elif str_list[i] in num_list:
            if str_list[i] == ' ' and len(number) != 0:
                if str_list[i+1] in num_list:
                    return 0
            elif str_list[i] != ' ':
                number = number + str_list[i]
        elif str_list[i] not in num_list:
            if len(number) == 0:
                return 0
            elif str_list[i] != str_list[-1]:
                if str_list[i+1] in num_list:
                    return 0

    number = int(number) * positive_or_negative

    if number > 2 ** 31 - 1:
        number = 2 ** 31 - 1
    elif number < -2 ** 31:
        number = -2 ** 31

    return number

def isPalindrome(x):
    num_list = [c for c in str(x)]
    reversed_num = []

    for i in num_list:
        reversed_num = [i] + reversed_num

    if x < 0:
        return 'false'
    elif num_list == reversed_num:
        return 'true'
    else:
        return 'false'

def maxArea(height):
    Area = 0
    Median = 0
    for i in height:
        Median = Median + height[i]

    Median = Median / len(height)

    if height[0] < height[-1]:
        Area = height[0] * (len(height) - 1)
    elif height[0] > height[-1]:
        Area = height[-1] * (len(height) - 1)
    elif height[0] == height[-1]:
        Area = height[-1] * (len(height) - 1)

    if len(height) == 2:
        return Area

    for i in range(len(height)):
        start = height[i]
        if height[i] < Median:
            Area = Area
        else:
            for c in range(i + 1, len(height)):
                end = height[c]
                width = c - i
                length = 0
                if start > end:
                    length = end
                elif end > start:
                    length = start
                elif end == start:
                    length = end

                if length * width > Area:
                    Area = length * width

    return Area