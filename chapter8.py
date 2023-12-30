#dictionaries (key value pair)

month_shortcuts={
    "jan":"january",
    "feb":"february",
    "mar":"march"
}

your_month=input("Enter your month : ")
if(your_month.lower()=="jan"):
    print("this is "+month_shortcuts['jan'])
elif (your_month.lower()=="feb"):
    print("this is "+month_shortcuts['feb'])
elif (your_month.lower()=="mar"):
    print("this is "+month_shortcuts['mar'])
else:
    print("Error : "+month_shortcuts.get("any","Invalid key you have entered"))