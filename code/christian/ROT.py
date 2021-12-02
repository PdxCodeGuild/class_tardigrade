

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ''
# Index       0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
# English     a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z
# ROT+13      n   o   p   q   r   s   t   u   v   w   x   y   z   a   b   c   d   e   f   g   h   i   j   k   l   m
# '''


user = input('What do you want to encode?: ')


def encode(message):
    answer = ''
    for char in message:
        index_position = letters.index(char)# .index used to get the index of a list
        if index_position > 12:
            rot_letter = letters[index_position-13]
            answer += rot_letter  # concantinate
        else:
            rot_letter = letters[index_position+13]  # checks everythin else
            answer += rot_letter
    return answer


print(encode(user))
