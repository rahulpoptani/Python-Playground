'''
Input:
-------
177
10
Output:
--------
17
7
(17, 7)
'''

def format_output(a,b):
    div = a//b
    mod = a%b
    print(div)
    print(mod)
    print('({}, {})'.format(div, mod))

if __name__ == '__main__':
    a, b = int(input()), int(input())
    format_output(a,b)