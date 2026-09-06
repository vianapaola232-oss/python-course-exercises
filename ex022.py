name = str(input("Full name: ")).strip()

print(f"Your name in uppercase is {name.upper()}.")
print(f"Your name in lowercase is {name.lower()}.")
print(f"Your name has {len(name) - name.count(' ')} characters.")
characters = name.split()
print(f"The first name {characters[0]} has {len(characters[0])} characters.")
