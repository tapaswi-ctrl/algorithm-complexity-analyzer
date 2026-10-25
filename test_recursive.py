from analyzer.recursive_analyzer import RecursiveComplexityAnalyzer


analyzer = RecursiveComplexityAnalyzer()


code = """
i = 1

while i < n:
    i *= 2
"""


result = analyzer.analyze(code)

print("Expression:", result["expression"])
print("Big-O:", result["big_o"])