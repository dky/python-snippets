colors = ['red', 'blue', 'orange', 'green', 'yellow']
# Taking colors and making them uppercase, traditional
"""
uppercase_colors = []
for color in colors:
    uppercase_colors.append(color.upper())

print(uppercase_colors)
"""
# list comprehension approach
"""
uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)
"""
# Taking a list of colors and only selecting "warm/bright" colors, traditional
"""
warm_colors = []
for color in colors:
    if color in ['red', 'orange', 'yellow']:
        warm_colors.append(color)

print(warm_colors)
"""
# list comprehension approach
warm_colors = [
    color for color in colors if color in ['red', 'orange', 'yellow']
]

print(warm_colors)
