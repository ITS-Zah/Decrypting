key = {"G": 'e', "L": 'h', "W": 't', "N": 'n', "C": 'a'}

text = ""
with open("Ex1.txt", "r") as f:
    text = f.readline()

text_list = list(text)
for i, char in enumerate(text_list):
    if char in key:
        text_list[i] = key[char]
text = "".join(text_list)
print(text)
