#List

fruits = ["apple", "banana","orange","kiwi"]
print(fruits)
print(fruits[-3],fruits[1])
print(fruits[1:])
fruits[2]="dragon fruit"

print(fruits[-3:-1])

bucket_fruits=["green apple","mango"]
fruits.extend(bucket_fruits)
print(fruits)
fruits.append("jackfruit")
print(fruits)