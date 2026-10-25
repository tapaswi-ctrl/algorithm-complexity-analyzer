from analyzer.structure_analyzer import analyze_structure


code = """
for i in range(n):
    for j in range(n):
        print(i, j)
"""


result = analyze_structure(code)

print(result)