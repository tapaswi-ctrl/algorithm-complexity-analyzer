from .ast_parser import analyze_code
from .recursive_analyzer import RecursiveComplexityAnalyzer
from .space_analyzer import analyze_space
from .operation_counter import OperationCounter
from .explanation_generater import generate_explanation

class AlgorithmAnalyzer:

    def __init__(self):

        self.time_analyzer = RecursiveComplexityAnalyzer()
        self.operation_counter = OperationCounter()

    def analyze(self, code):

        # --------------------------------
        # BASIC AST ANALYSIS
        # --------------------------------

        basic_analysis = analyze_code(code)

        if "error" in basic_analysis:
            return basic_analysis

        # --------------------------------
        # TIME COMPLEXITY
        # --------------------------------

        time_result = self.time_analyzer.analyze(code)

        if "error" in time_result:
            return time_result

        # --------------------------------
        # SPACE COMPLEXITY
        # --------------------------------

        space_result = analyze_space(code)

        if "error" in space_result:
            return space_result

        # --------------------------------
        # OPERATION ESTIMATE
        # --------------------------------

        operation_result = self.operation_counter.count(code)

        # --------------------------------
        # FINAL RESULT
        # --------------------------------

        explanation = generate_explanation({
    "time_complexity": time_result["big_o"],
    "loops": basic_analysis["loops"]
})

        return {

            "time_complexity":
                time_result["big_o"],

            "time_expression":
                time_result["expression"],

            "space_complexity":
                space_result["complexity"],

            "space_reason":
                space_result["reason"],

            "operation_estimate":
                operation_result,

            "explanation":
                explanation,

            "loops":
                basic_analysis["loops"],

            "max_loop_depth":
                basic_analysis["max_loop_depth"],

            "conditions":
                basic_analysis["conditions"],

            "function_calls":
                basic_analysis["function_calls"],

            "operations":
                basic_analysis["operations"],

            "logarithmic_loops":
                basic_analysis["logarithmic_loops"],

            "n_log_n_patterns":
                basic_analysis["n_log_n_patterns"]
        }