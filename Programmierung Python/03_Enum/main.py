from cupsizes_enum import Cupsize

print(Cupsize.GIANT) # Den Typ
print(Cupsize.GIANT.name) # Den Namen
print(Cupsize.GIANT.value) # Den Wert


print(Cupsize(0.5).name) # Gibt den Namen zu dem gegeben Wert aus.

for cupsize in (Cupsize):
    print(cupsize.value, "-", cupsize)

if Cupsize.GIANT.name == Cupsize.LARGE.name:
    print("Giant and Large are the same")
else:
    print("Giant and Large are not the same")

if Cupsize.GIANT is Cupsize.LARGE:
    print("Giant and Large are the same")
else:
    print("Giant and Large are not the same")