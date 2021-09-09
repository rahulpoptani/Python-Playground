import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
pat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-123-schafer@work.net

'''

'''
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
'''


# pattern = re.compile(r'ABC')

# pattern = re.compile(r'\d') # Single digit match

# pattern = re.compile(r'\d+') # Sequence of digit match

# pattern = re.compile(r'\w+') # Sequence of words match

# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # phone number. 3 digit followed by - or .
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}') # phone number. 3 digit followed by - or .

# pattern = re.compile(r'[^b]at') # cat, mat, pat but not bat

# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # Mr Mrs

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.(com|edu|net)') # Email -> Note: not a valid expression. dont use in prod




matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# print(text_to_search[55:56])