word=input("Enter a Word: ") or "Python"

print("Word:",word)
print("Length of Word:",len(word))
characters=list(word)
print("Characters in the given word:",characters)
pairs=list(zip(characters,characters[1:]))
print("Adjacent pairs:",pairs)
