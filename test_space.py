from analyzer.space_analyzer import analyze_space


code = """
def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n - 1)
"""


result = analyze_space(code)

print("Space Complexity:")
print(result["complexity"])

print("Reason:")
print(result["reason"])