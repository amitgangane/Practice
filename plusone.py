list_old = [1,2,3]
cunt = 1
total = 0
for item in list_old [::-1]:
            total = total + cunt*item
            cunt = cunt*10
total = total +1
list_one = []

for i in str(total):
    list_one.append(int(i))
print(list_one)