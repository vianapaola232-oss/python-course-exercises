phrase = str(input("Write a phrase: ")).strip().upper()
print(f"The letter A appears {phrase.count('A')} times.")
print(f"The first letter A appears in position {phrase.find('A') + 1}.")
print(f"The last letter A appears in position {phrase.rfind('A') + 1}.")
