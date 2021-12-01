"""Lab 11: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file. You can find a .txt file to use at Project Gutenberg The
 automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The
 general formula to compute the ARI is as follows:

The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number
of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal,
always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:"""

book = open(r"C:\Users\dhols\Documents\GitHub\class_tardigrade\code\Dustin\wizard-of-oz.txt", "rt")
data = book.read()
words = data.split()

print('Number of words in text file :', len(words))

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
