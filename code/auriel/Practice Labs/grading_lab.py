grading_score = int(input('Enter grading score 0-100: ')) 

if grading_score >= 90: 
    print(f'Grade is A')
elif grading_score >= 80 and grading_score <= 89:
    print(f'Grade is B') 
elif grading_score >= 70 and grading_score <= 79:
    print(f'Grade is C') 
elif grading_score >= 60 and grading_score <= 69:
    print(f'Grade is D') 
else :
    print(f'Grade is F')