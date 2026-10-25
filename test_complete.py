from analyzer.analyzer import AlgorithmAnalyzer


code = """
for i in range(n):
    for j in range(n):
        print(i, j)
"""


analyzer = AlgorithmAnalyzer()

result = analyzer.analyze(code)


print()
print("==============================")
print("     ALGORITHM ANALYSIS")
print("==============================")

print()

print("Time Complexity  :", result["time_complexity"])
print("Space Complexity :", result["space_complexity"])
print("Estimated Ops    :", result["operation_estimate"])

print()

print("Time Expression  :", result["time_expression"])
print("Loops            :", result["loops"])
print("Maximum Depth    :", result["max_loop_depth"])
print("Conditions       :", result["conditions"])
print("Function Calls   :", result["function_calls"])

print()

print("Space Analysis:")
print(result["space_reason"])

print("==============================")
print()
print("Explanation:")
print(result["explanation"])