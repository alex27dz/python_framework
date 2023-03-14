file = open('hello.txt', 'r')
content = file.read()
print(content)
file.close()

new_content = content.replace('alex', 'Bob')
file = open('hello.txt', 'w')
file.write(new_content)
file.close()

file = open('hello.txt', 'r')
content = file.read()
print(content)
file.close()

