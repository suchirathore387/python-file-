a = input("Enter a string: ")

v = 0
c = 0

for i in a:
    if i.isalpha():
        if i in "aeiouAEIOU":
            v = v + 1
        else:
            c = c + 1

print("Vowels =", v)
print("Consonants =", c)
