def rem(l, word):
    while word in l:
        l.remove(word)
    return l

l = ["shivam", "Rohan", "rm"]

print(rem(l, "rm"))
