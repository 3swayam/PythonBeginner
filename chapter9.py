# while and for
my_num=0
while my_num<=2:
    print("less than 2")
    my_num=my_num+1

friends=["h","e","l","p"]
for frnd in friends:
    print(frnd)

for index in range(len(friends)):
    print(str(index+1)+ "-"+friends[index])
