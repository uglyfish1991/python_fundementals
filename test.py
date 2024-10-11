
shopping_list =[
    "cheese",
    "beans",
    "crisps",
    "milk",
    "apples"
]
at_the_shops =[
    "pears",
    "jam",
    "cheese",
    "apples",
    "bread",
    "tuna",
    "crisps"
]
for i in range(len(shopping_list)):
    for j in range(len(at_the_shops)):
        if shopping_list[i] == at_the_shops[j]:
            print("They’ve got it!", shopping_list[i])
            break
    else:
        print("They don't have", shopping_list[i])

print(at_the_shops)
print(*at_the_shops)