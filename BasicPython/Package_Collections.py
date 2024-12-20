# A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. 
from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(dict(ChainMap(adjustments, baseline)))


###############################################################################################################################################
# A counter tool is provided to support convenient and rapid tallies.
# A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

import re
words = re.findall(r'\w+', open('BasicPython/resources/hamlet.txt').read().lower())
print(Counter(words).most_common(10)) # list of words
print(Counter('AABBCCAABB').most_common(3)) # chars in a word
print(Counter('AABBCCAABB').total()) # chars in a word


###############################################################################################################################################
#  Deque
from collections import deque
d = deque('ghi')
print(d)
d.append('j')
d.appendleft('f')
print(d)
print(d.pop())
print(d.popleft())
d.extend('jkl')
print(d)
d.rotate(2) # right rotate, negative for left rotate
print(d)
d.clear()
print(d)

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            yield next(iterators[0])
            iterators.rotate(-1)
        except StopIteration:
            iterators.popleft() # Remove an exhausted iterator.

print(list(roundrobin('ABC', 'D', 'EF')))

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d = deque([1,2,3,4,5])
delete_nth(d, 3)
print(d) # 3rd index, which is 4 is removed


###############################################################################################################################################
# defaultdict is a subclass of the built-in dict class. It overrides one method(__missing__) and adds one writable instance variable.
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(list)
ds = defaultdict(set)

for k, v in s:
    d[k].append(v)
    ds[k].add(v)
print(d.items())
print(ds.items())

# Setting the default_factory to int makes the defaultdict useful for counting
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d.items())


###############################################################################################################################################
# Named Tuple
from collections import namedtuple
EmployeeRecord = namedtuple('EmployeeRecord', 'first, last, pay')
import sqlite3
conn = sqlite3.connect('BasicPython/resources/employee.db')
cursor = conn.cursor()
cursor.execute('SELECT first, last, pay FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.first, emp.last, emp.pay)

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p.x, p.y)
p = Point._make([30,50])
print(p.x, p.y)
