# algorithm-complexity-analyzer
# Algorithm Complexity Analyzer

A Python-based static code analysis tool that estimates the time complexity, space complexity, and operation count of Python algorithms using Abstract Syntax Tree (AST) analysis.

## Features

- **Time Complexity Analysis:** Estimates algorithm complexity in Big-O notation.
- **Space Complexity Analysis:** Estimates the additional space required by an algorithm.
- **Loop Analysis:** Identifies loops and maximum nesting depth.
- **Condition Analysis:** Counts conditional statements and function calls.
- **Operation Estimation:** Estimates the number of operations performed.
- **Automated Explanations:** Explains the estimated time and space complexity.
- **Interactive Web Interface:** Provides an easy-to-use interface with Streamlit.

## Technologies Used

- Python
- Abstract Syntax Tree (AST)
- Streamlit

## Project Structure

```text
algorithm-complexity-analyzer/
│
├── analyzer/
│   ├── analyzer.py
│   ├── ast_parser.py
│   ├── structure_analyzer.py
│   ├── complexity_expression.py
│   ├── complexity_engine.py
│   ├── recursive_analyzer.py
│   ├── space_analyzer.py
│   ├── operation_counter.py
│   └── explanation_generator.py
│
├── app.py
├── test_analyzer.py
├── test_complete.py
├── test_complexity.py
├── test_expression.py
├── test_operations.py
├── test_recursive.py
├── test_space.py
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tapaswi-ctrl/algorithm-complexity-analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd algorithm-complexity-analyzer
```

### 3. Install Dependencies

```bash
python -m pip install streamlit
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

## How to Use

1. Start the application using Streamlit.
2. Enter or paste Python code into the code input area.
3. Click **Analyze Code**.
4. View the estimated time complexity, space complexity, and operation count.
5. Review the code structure, loop information, and automatically generated explanations.

## Example

Input:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Expected time complexity: **O(n²)**

The nested loops result in approximately \(n \times n\) iterations.

*Note: Results depend on the analyzer's supported patterns and are estimates, not guaranteed exact complexity proofs.*

## Testing

The project includes Python test files for checking different analysis components.

Run an individual test using:

```bash
python test_analyzer.py
```

Replace `test_analyzer.py` with another test filename to run a different test.

## Limitations

- The analyzer uses static analysis and pattern-based estimation.
- Complex recursion and data-dependent execution may not be analyzed exactly.
- Results may vary for code structures that the analyzer does not explicitly support.

## Future Enhancements

- Improve recursive algorithm analysis.
- Support more complex control-flow patterns.
- Improve space complexity estimation.
- Add complexity-growth visualizations.
- Expand test coverage.

## Academic Project

Developed as a **Design and Analysis of Algorithms (DAA)** project to explore algorithm complexity estimation using Python and static code analysis.
