five_letters = []

with open('Advanced Python\Wordle\slovar.py', 'r', encoding='utf-8') as file: 
    data = file.readlines()
    for i in data:
        i = i.replace('\n', '')
        if len(i) == 5:
            five_letters.append(i.upper())






