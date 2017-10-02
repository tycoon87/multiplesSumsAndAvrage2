a = [1, 2, 5, 10, 255, 3]
x = 0

for i in range(1001):
    if ( i%2 != 0):
        print(i)

for i in range(1000000):
    if ( i%5 == 0):
        print(i)
        
for i in range(len(a)):
    if i < len(a):
        x = x+a[i]
print(x)

for i in range(len(a)):
    if i < len(a):
        x = x+a[i]
        x = x/2
print(x)