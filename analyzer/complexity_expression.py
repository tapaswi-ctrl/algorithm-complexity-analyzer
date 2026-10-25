class ComplexityExpression:

    def __init__(self):
        self.terms = []

    def add_term(self, term):
        self.terms.append(term)

    def multiply_term(self, term):
        self.terms.append(term)

    def simplify(self):

        if not self.terms:
            return "1"

        # Count occurrences of n
        n_count = self.terms.count("n")

        # Check for logarithmic term
        has_log = "log(n)" in self.terms

        if n_count == 0:

            if has_log:
                return "log(n)"

            return "1"

        if has_log:

            if n_count == 1:
                return "n log(n)"

            return f"n^{n_count} log(n)"

        if n_count == 1:
            return "n"

        return f"n^{n_count}"