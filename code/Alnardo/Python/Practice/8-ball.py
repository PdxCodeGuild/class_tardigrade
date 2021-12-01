# Magic 8-Ball
# It is certain
# 
# Without a doubt
# Yes definitely
# You may rely on it
# As I see it, yes
# Most likely
# Outlook good
# Yes
# Signs point to yes
# Reply hazy try again
# Ask again later
# Better not tell you now
# Cannot predict now
# Concentrate and ask again
# Don't count on it
# My reply is no
# My sources say no
# Outlook not so good
# Very doubtful

import random
predictions = ['It is certain', 'My reply is no', 'Without a doubt', 'Yes, definitely', 'Very doubtful', 'As I see it, yes', 'Most likely', 'Reply hazy try again', 'Ask again later', 'Better not tell you now']


message = input('Would you like to use the Magic 8-ball? yes/no: ')


while message == 'yes':
    question = input('What would you like to ask the Magic 8-ball?: ')
    eight_ball_answer = random.choice(predictions)
    print(eight_ball_answer)
    message = input('Play again? yes/no: ')

if message == 'no':
    print('Thanks for playing!')
