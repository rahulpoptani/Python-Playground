'''
Find common words in any given two sentences and return them sorted alphabetically.

Test Case #1
Input: ["Today is a great day to learn something new!", "Is today the day to learn?"]
Output: ["day", "is", "learn", "to", "today"]
Description: This test checks if the function can correctly identify common words regardless of their position in the sentence and handle a simple punctuation mark.

Test Case #2
Input: ["Learning to code: it's fun and engaging", "Engaging activities include learning to code."]
Output: ["code", "engaging", "learning", "to"]
Description: This test evaluates the function's ability to match words that are identical despite the presence of punctuation and possessive forms nearby.

Test Case #3
Input: ["The cat's favorite toy", "The favorite toy of the cat is here."]
Output: ["favorite", "the", "toy"]
Description: This test verifies if the function can correctly identify common words, including those preceded by possessive markers.
'''
import re
from collections import Counter

def find_common_words(input):
    """ 
    :type input: List[str] 
    :type sentence2: str 
    :rtype: Set[str]
    """

    sentence1 = input[0]
    sentence2 = input[1]

    sentence1 = re.sub(r'[^\w\s]', '', sentence1)
    sentence2 = re.sub(r'[^\w\s]', '', sentence2)

    frequency = Counter(sentence1.lower().split()) + Counter(sentence2.lower().split())
    return sorted([word for word in frequency if frequency[word] > 1])

# Time: O(n)
# Space: O(n)

# Test Case 1
input = ["Today is a great day to learn something new!", "Is today the day to learn?"]
print(find_common_words(input))

# Test Case 2
input = ["Learning to code: it's fun and engaging", "Engaging activities include learning to code."]
print(find_common_words(input))

# Test Case 3
input = ["The cat's favorite toy", "The favorite toy of the cat is here."]
print(find_common_words(input))
