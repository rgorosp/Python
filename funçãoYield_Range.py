"""
FUNÇÃO YIELD - RANGE
"""
def geradora():
    a = 2
    while True:
        yield a 
        a += 2

g = geradora()

for i in range(20):
    print(next(g), end='*')

print('\n------------------------------------------------------')