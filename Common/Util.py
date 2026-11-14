def separator(msg: str, hash_count = 15):
   print("#" * hash_count + " " + msg + " " + hash_count * "#")

def all_substrings(s: str) -> list[str]:
    """
    Returns all substrings of a given string s.
    """
    substrings = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    
    return substrings

assert all_substrings("abc") == ["a", "ab", "abc", "b", "bc", "c"]
assert all_substrings("abcd") == ["a", "ab", "abc", "abcd", "b", "bc", "bcd", "c", "cd", "d"]
