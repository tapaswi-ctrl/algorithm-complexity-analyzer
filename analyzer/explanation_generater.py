def generate_explanation(result):

    time_complexity = result["time_complexity"]

    if time_complexity == "O(1)":

        return (
            "The code performs a constant amount of work "
            "that does not depend on the input size n."
        )

    if time_complexity == "O(log n)":

        return (
            "The loop grows or reduces the problem size "
            "multiplicatively. Therefore, the number of "
            "iterations grows logarithmically with n."
        )

    if time_complexity == "O(n)":

        loops = result["loops"]

        if loops > 1:
            return (
                "The code contains sequential linear operations. "
                "Their costs add together, but constant factors "
                "are ignored in Big-O notation. Therefore, "
                "the overall complexity is O(n)."
            )

        return (
            "The main loop performs approximately n iterations. "
            "Therefore, the running time grows linearly with "
            "the input size."
        )

    if time_complexity == "O(n log n)":

        return (
            "A linear loop contains a logarithmic operation. "
            "The outer part contributes n iterations and the "
            "inner part contributes log(n) iterations. "
            "Therefore, T(n) = n × log(n), giving O(n log n)."
        )

    if time_complexity == "O(n²)":

        return (
            "The code contains nested loops. The outer loop "
            "runs approximately n times and the inner loop "
            "runs approximately n times for each outer "
            "iteration. Therefore, T(n) = n × n = n², "
            "giving O(n²)."
        )

    if time_complexity == "O(n³)":

        return (
            "The code contains three levels of nested loops. "
            "Each level contributes approximately n iterations, "
            "giving T(n) = n × n × n = n³. Therefore, "
            "the time complexity is O(n³)."
        )

    return (
        f"The analyzer estimates the time complexity as "
        f"{time_complexity}."
    )