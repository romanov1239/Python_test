def F(x,y,z,w):
    l1=z==w
    l2=x<=l1
    l3=not(y<=w)
    return int(l2 or l3)

print('x y z w | F(x,y,z,w)')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if F(x,y,z,w)==0:
                    print(x, y, z, w, '|', F(x,y,z,w))