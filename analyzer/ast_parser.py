import ast


class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.loop_count = 0
        self.max_loop_depth = 0
        self.current_loop_depth = 0
        self.condition_count = 0
        self.operation_count = 0
        self.function_count = 0

        # Complexity pattern counters
        self.logarithmic_loops = 0
        self.n_log_n_patterns = 0

    def visit_For(self, node):

        self.loop_count += 1
        self.current_loop_depth += 1

        self.max_loop_depth = max(
            self.max_loop_depth,
            self.current_loop_depth
        )

        # Check whether this for-loop
        # contains a logarithmic while-loop.
        contains_log_loop = False

        for child in ast.walk(node):

            if isinstance(child, ast.While):

                for statement in child.body:

                    if isinstance(statement, ast.AugAssign):

                        if isinstance(
                            statement.op,
                            (ast.Mult, ast.Div)
                        ):
                            contains_log_loop = True

        if contains_log_loop:
            self.n_log_n_patterns += 1

        self.generic_visit(node)

        self.current_loop_depth -= 1

    def visit_While(self, node):

        self.loop_count += 1
        self.current_loop_depth += 1

        self.max_loop_depth = max(
            self.max_loop_depth,
            self.current_loop_depth
        )

        # Detect logarithmic loop:
        # i *= 2
        # i /= 2
        # i *= constant
        # i /= constant

        for statement in node.body:

            if isinstance(statement, ast.AugAssign):

                if isinstance(
                    statement.op,
                    (ast.Mult, ast.Div)
                ):
                    self.logarithmic_loops += 1

        self.generic_visit(node)

        self.current_loop_depth -= 1

    def visit_If(self, node):

        self.condition_count += 1
        self.generic_visit(node)

    def visit_Call(self, node):

        self.function_count += 1
        self.generic_visit(node)

    def visit_Assign(self, node):

        self.operation_count += 1
        self.generic_visit(node)

    def visit_AugAssign(self, node):

        self.operation_count += 1
        self.generic_visit(node)

    def visit_BinOp(self, node):

        self.operation_count += 1
        self.generic_visit(node)


def analyze_code(code):

    try:

        tree = ast.parse(code)

        analyzer = CodeAnalyzer()

        analyzer.visit(tree)

        return {
            "loops": analyzer.loop_count,
            "max_loop_depth": analyzer.max_loop_depth,
            "conditions": analyzer.condition_count,
            "function_calls": analyzer.function_count,
            "operations": analyzer.operation_count,
            "logarithmic_loops": analyzer.logarithmic_loops,
            "n_log_n_patterns": analyzer.n_log_n_patterns
        }

    except SyntaxError as e:

        return {
            "error": f"Syntax Error: {e}"
        }