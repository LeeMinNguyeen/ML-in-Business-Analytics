'''
    Name: Le Minh Nguyenn
    Student ID: K224161829
'''

### Default Parameter ###

def sum(a, b, c=100):
    return a + b + c

print(sum(1, 2)) # 103
print(sum(a=1, b=2)) # 103
print(sum(1, 2, 500)) # 503
print(sum(1, 2, c=500)) # 503

