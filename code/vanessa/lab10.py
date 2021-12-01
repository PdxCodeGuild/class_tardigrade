#ROT CIPHER

# get input from user for string to encoded
# separate string into inidividual characters/components
# encrypt with ROT+ 13 by finding corresponding character and add it to an output string
"""my thoughts are: need a dictionary for ROT+ 13 replacements and an output list for output string"""
"my thoughts 2: it's about list manipulation so dictionary not needed?"

# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j   k   l   m

english=["a","b","c","d","e","f",
"g","h","i","j","k","l","m","n",
"o","p","q","r","s","t","u","v",
"w","x","y","z"]



user_input = input("Please type word to encode: ")


# print(user_input)
def encrypt(entered_word):
    new_word= ""
    print(entered_word)
    for i in entered_word:
        index = english.index(i)
        print(index)
        if index > 13:
            new_letter = english[index-13]
            new_word += new_letter
        else:
            new_letter = english[index+13]
            new_word += new_letter
    print(new_word)
            
(encrypt(user_input))
    