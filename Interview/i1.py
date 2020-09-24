# Overlap problem

list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

n = 3
m = 1

for i in range(0, len(list_), n-m):
    print(list_[i: i+n])
