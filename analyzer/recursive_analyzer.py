import ast


class Complexity:

    def __init__(self, n_power=0, log_power=0):
        self.n_power = n_power
        self.log_power = log_power

    def multiply(self, other):
        return Complexity(
            self.n_power + other.n_power,
            self.log_power + other.log_power
        )

    def add(self, other):
        # For Big-O addition, keep the dominant term.
        if self.n_power > other.n_power:
            return self

        if other.n_power > self.n_power:
            return other

        if self.log_power >= other.log_power:
            return self

        return other

    def to_expression(self):

        if self.n_power == 0 and self.log_power == 0:
            return "1"

        if self.n_power == 0:

            if self.log_power == 1:
                return "log(n)"

            return f"log(n)^{self.log_power}"

        if self.log_power == 0:

            if self.n_power == 1:
                return "n"

            return f"n^{self.n_power}"

        if self.n_power == 1 and self.log_power == 1:
            return "n log(n)"

        if self.n_power == 1:
            return f"n log(n)^{self.log_power}"

        if self.log_power == 1:
            return f"n^{self.n_power} log(n)"

        return f"n^{self.n_power} log(n)^{self.log_power}"

    def to_big_o(self):

        expression = self.to_expression()

        conversions = {
            "1": "O(1)",
            "n": "O(n)",
            "log(n)": "O(log n)",
            "n log(n)": "O(n log n)",
            "n^2": "O(n²)",
            "n^3": "O(n³)"
        }

        return conversions.get(
            expression,
            f"O({expression})"
        )


class RecursiveComplexityAnalyzer:

    def analyze(self, code):

        try:
            tree = ast.parse(code)

            result = self.analyze_block(tree.body)

            return {
                "expression": result.to_expression(),
                "big_o": result.to_big_o()
            }

        except SyntaxError as e:

            return {
                "error": f"Syntax Error: {e}"
            }

    def analyze_block(self, statements):

        result = Complexity()

        for statement in statements:

            statement_complexity = self.analyze_node(
                statement
            )

            result = result.add(statement_complexity)

        return result

    def analyze_node(self, node):

        # -----------------------------
        # CONSTANT OPERATIONS
        # -----------------------------

        if isinstance(
            node,
            (
                ast.Assign,
                ast.AnnAssign,
                ast.AugAssign,
                ast.Expr,
                ast.Return
            )
        ):
            return Complexity(0, 0)

        # -----------------------------
        # IF / ELSE
        # -----------------------------

        if isinstance(node, ast.If):

            body_complexity = self.analyze_block(
                node.body
            )

            else_complexity = self.analyze_block(
                node.orelse
            )

            return body_complexity.add(
                else_complexity
            )

        # -----------------------------
        # FOR LOOP
        # -----------------------------

        if isinstance(node, ast.For):

            body_complexity = self.analyze_block(
                node.body
            )

            loop_complexity = Complexity(1, 0)

            return loop_complexity.multiply(
                body_complexity
            )

        # -----------------------------
        # WHILE LOOP
        # -----------------------------

        if isinstance(node, ast.While):

            body_complexity = self.analyze_block(
                node.body
            )

            if self.is_logarithmic_while(node):

                loop_complexity = Complexity(0, 1)

            else:

                loop_complexity = Complexity(1, 0)

            return loop_complexity.multiply(
                body_complexity
            )

        # -----------------------------
        # FUNCTION DEFINITION
        # -----------------------------

        if isinstance(node, ast.FunctionDef):

            return self.analyze_block(
                node.body
            )

        # -----------------------------
        # DEFAULT
        # -----------------------------

        return Complexity(0, 0)

    def is_logarithmic_while(self, node):

        for statement in node.body:

            if isinstance(statement, ast.AugAssign):

                if isinstance(
                    statement.op,
                    (ast.Mult, ast.Div)
                ):
                    return True

        return False