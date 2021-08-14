from collections import namedtuple

Color = namedtuple('Color', ['red', 'blue', 'green'])
color = Color(55, 155, 255)

print(color.red)