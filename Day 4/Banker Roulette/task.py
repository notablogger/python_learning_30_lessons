import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(friends[random.randint(0, len(friends)-1)])


print(random.choice(friends))
print(random.choices(friends,k=3))
