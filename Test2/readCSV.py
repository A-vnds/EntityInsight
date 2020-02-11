import csv
import random
from itertools import zip_longest
import string

p = 0.3
m = 0.3

with open("FirstName.csv", 'r') as file:
    csv_file = csv.reader(file)
    my_list = list(csv_file)

for i in range(len(my_list)):
    my_list[i][1] = int(my_list[i][1])

name_list = []

for i in range(len(my_list)):
    for j in range(0, my_list[i][1]):
        name_list.append(my_list[i][0])

with open("LastName.csv", 'r') as file:
    csv_file = csv.reader(file)
    my_list = list(csv_file)

for i in range(len(my_list)):
    my_list[i][1] = int(my_list[i][1])

lname_list = []

for i in range(len(my_list)):
    for j in range(0, my_list[i][1]):
        lname_list.append(my_list[i][0])

with open("Addresses.csv", 'r') as file:
    csv_file = csv.reader(file)
    my_list = list(csv_file)

for i in range(len(my_list)):
    my_list[i][1] = int(my_list[i][1])

address_list = []

for i in range(len(my_list)):
    for j in range(0, my_list[i][1]):
        address_list.append(my_list[i][0])

address2_list=[]

for address in address_list:
    new_address = []
    words = address.split(' ')
    for word in words:
        outcome = random.random()
        if outcome <= m:
            ix = random.choice(range(len(word)))
            new_word = ''.join([word[w] if w != ix else random.choice(string.ascii_letters) for w in range(len(word))])
            new_address.append(new_word)
        else:
            new_address.append(word)
    new_address = ' '.join([w for w in new_address])
    address2_list.append(new_address)

random.shuffle(name_list)
random.shuffle(lname_list)
random.shuffle(address2_list)

name2_list = []
lname2_list = []

for name in name_list:
    outcome = random.random()
    if outcome <= p:
        ix = random.choice(range(len(name)))
        new_word = ''.join([name[w] if w != ix else random.choice(string.ascii_letters) for w in range(len(name))])
        name2_list.append(new_word)
    else:
        name2_list.append(name)

for name in lname_list:
    outcome = random.random()
    if outcome <= p:
        ix = random.choice(range(len(name)))
        new_word = ''.join([name[w] if w != ix else random.choice(string.ascii_letters) for w in range(len(name))])
        lname2_list.append(new_word)
    else:
        lname2_list.append(name)

with open('finalData.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    data = list(zip_longest(name2_list, lname2_list, address2_list, fillvalue=' '))
    for row in data:
        row = list(row)
        spamwriter.writerow(row)
print("Program completed")

