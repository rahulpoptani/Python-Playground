'''
Find non-repeated words in any given 2 sentences.

Test Case #1
Input: ["The cat in the hat", "A cat in a mat"]
Output: ['The', 'the', 'hat', 'A', 'a', 'mat']
Description: This tests the function’s ability to identify non-repeated words between sentences with slight variations and common stop words.

Test Case #2
Input: ["Innovation distinguishes between a leader and a follower", "Creativity is thinking up new things, Innovation is doing new things"]
Output: ['distinguishes', 'between', 'leader', 'and', 'follower', 'Creativity', 'thinking', 'up', 'things,', 'doing', 'things']
Description: This case evaluates the algorithm’s handling of longer sentences with multiple repeated and unique words.

Test Case #3
Input: ["", "The quick brown fox jumps over the lazy dog"]
Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
Description: The function is tested with an empty string for one sentence and a list of non-repeating words in another to ensure correct identification when no commonality exists.
'''

from collections import Counter

def non_repeated_words(input):
    """
    :type input: List[str]
    :rtype: List[str]
    """

    sentence1 = input[0]
    sentence2 = input[1]

    word_counts = Counter(sentence1.split() + sentence2.split())
    return [word for word, count in word_counts.items() if count == 1]

# Time: O(n)
# Space: O(n)

# Test Case 1
input = ["The cat in the hat", "A cat in a mat"]
print(non_repeated_words(input))

# Test Case 2
input = ["Innovation distinguishes between a leader and a follower", "Creativity is thinking up new things, Innovation is doing new things"]
print(non_repeated_words(input))

# Test Case 3
input = ["", "The quick brown fox jumps over the lazy dog"]
print(non_repeated_words(input))
