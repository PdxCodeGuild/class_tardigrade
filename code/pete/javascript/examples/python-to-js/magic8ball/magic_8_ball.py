import random

responses = [
    "I don't know",
    "What? I wasn't listening.  Could you please ask again?",
    'I know it to be true',
    'Doubtful',
    'sure, i guess',
]

print('welcome to the amazing 8 ball')

input('what is it you wish to know?  ')

print('Looking into it...')

response = random.choice(responses)

print(response)
# random.randint(0, 4)