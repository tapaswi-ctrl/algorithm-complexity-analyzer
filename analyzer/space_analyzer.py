import ast


class SpaceAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.variables = 0
        self.lists = 0
        self.dictionaries = 0
        self.sets = 0
        self.recursive_functions = 0

    def visit_Assign(self, node):

        self.variables += len(node.targets)

        value = node.value

        # Direct list creation
        if isinstance(value, (ast.List, ast.ListComp)):
            self.lists += 1

        # List created using multiplication
        # Example: [0] * n
        elif isinstance(value, ast.BinOp):

            if isinstance(value.left, (ast.List, ast.ListComp)):
                self.lists += 1

        # Dictionary creation
        elif isinstance(value, (ast.Dict, ast.DictComp)):
            self.dictionaries += 1

        # Set creation
        elif isinstance(value, (ast.Set, ast.SetComp)):
            self.sets += 1

        self.generic_visit(node)

    def visit_FunctionDef(self, node):

        function_name = node.name

        # Check whether the function calls itself
        for child in ast.walk(node):

            if isinstance(child, ast.Call):

                if isinstance(child.func, ast.Name):

                    if child.func.id == function_name:
                        self.recursive_functions += 1
                        break

        self.generic_visit(node)


def analyze_space(code):

    try:

        tree = ast.parse(code)

        analyzer = SpaceAnalyzer()

        analyzer.visit(tree)

        # Recursive functions require call-stack space
        if analyzer.recursive_functions > 0:

            return {
                "complexity": "O(n)",
                "reason": "Recursive call stack detected"
            }

        # Input-sized data structures
        if (
            analyzer.lists > 0
            or analyzer.dictionaries > 0
            or analyzer.sets > 0
        ):

            return {
                "complexity": "O(n)",
                "reason": "Dynamic data structure detected"
            }

        return {
            "complexity": "O(1)",
            "reason": "No input-sized auxiliary data structure detected"
        }

    except SyntaxError as e:

        return {
            "error": f"Syntax Error: {e}"
        }