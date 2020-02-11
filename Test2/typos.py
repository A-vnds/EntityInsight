import string
import random

phrase = "The quick brown fox jumps over the lazy dog"
new_phrase = []
words = phrase.split(' ')

# for word in words:
#     outcome = random.random()
#     if outcome <= p:
#         ix = random.choice(range(len(word)))
#         new_word = ''.join([word[w] if w != ix else random.choice(string.ascii_letters) for w in range(len(word))])
#         new_phrase.append(new_word)
#     else:
#         new_phrase.append(word)


name_list = ['stop', 'play', 'pause', 'apple', 'banana']
p = 0.3
new_list = []


for name in name_list:
    outcome = random.random()
    if outcome <= p:
        ix = random.choice(range(len(name)))
        new_word = ''.join([name[w] if w != ix else random.choice(string.ascii_letters) for w in range(len(name))])
        new_list.append(new_word)
    else:
        new_list.append(name)


# new_phrase = ' '.join([w for w in new_phrase])
# print(new_phrase)

print(new_list)
