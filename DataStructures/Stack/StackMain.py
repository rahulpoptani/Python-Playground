from SpecialStack import SpecialStack

ss = SpecialStack()


ss.push(4)
ss.push(2)

ss.printStack()
print('Top Element: {}'.format(ss.peek()))

ss.push(1)

print('Min Element: {}'.format(ss.getMin()))

ss.pop()

ss.printStack()

print('Min Element: {}'.format(ss.getMin()))

