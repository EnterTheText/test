def crypt(s):
    new = ""
    for k in s:
        print(alphabet.index(k.lower()) + n % 33 + 1)
        new += (alphabet[(alphabet.index(k) + n % 33 + 1)] if k.islower() else alphabet[
            (alphabet.index(k.lower()) + n % 33 + 1)].upper())
    return new
alphabet = [chr(i) for i in range(1072, 1104)]
alphabet.insert()
print(len(alphabet), *alphabet)
s = input()
n = int(input())
new = ""
print(crypt(s))