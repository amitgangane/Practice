n = 121
if n<0:
    print (False)
else:
    revs_num = 0
    temp =n
    while temp != 0:
        rem = temp % 10
        revs_num = revs_num * 10 + rem
        temp = temp//10
    print(revs_num == n)






