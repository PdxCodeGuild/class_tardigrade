

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
    for i in range(len(headers)):
        # print(headers[i])
        # print(hero[i])
        hero_dict[headers[i]] = hero[i]
    hero_list.append(hero_dict)
print(hero_list)



while True:
    user_input = input('Do you want to create a hero? Retreive a hero? Update hero? Delete a hero? or type "done" to quit: ')
    if user_input == "done":
        print('Thanks for playing')
        break
    elif user_input == "create a hero":
        #create a dict for new hero
        new_hero = {}
        hero_name =  input('What is their name?: ')
        new_hero[headers[0]] = hero_name
        hero_power = input('What is their power?: ')
        new_hero[headers[1]] = hero_power
        hero_enemy = input('Who is their enemy?: ')
        new_hero[headers[2]] = hero_enemy
        hero_alias = input('What is their alias?: ')
        new_hero[headers[3]] = hero_alias
        hero_list.append(new_hero)
        print(hero_list)
    elif user_input == "retreive a hero":
        pull_hero = input("what is their name?: ")
        for hero in hero_dict:
            if pull_hero == hero_dict['name']:
                    print(hero, hero_dict[hero])
        #find dictionary of hero and print dictionary
    elif user_input == 'update a hero':
        update_hero = input('Which hero do you want to update?: ')
        update_value = input('what do you want to update?') #name power enemy alias
        # update_
        #ask what value to change it to
        for i in range(len(hero_list)):
            hero_list[i] = update_hero[i]
            print(hero_list)











        
        

    


# Implement a CRUD REPL

# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list
    
        
  

