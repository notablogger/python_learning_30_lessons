alph=["1","2","3","4","5","6","7","8","9"]
n_alph=["a","b","c","d","e","f","g","h","i","j"]


print(alph)
print(alph[0])
print(alph[1])
print(alph[2])
print(alph[-0])

#override(replace)
alph[2]="new"
print(alph[2])

#insert on a particular loc
alph.insert(2,"new1")
print(alph[2])

#append at end
alph.append("10")
print(alph)

#remove
alph.remove("1")
print(alph)

#remove from end and return
print(alph.pop())
print(alph)

#concat
alph.extend(n_alph)
print(alph)
print(n_alph)

#sort
alph.sort()
print(alph)

#reverse
alph.reverse()
print(alph)