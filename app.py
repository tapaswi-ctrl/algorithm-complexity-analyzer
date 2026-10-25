import streamlit as st

from analyzer.analyzer import AlgorithmAnalyzer


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Algorithm Complexity Analyzer",
    page_icon="🔍",
    layout="wide"
)


# -----------------------------
# TITLE
# -----------------------------

st.title("🔍 Algorithm Complexity Analyzer")

st.markdown(
    """
    Analyze Python code and estimate:

    **Time Complexity • Space Complexity • Operations • Big-O**
    """
)


# -----------------------------
# CREATE ANALYZER
# -----------------------------

analyzer = AlgorithmAnalyzer()


# -----------------------------
# CODE INPUT
# -----------------------------

st.subheader("📝 Enter Python Code")

code = st.text_area(
    "Python Code",
    height=300,
    placeholder="""for i in range(n):
    for j in range(n):
        print(i, j)"""
)


# -----------------------------
# ANALYZE BUTTON
# -----------------------------

if st.button("⚡ Analyze Code", type="primary"):

    if not code.strip():

        st.warning("Please enter some Python code.")

    else:

        with st.spinner("Analyzing code..."):

            result = analyzer.analyze(code)

        if "error" in result:

            st.error(result["error"])

        else:

            st.success("Analysis completed!")


            # -----------------------------
            # MAIN RESULTS
            # -----------------------------

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "⏱ Time Complexity",
                    result["time_complexity"]
                )

            with col2:

                st.metric(
                    "💾 Space Complexity",
                    result["space_complexity"]
                )

            with col3:

                st.metric(
                    "🔢 Estimated Operations",
                    result["operation_estimate"]
                )


            st.divider()


            # -----------------------------
            # CODE STRUCTURE
            # -----------------------------

            st.subheader("📊 Code Structure")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Loops",
                    result["loops"]
                )

            with col2:
                st.metric(
                    "Maximum Depth",
                    result["max_loop_depth"]
                )

            with col3:
                st.metric(
                    "Conditions",
                    result["conditions"]
                )

            with col4:
                st.metric(
                    "Function Calls",
                    result["function_calls"]
                )


            # -----------------------------
            # EXPLANATION
            # -----------------------------

            st.subheader("💡 Why this complexity?")

            st.info(result["explanation"])


            # -----------------------------
            # SPACE EXPLANATION
            # -----------------------------

            st.subheader("💾 Space Analysis")

            st.write(result["space_reason"])