bone = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
marrow = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
text = input()

# encipher
CipheredText = ""
for i in text.upper():
    if i.isalpha(): CipheredText += marrow[ (bone[i] + key)%26 ]
    else: CipheredText += i

# decipher
text2 = ""
for i in CipheredText.upper():
    if i.isalpha(): text2 += marrow[ (bone[i] - key)%26 ]
    else:
      text2 += i

print(text)
print(CipheredText)
print(text2)
