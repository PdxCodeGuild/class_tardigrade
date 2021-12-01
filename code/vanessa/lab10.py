#ROT CIPHER

# get input from user for string to encoded
# separate string into inidividual characters/components
# encrypt with ROT+ 13 by finding corresponding character and add it to an output string
"""my thoughts are: need a dictionary for ROT+ 13 replacements and an output list for output string"""
"my thoughts 2: it's about list manipulation so dictionary not needed?"

# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j

english=["a","b","c","d","e","f",
"g","h","i","j","k","l","m","n",
"o","p","q","r","s","t","u","v",
"w","x","y","z"]
rot= english.copy()

for j in range(len(rot)):
    rot.insert(j,(english[j]+13))
    print (j)
    print(rot)
    




# word_to_encode = input("Please type word to encode: ")
# word_to_encode =list(word_to_encode)
# print(word_to_encode)
# def encrypt(entered_word):
#     new_word=[]
#     for j in range(len(entered_word)):
#             entered_word.insert(j,english[j+13])
#             new_word.append(entered_word[j])
#     print(new_word)
            

# (encrypt(rot))
    