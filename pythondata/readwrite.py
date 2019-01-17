with open('name.txt') as f:
    name = f.read()

    greeting = "Hello my name is " + name + "."

with open('testwrite.txt', "w") as g:
    g.write(greeting)


print(greeting)