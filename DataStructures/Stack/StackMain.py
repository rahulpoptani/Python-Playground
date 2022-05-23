from doctest import Example
from Stack import Stack

# Create a stack
s1 = Stack()

print('Stack Empty? {}'.format(s1.isEmpty))

print('Peek: {}'.format(s1.peek()))

print('Size: {}'.format(s1.size()))

print('Pushing Elements in Stack')
for _ in range(5):
    s1.push(_)

s1.printStack()

print('Peek: {}'.format(s1.peek()))

print('Size: {}'.format(s1.size()))

print('Poping 3 Elements in Stack')
for _ in range(3):
    s1.pop()

s1.printStack()


# Evaluate postfix expression: Time O(n)
# Example: Infix (6 + 3 * 8 - 4) Equivalent Postfix (6 3 8 * + 4 -)
def evaluate_postfix_expression(exp):
    stack = Stack()
    try:
        for char in exp:
            if char.isdigit():
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        return int(float(stack.pop()))
    except TypeError:
        return 'Invalid Sequence'

print("Result of expression (638*+4-) : " + str(evaluate_postfix_expression("638*+4-")))
print("Result of expression (921*-8-4+) : " + str(evaluate_postfix_expression("921*-8-4+")))
print("Result of expression (921*-8--4+) : " + str(evaluate_postfix_expression("921*-8--4+")))
print("Result of expression (942+*6147/+*) : " + str(evaluate_postfix_expression("942+*6147/+*")))

