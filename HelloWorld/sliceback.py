#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1]) # useful when not sure if string is empty or not
print(letters[0])