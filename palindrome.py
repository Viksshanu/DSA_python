def palindrome(x):
    if x < 0:     #check is there any negative number ?
        return False

    n = x   #copy your original number into x  and use x
    rev = 0 #create a variable to store the reverse of number

    while n > 0:  
        d = n % 10   #get the last digit of n
        rev = rev * 10 + d  #add last digit into rev and shift rev to left by multiplying by 10
        n = n // 10   #remove last digit from n by doing integer division by 10

    if x==rev:      #compare otiginal valuse to the reversed value
        return True
    else:
        return False


print(palindrome(121))