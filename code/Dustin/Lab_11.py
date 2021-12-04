"""Lab 11: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file. You can find a .txt file to use at Project Gutenberg The
 automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The
 general formula to compute the ARI is as follows:

The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number
of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal,
always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:"""

book = open(r"C:\Users\dhols\Documents\GitHub\class_tardigrade\code\Dustin\wizard-of-oz.txt", "r")
data = book.read()
words = data.split()
import math
"""Using the math module seemed to be the best way to round up, I dont know if we cover it specifically in
class. So wanted to note its use here."""

"""parsing the txt file here for the relevant information"""
just_char = data.replace(" ","")
number_of_char = len(just_char)
number_of_words = len(words)
number_of_sentences = data.count(".")

"""Checking my code is done correctly with print statements"""
#print('Number of characters: ', number_of_char)
#print('Number of words: ', number_of_words)
#print('Number of sentences: ', number_of_sentences)

ari_score = math.ceil(4.71 * (number_of_char / number_of_words) +.5 * (number_of_words / number_of_sentences) - 21.43)


ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
current_scale = ari_scale[ari_score]


"""Output """

print("The ARI for wizard-of-oz.txt is : ", ari_score)
print(f"That is suitable for an average person {current_scale['ages']} years old.")
print(f"This corresponds to a {current_scale['grade_level']} level of difficulty.")