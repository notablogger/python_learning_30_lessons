import random
import my_module

print(f"number from my module {my_module.number}")
print(random.randint(1,10))
print(random.random()*10)
print(random.uniform(1,10))


#head tail logi based on even odd
randint = random.randint(1, 10)
print(randint)
if randint % 2==0:
    print("head")
else:
    print("tail")