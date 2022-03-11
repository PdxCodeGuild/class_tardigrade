

with open('superheroes.csv', 'r') as f:
    heroes = f.read().split('\n')
# print(heroes, 'heroes')

headers = heroes[0].split(',')
# print(headers,'headers')
marvel = heroes[1:]
# print(marvel,'marvel')

hero_list = []
for hero in marvel:
    hero = hero.split(',')
    hero_dict = {}
    hero_dict= dict(zip(headers, marvel))
    hero_list.append(hero_dict)


def create_hero():
    global headers
    global hero_list
    hero_dict = {}
    for header in headers:
        prompt = input(f'Enter the {header} of the hero: ')
        hero_dict[header] = prompt
    hero_list.append(hero_dict)

def retrieve(name):
    global hero_list
    for hero in hero_list:
        if hero['name'] == name:
            return hero

def update(hero):
    global headers
    for header in headers:
        update = input(f'Enter an update for {header} (currently {hero[header]}')
        hero[header] = update

def delete(hero):
    global hero_list
    hero_list.pop(hero_list.index(hero))



while True:
    user = input('Do you want to create, retrieve, update, or delete a hero? or enter "done" to quit')
    if user == 'done':
        print('Goodbye!')
        break
    elif user == 'create':
        create_hero()
    elif user == 'retrieve':
        hero_name = input('Which hero do you want to retrieve?: ')
        hero = retrieve(hero) 
        for header in headers:
            print(f'{header}... {hero[header]}')
    elif user == 'update':
        hero_name = input('Which hero do you want to update?: ')
        hero = retrieve(hero)
        update(hero)
    elif user == 'delete':
        user = input('Which hero do you want to delete?: ')
        hero = retrieve(hero)
        delete(hero)












# Implement a CRUD REPL

# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list
    
        
  

