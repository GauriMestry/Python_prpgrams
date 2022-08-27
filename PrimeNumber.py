
Plain_Text=int(input("Enter plain text:"))
p=int(input("Enter value of P:"))
q=int(input("Enter value of q"))
N=p*q
Flag=0
def PrimeNumber(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                print(n,"is not a prime number")
                break
        else:
            print(n,"is prime number")
            Flag=1
            return Flag
    else:
        print(n,"num is not a prime number")
        
        
        
        M=8
    #for i in M:
    if M==2:
        print(M,"is Prime Number")
        Flag=1
        return Flag
    elif M==3:
        print(M,"is Prime Number")
        Flag=1
        return Flag
    else:
        l=(M-1)/6
        P_N=6*l+1
        if(P_N==M):
            print(M,"is prime")
            Flag=1
            return Flag
        else:
            print(M,"is not a prime number")
            
            
#Public key 
    if M_Fac==2:
        PublicKey=3
        return PublicKey
    elif M_Fac==3:
        PublicKey=5
        return PublicKey
    else:
        p_num=7
        while True:
            Prime=PrimeNumber(p_num)
            if Prime:
                for i in range(p_num+1,p_num+3,):
                    P=PrimeNumber(i)
                    print(P)
                    if P and P>p_num:
                        PublicKey=p
                        return PublicKey
            break            
        p_num+=2