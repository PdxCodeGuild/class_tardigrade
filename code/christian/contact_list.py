

with open('superheroes.csv', 'r') as f:
    heroes = f.read().split('\n')
print(heroes, 'heroes')

headers = heroes[0].split(',')
print(headers,'headers')
marvel = heroes[1:]
print(marvel,'marvel')


for hero in marvel:
    print(hero.split(','))
    hero_dict = {}
    hero_dict[headers[0]] = marvel
    for i in marvel:
     print(marvel.split(','))
    
        
  

