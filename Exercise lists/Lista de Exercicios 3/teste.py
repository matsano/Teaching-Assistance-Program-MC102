v1 = []
v2 = []
n = 123456789
while n != 0:
    v1 . append ( n % 10)
    n = n // 10
    v2 . append (1)

for a in v1 [: -1]:
    print (a , end = ", ")
print ( v1 [ -1])

for a in v2 [: -1]:
    print (a , end = ", ")
print ( v2 [ -1])

for i in range (len ( v1 ) ) :
    for j in range ( v1 [ i ]) :
        v2 [ i ] = 2 * v2 [ i ]

for a in v2 :
    print (a , end = ", ")
print (1)
