import itertools


ll = [x for x in range(1, 11)]

print(list(itertools.accumulate(ll)))

print(list(itertools.batched(ll,3)))

print(list(itertools.chain(ll, ll[:4])))

print(list(itertools.combinations(ll[:4],2)))

print(list(itertools.pairwise(ll)))

print(list(itertools.permutations(ll[:3])))

print(list(itertools.product(['A','B','C'], ['x','y'])))

print(list(itertools.repeat('AB', 3)))

print(list(itertools.takewhile(lambda x: x>5, reversed(ll))))

