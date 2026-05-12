import os
import streamlit as st
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("NVIDIA_API_KEY") or st.secrets["NVIDIA_API_KEY"]
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY,
    timeout=60
)

def get_llm_response(prompt):
    try:
        start_time = time.time()
        completion = client.chat.completions.create(
            model="mistralai/mistral-nemotron",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            top_p=0.7,
            max_tokens=4096
        )
        end_time = time.time()
        response_text = completion.choices[0].message.content
        usage = completion.usage
        return (
            response_text,
            round(end_time - start_time, 2),
            usage.prompt_tokens,
            usage.completion_tokens
        )
    except Exception as e:
        return f"Error: {str(e)}", 0, 0, 0