#Exercise 11

print("How old are you?")
age = input()
print("How tall are you?", end=' ') # We put a end=' ' at the end of each print line. This tells print to not end the line with a newline character and go to the next line.
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
