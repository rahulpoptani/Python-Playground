import re


# 1. re.match() - This function attempts to match a pattern at the beginning of the string.
# Syntax: re.match(pattern, string, flags=0)
# Example:
result = re.match(r'Python', 'Python is easy')
print(result.group())  # Output: Python

# 2. re.search() - This function searches for the first occurrence of a pattern in the string.
# Syntax: re.search(pattern, string, flags=0)
# Example:
result = re.search(r'Python', 'Python is easy')
print(result.group(0))  # Output: Python

# 3. re.findall() - This function returns a list of all occurrences of a pattern in the string.
# Syntax: re.findall(pattern, string, flags=0)
# Example:
result = re.findall(r'Python', 'Python is easy, Python is fun')
print(result)  # Output: ['Python', 'Python']

# 4. re.sub() - This function replaces all occurrences of a pattern in the string with a new string.
# Syntax: re.sub(pattern, repl, string, count=0, flags=0)
# Example:
result = re.sub(r'Python', 'Java', 'Python is easy, Python is fun')
print(result)  # Output: Java is easy, Java is fun

# 5. re.split() - This function splits the string based on a pattern and returns a list of substrings.
# Syntax: re.split(pattern, string, maxsplit=0, flags=0)
# Example:
result = re.split(r'\s', 'Python is easy')
print(result)  # Output: ['Python', 'is', 'easy']

# 6. re.compile() - This function compiles a regular expression pattern into a regular expression object.
# Syntax: re.compile(pattern, flags=0)
# Example:
pattern = re.compile(r'Python')
result = pattern.findall('Python is easy, Python is fun')
print(result)  # Output: ['Python', 'Python']

# 7. Special Characters:
# - . : Matches any character except a newline.
# - ^ : Matches the start of the string.
# - $ : Matches the end of the string.
# - * : Matches zero or more occurrences of the preceding character.
# - + : Matches one or more occurrences of the preceding character.
# - ? : Matches zero or one occurrence of the preceding character.
# - {n} : Matches exactly n occurrences of the preceding character.
# - {n,} : Matches n or more occurrences of the preceding character.
# - {n,m} : Matches between n and m occurrences of the preceding character.
# - [] : Matches any one of the characters inside the square brackets.
# - [^] : Matches any character not inside the square brackets.
# - | : Matches either the pattern on the left or the pattern on the right.

# 8. Special Sequences:
# - \d : Matches any digit (0-9).
# - \D : Matches any non-digit character.
# - \s : Matches any whitespace character.
# - \S : Matches any non-whitespace character.
# - \w : Matches any alphanumeric character.
# - \W : Matches any non-alphanumeric character.
# - \b : Matches the empty string at the beginning or end of a word.
# - \B : Matches the empty string not at the beginning or end of a word.

# 9. Grouping:
# - (pattern) : Matches the pattern inside the parentheses and captures the matched substring.
# - (?P<name>pattern) : Matches the pattern and captures the matched substring with the specified name.
# - \1, \2, ... : Refers to the first, second, ... captured group in the pattern.

# 10. Flags:
# - re.IGNORECASE : Makes the pattern case-insensitive.
# - re.MULTILINE : Makes the pattern match the start and end of each line.
# - re.DOTALL : Makes the dot (.) match any character, including a newline.
# - re.VERBOSE : Allows the use of whitespace and comments within the pattern.

# 11. Anchors:
# - ^ : Matches the start of the string.
# - $ : Matches the end of the string.
# - \b : Matches the empty string at the beginning or end of a word.
# - \B : Matches the empty string not at the beginning or end of a word.

# 12. Quantifiers:
# - * : Matches zero or more occurrences of the preceding character.
# - + : Matches one or more occurrences of the preceding character.
# - ? : Matches zero or one occurrence of the preceding character.
# - {n} : Matches exactly n occurrences of the preceding character.
# - {n,} : Matches n or more occurrences of the preceding character.
# - {n,m} : Matches between n and m occurrences of the preceding character.

# 13. Character Classes:
# - [abc] : Matches any one of the characters a, b, or c.
# - [a-z] : Matches any lowercase letter from a to z.
# - [A-Z] : Matches any uppercase letter from A to Z.
# - [0-9] : Matches any digit from 0 to 9.
# - [a-zA-Z0-9] : Matches any alphanumeric character.
# - [^abc] : Matches any character except a, b, or c.
# - [^a-z] : Matches any character except a lowercase letter from a to z.
# - [^A-Z] : Matches any character except an uppercase letter from A to Z.
# - [^0-9] : Matches any character except a digit from 0 to 9.
# - [^a-zA-Z0-9] : Matches any character except an alphanumeric character.

# 14. Lookahead and Lookbehind:
# - (?=pattern) : Positive lookahead assertion.
# - (?!pattern) : Negative lookahead assertion.
# - (?<=pattern) : Positive lookbehind assertion.
# - (?<!pattern) : Negative lookbehind assertion.

# 15. Greedy and Non-Greedy Matching:
# - Greedy Matching : Matches as much as possible.
# - Non-Greedy Matching : Matches as little as possible.
# - *? : Non-greedy version of *.
# - +? : Non-greedy version of +.
# - ?? : Non-greedy version of ?.
# - {n}? : Non-greedy version of {n}.
# - {n,}? : Non-greedy version of {n,}.
# - {n,m}? : Non-greedy version of {n,m}.
# Example:
# import re
# result = re.search(r'<.*?>', '<html><head><title>Title</title></head></html>')
# print(result.group(0))  # Output: <html>

# 16. Backreferences:
# - \1, \2, ... : Refers to the first, second, ... captured group in the pattern.
# Example:
# import re
# result = re.search(r'(\w+) \1', 'hello hello world')
# print(result.group(0))  # Output: hello hello

# 17. Named Groups:
# - (?P<name>pattern) : Matches the pattern and captures the matched substring with the specified name.
# Example:
# import re
# result = re.search(r'(?P<word>\w+) (?P=word)', 'hello hello world')
# print(result.group(0))  # Output: hello hello

# 18. Substitution:
# - \g<name> : Refers to the named group in the substitution string.
# Example:
# import re
# result = re.sub(r'(?P<word>\w+) (?P=word)', r'\g<word>', 'hello hello world')
# print(result)  # Output: hello world

