from analyzer.ast_parser import analyze_code
from analyzer.complexity_engine import analyze_complexity
from analyzer.complexity_engine import get_big_o


code = """
for i in range(n):

    j = 1

    while j < n:
        j *= 2
"""


analysis = analyze_code(code)

print("Analysis:")
print(analysis)

expression = analyze_complexity(analysis)

print("Complexity Expression:")
print(expression)

big_o = get_big_o(expression)

print("Time Complexity:")
print(big_o)