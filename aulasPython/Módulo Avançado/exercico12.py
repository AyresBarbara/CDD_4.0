from biblioteca12 import *
users = [""]*5
tam = len(users)

for x in range(tam):
    users[x] = input(f"Digite o nome do {x+1}ª usuário: ")
for x in range(tam):
    print(f"{x+1} - "+ users[x])

users.reverse()
print(users)
"""for x in range(tam-1, -1, -1):
    print(users[x], end=" ")"""
