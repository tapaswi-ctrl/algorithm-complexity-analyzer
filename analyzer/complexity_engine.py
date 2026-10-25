from .complexity_expression import ComplexityExpression


def analyze_complexity(analysis):

    # n log(n) pattern
    if analysis.get("n_log_n_patterns", 0) > 0:
        return "n log(n)"

    # logarithmic loop
    if analysis.get("logarithmic_loops", 0) > 0:
        return "log(n)"

    # no loops
    if analysis["loops"] == 0:
        return "1"

    # nested loops
    depth = analysis["max_loop_depth"]

    expression = ComplexityExpression()

    for _ in range(depth):
        expression.add_term("n")

    return expression.simplify()


def get_big_o(expression):

    if expression == "1":
        return "O(1)"

    if expression == "n":
        return "O(n)"

    if expression == "n^2":
        return "O(n²)"

    if expression == "n^3":
        return "O(n³)"

    if expression == "log(n)":
        return "O(log n)"

    if expression == "n log(n)":
        return "O(n log n)"

    return f"O({expression})"