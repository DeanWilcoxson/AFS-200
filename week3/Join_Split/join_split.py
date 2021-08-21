csv = 'Eric,John,Michael,Terry,Graham,Terry G,Brian'

friends_list = []

name = csv.split(',')
print(name)

for letter in name:
    friends_list.append(letter)

print(friends_list)

for letter in friends_list:
    print(letter)
