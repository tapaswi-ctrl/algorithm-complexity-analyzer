from analyzer.complexity_expression import ComplexityExpression


expression = ComplexityExpression()

expression.add_term("log(n)")

print("Expression:", expression.simplify())