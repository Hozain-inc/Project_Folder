# shopping list
item_1 = input("enter first item on your shopping list:")
item_2 = input("enter second item on your shopping list:")
item_3 = input("enter third item on your shopping list:")
items = (item_1, item_2, item_3)
lst = list(items)
item_4 = input(" enter one more item on your shopping list:")
item_5 = input(" enter one more item on your shopping list:")
extra_items = (item_4, item_5)
result = items + extra_items
shopping_list = tuple(result)
print("the items for your shopping list", "|".join(result))
print(type/shopping_list)