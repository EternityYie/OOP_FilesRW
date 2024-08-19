files = ['1.txt', '2.txt', '3.txt']
list_1 = []

for file in files:
    with open(file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        list_1.extend([file, str(len(lines)), lines])

    with open('new.txt', 'w', encoding='UTF-8') as f:
        for lst in list_1:
            f.write(''.join(lst) + '\n')