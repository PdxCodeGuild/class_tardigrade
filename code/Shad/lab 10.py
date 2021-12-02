code=[]
rot13 = {'n':0, 'o':1,'p':2,'q':3,'r':4,'s':5,'t':6,'u':7,'v':8,'w':9,'x':10,'y':11,'z':12,'a':13,'b':14,'c':15,'d':16,'e':17,'f':18,'g':19,'h':20,'i':21,'j':22,'k':23,'l':24,'m':25} 
user = input('Enter your string: ')
for i, co in enumerate(user):
    if True:
        i=rot13.get(user[i])
    print(i, end=' ')


# rot13.get(user)
