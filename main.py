import operator
import re

one_letter_dict = {}
two_letter_dict = {}
three_letter_dict = {}
text = ""
with open("Ex1.txt", "r") as f:
    text = f.readline()

two_letter = ""
three_letter = ""
for char in text:
    if char in one_letter_dict:
        pass
    else:
        one_letter_dict[char] = len(re.findall(char, text))

    if len(two_letter) <= 2:
        two_letter += char
    if len(two_letter) == 2:
        if two_letter in two_letter_dict:
            pass
        else:
            two_letter_dict[two_letter] = len(re.findall(two_letter, text))
        two_letter = two_letter[1]

    if len(three_letter) <= 3:
        three_letter += char
    if len(three_letter) == 3:
        if three_letter in three_letter_dict:
            pass
        else:
            three_letter_dict[three_letter] = len(re.findall(three_letter, text))
        three_letter = three_letter[1] + three_letter[2]

letter_dict = sorted(one_letter_dict.items(), key=operator.itemgetter(1), reverse=True)
two_letter_dict = sorted(two_letter_dict.items(), key=operator.itemgetter(1), reverse=True)
three_letter_dict = sorted(three_letter_dict.items(), key=operator.itemgetter(1), reverse=True)
print(letter_dict)
print(two_letter_dict)
print(three_letter_dict)



