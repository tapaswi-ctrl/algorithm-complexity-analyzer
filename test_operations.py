from analyzer.operation_counter import OperationCounter


counter = OperationCounter()


code = """
for i in range(n):

    j = 1

    while j < n:
        j *= 2
"""


result = counter.count(code)

print("Estimated Operations:")
print(result)