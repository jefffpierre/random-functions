import random
import my_module

random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)

random_float1 = random.random() * 10 #
print(random_float1)

random_float2 = random.uniform(0.0, 5.0)
print(random_float2)

love_score = random.randint(1, 100)
print(f"Your score is: {love_score}")