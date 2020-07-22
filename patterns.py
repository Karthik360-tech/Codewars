#single sided staircase 
def pattern (n) :
    counter = ''
    temp = n-1
    j=0
    while j<n :
        if temp >0 :
          counter += '*'
          print(' '*temp+counter)
        else :
            counter += '*'
            print(counter)
        temp -= 1
        j+=1

 #double sided staircase 
def pattern1 () :
    num =  int(input('INPUT :'))
    count = ''
    temp = num-1
    for j in range(num,0,-1):
        count+= '*'
        ans1 = ( ' '*j + str(count))
        ans2 = ( ' '*temp + str(count))
        print(str(ans1)+'\t'+'HELLO'+str(ans2))
        
while True :
    print('''1.One Sided Staircase\n2.Complete Staircase\n3.Exit\n''')
    choice = int(input('Enter the choice :'))
    if choice == 1 :
        num = int(input('Enter a positive number :'))
        pattern(num)
    elif choice ==2 :
        pattern1()
    elif choice == 3 :
        print('Thanks !!')
        break
