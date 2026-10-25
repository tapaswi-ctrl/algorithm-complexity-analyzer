import ast


class OperationCounter:

    def count(self, code):

        try:
            tree = ast.parse(code)

            result = self.analyze_block(tree.body)

            return result

        except SyntaxError as e:

            return {
                "expression": "Unknown",
                "error": f"Syntax Error: {e}"
            }

    def analyze_block(self, statements):

        expressions = []

        for statement in statements:

            expression = self.analyze_node(statement)

            if expression != "1":
                expressions.append(expression)

        if not expressions:
            return "1"

        return self.simplify_addition(expressions)

    def analyze_node(self, node):

        # -------------------------
        # FOR LOOP
        # -------------------------

        if isinstance(node, ast.For):

            body_expression = self.analyze_block(
                node.body
            )

            if body_expression == "1":
                return "n"

            return self.multiply_by_n(
                body_expression
            )

        # -------------------------
        # WHILE LOOP
        # -------------------------

        if isinstance(node, ast.While):

            body_expression = self.analyze_block(
                node.body
            )

            if self.is_logarithmic(node):

                if body_expression == "1":
                    return "log(n)"

                return f"{body_expression} log(n)"

            if body_expression == "1":
                return "n"

            return self.multiply_by_n(
                body_expression
            )

        # -------------------------
        # IF
        # -------------------------

        if isinstance(node, ast.If):

            body = self.analyze_block(
                node.body
            )

            else_body = self.analyze_block(
                node.orelse
            )

            return self.simplify_addition(
                [body, else_body]
            )

        # -------------------------
        # BASIC OPERATION
        # -------------------------

        if isinstance(
            node,
            (
                ast.Assign,
                ast.AugAssign,
                ast.Expr,
                ast.Return
            )
        ):

            return "1"

        # -------------------------
        # OTHER
        # -------------------------

        return "1"

    def is_logarithmic(self, node):

        for statement in node.body:

            if isinstance(
                statement,
                ast.AugAssign
            ):

                if isinstance(
                    statement.op,
                    (ast.Mult, ast.Div)
                ):
                    return True

        return False

    def multiply_by_n(self, expression):

        if expression == "n":
            return "n²"

        if expression == "n²":
            return "n³"

        if expression == "log(n)":
            return "n log(n)"

        return f"n × {expression}"

    def simplify_addition(self, expressions):

        expressions = [
            e for e in expressions
            if e != "1"
        ]

        if not expressions:
            return "1"

        # Count identical terms
        counts = {}

        for expression in expressions:
            counts[expression] = (
                counts.get(expression, 0) + 1
            )

        parts = []

        for expression, count in counts.items():

            if count == 1:
                parts.append(expression)

            else:
                parts.append(
                    f"{count}{expression}"
                )

        return " + ".join(parts)