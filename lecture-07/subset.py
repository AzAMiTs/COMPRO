seta = {1,2,3,4}
setb = {2,3}
setc = {1,2,3,4}
setd = {1,2,3,5,6}

print("is seta a superset of setb", seta >= setb)
print("is setb a subset of seta", setb <= seta)


print("is seta a proper superset of setb", seta > setb)
print("is seta a proper subset of setb", setb < seta)


print("is seta and setc eqaul", seta == setc)


print("is setb a subset of setd and not eqaul", setb <= setd and setb != setd)



