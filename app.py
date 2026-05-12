import streamlit as st
import pandas as pd
from optimizer import optimize_prompt
from llm_api import get_llm_response
from formatter import format_response

st.set_page_config(layout="wide")
st.title("Low-Bandwidth AI Learning Assistant")

user_input = st.text_input("Enter your question:")
mode = st.selectbox("Select Mode", ["Normal", "ELI10", "ELI5"])
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        optimized_prompt = optimize_prompt(user_input, mode)
        raw_response, time_taken, in_tokens, out_tokens = get_llm_response(optimized_prompt)
        final_response = format_response(raw_response)
        st.subheader("Response:")
        st.write(final_response)
        st.subheader("Metrics:")
        data = {
            "Metric": [
                "Input prompt length (chars)",
                "Optimized prompt length (chars)",
                "Input tokens",
                "Output tokens",
                "Response time (seconds)"
            ],
            "Value": [
                len(user_input),
                len(optimized_prompt),
                in_tokens,
                out_tokens,
                time_taken
            ]
        }
        df = pd.DataFrame(data)
        st.table(df)  

st.markdown("---")
st.markdown("""<div style='text-align: center; padding: 10px;'><p>Alby Jacob Martin</p><p><a href="https://github.com/albyjacobmartin" target="_blank">GitHub</a> |<a href="https://linkedin.com/in/albyjacobmartin" target="_blank">LinkedIn</a></p></div>""",
    unsafe_allow_html=True
)