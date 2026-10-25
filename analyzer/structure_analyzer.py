import ast


class StructureAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.sequential_loops = 0
        self.nested_loops = 0
        self.max_depth = 0
        self.current_depth = 0

    def visit_For(self, node):

        self.current_depth += 1

        self.max_depth = max(
            self.max_depth,
            self.current_depth
        )

        # Check whether this loop directly contains
        # another loop.
        has_nested_loop = False

        for statement in node.body:

            if isinstance(statement, (ast.For, ast.While)):
                has_nested_loop = True

        if has_nested_loop:
            self.nested_loops += 1
        else:
            self.sequential_loops += 1

        self.generic_visit(node)

        self.current_depth -= 1

    def visit_While(self, node):

        self.current_depth += 1

        self.max_depth = max(
            self.max_depth,
            self.current_depth
        )

        has_nested_loop = False

        for statement in node.body:

            if isinstance(statement, (ast.For, ast.While)):
                has_nested_loop = True

        if has_nested_loop:
            self.nested_loops += 1
        else:
            self.sequential_loops += 1

        self.generic_visit(node)

        self.current_depth -= 1


def analyze_structure(code):

    try:

        tree = ast.parse(code)

        analyzer = StructureAnalyzer()

        analyzer.visit(tree)

        return {
            "sequential_loops": analyzer.sequential_loops,
            "nested_loops": analyzer.nested_loops,
            "max_depth": analyzer.max_depth
        }

    except SyntaxError as e:

        return {
            "error": f"Syntax Error: {e}"
        }