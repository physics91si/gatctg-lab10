from sets import Set

a = Set()
a.add(4)
a.add(5)
a.remove(3)
a.remove(4)
a.add(1)
a.add(7)
a.add(3)

b = Set()
b.add(2)
b.add(4)
b.add(6)
b.add(7)

print(a - b)
