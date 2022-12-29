a = ['-','-','-']
b = ['-','-','-']
c = ['-','-','-']
var=1

def display():
    print("{}|{}|{}".format(a[0],a[1],a[2]))
    print("{}|{}|{}".format(b[0],b[1],b[2]))
    print("{}|{}|{}".format(c[0],c[1],c[2]))

def enter():
    global var,rep
    
    if var==1:
        rep='x'
        var=0
    elif var==0:
        rep='o'
        var=1
        
    pos=int(input("enter position:"))
    if pos==1 or pos==2 or pos==3:
        a[pos-1]=rep
    elif pos==4 or pos==5 or pos==6:
        b[pos-4]=rep
    elif pos==7 or pos==8 or pos==9:
        c[pos-7]=rep
    display()





def clear():
    
    for i in range(0,3):
            a[i]='-'
    for i in range(0,3):
            b[i]='-'
    for i in range(0,3):
            c[i]='-'
    display()

def result(p,q):
    print("your scores are x={} and o={}".format(p,q))
    if(p>q):
        print("x won!")
    elif(q>p):
       print("o won!")
    else:
        print("draw!")
    display()

        

if __name__=="__main__":
    display()
    
    i=1
    p=0
    q=0
    while(i==1):
        enter()
        global rep
        global pos
        
        if(rep=='x'):
            if((a[1]==a[2]==a[0]==(rep))or(b[1]==b[2]==b[0]==(rep))or(c[1]==c[2]==c[0]==(rep))):
                print("{} won!".format(rep))
                p+=1
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
    
            elif((a[0]==b[0]==c[0]==(rep))or(a[1]==b[1]==c[1]==(rep))or(a[2]==b[2]==c[2]==(rep))):
                print("{} won!".format(rep))
                p+=1
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
                
            elif((a[0]==b[1]==c[2]==(rep))or(a[2]==b[1]==c[0]==(rep))):
                print("{} won!".format(rep))
                p+=1
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
            elif(a[0:2]==rep and b[0:2]==rep and c[0:2]==rep):
                print("draw!")
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
            else:
                pass
        else:
            if((a[1]==a[2]==a[0]==(rep))or(b[1]==b[2]==b[0]==(rep))or(c[1]==c[2]==c[0]==(rep))):
                print("{} won!".format(rep))
                q+=1
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
            elif((a[0]==b[0]==c[0]==(rep))or(a[1]==b[1]==c[1]==(rep))or(a[2]==b[2]==c[2]==(rep))):
                print("{} won!".format(rep))
                q+=1
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
                
            elif((a[0]==b[1]==c[2]==(rep))or(a[2]==b[1]==c[0]==(rep))):
                print("{} won!".format(rep))
                q+=1
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
            elif(a[0:2]==rep and b[0:2]==rep and c[0:2]==rep):
                print("draw!")
                res=str(input("do you wish to continue? yes/no\n"))
                if(res==('yes' or 'YES')):
                    clear()
                    
                elif(res==('no' or 'NO')):
                    result(p,q)
                else:
                    print("invalid entry")
            else:
                pass
        
            
        
    
       
        
        
    """ clear()"""
""" lets say u won ok, after that its supposed to clr the brd, after someone wins it d\shouls \d ask if u want to continue, if yes clrs brd and continues. if not it breaks and see how many times  x and o won"""
    
