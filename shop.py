items = ["coffe", "soda", "candy", "pillow", "laptop", "pc", "drink"]

print("Welcome to casl's shop!!!")
print("here are the items:")

for x in range(len(items)):
    print(f"{x + 1}: {items[x]}")

buy = int(input("Enter the number of the item: "))

if range(0, len(items)).__contains__(buy - 1):
    print(f"you bought {items[buy - 1]}")
else:
    print("invalid item")