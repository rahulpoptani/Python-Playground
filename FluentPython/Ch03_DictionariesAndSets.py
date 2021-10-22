# Dictionary Comprehension
dial_codes = [                                                  
(880, 'Bangladesh'),
(55,  'Brazil'),
(86,  'China'),
(91,  'India'),
(62,  'Indonesia'),
(81,  'Japan'),
(234, 'Nigeria'),
(92,  'Pakistan'),
(7,   'Russia'),
(1,   'United States'),]

country_dial = {country: code for code, country in dial_codes}
print(country_dial)

dial_country = {code: country.upper() for country, code in sorted(country_dial.items())}
print(dial_country)


# Unpacking Mappings
def dump(**kwargs):
    return kwargs

print(dump(**country_dial))


# Merging Mapping with Pipe |
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

# Returns new map
print(d1 | d2)
# Inplace merge
d1 |= d2
print(d1)

# Hashable - An object is hashable if it has a hash code which never changes during its life time
t1 = (1, 2, (3, 4))
print(hash(t1))
t2 = (1, 2, [3, 4])
# Error Out because list is not hashable
# print(hash(t2)) # list are unhashable type

