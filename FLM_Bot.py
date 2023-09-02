import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent, create_csv_agent
from streamlit_chat import message
import os
import time
import random
from openai.error import RateLimitError
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if 'prompts' not in st.session_state:
    st.session_state.prompts = []
if 'responses' not in st.session_state:
    st.session_state.responses = []


def make_request_with_retry(api_call, max_retries=5):
    for i in range(max_retries):
        try:
            return api_call()
        except RateLimitError:
            wait_time = (2 ** i) + random.random()
            time.sleep(wait_time)
    raise Exception("Still hitting rate limit after max retries")


def send_click():
    if st.session_state.user != '':
        context = ("""
                    Context: The operator column contains 
                    'Niche', 'Progress', 'Yabeez', 'Rolek Allied', 'Tonleez',
                    'Shamid', 'Cape Trust', 'Double Infinity', 'Iroko Awe', 'UMD',
                    'UMD X30L', 'Labram', 'Progress X30L', 'Cape Trust X30L', 'LAMP',
                    'Galaxy Pharma', 'Jara Basket', 'Jara Basket X30L',
                    'Apec  Integrated', 'Apec  X30L', 'Interbrass', 'Scintilla', 'Iru',
                    'Safe Trip', 'Safe Trip X30L', 'Ruale', 'Mutakore', 'ACOMORAN',
                    'Elizabeth Mak X30L', 'ET Transport X30L', 'Ollykumar X30L',
                    'Speed Ex X30L', 'Ura - Ane X30L', 'GVJ X30L', 'Dovetop X30L',
                    'IBB X30L', 'Global kay X30L', 'Mubak Trust',
                    'City Cruise X30L', 'Global Kay X30L', 'Jafoson X30L'.
                    Also note that the columns in the dataset include 'Date', 'Month',
                    'Day ', 'Week Category', 'Route', 'Operator', 'Zone', 'Ridership',
                    'Revenue', 'Bus Deployed ', 'Actual Round Trips', 'Year'.
                    Please be precise with dates like month and year.
                    """)
        prompt = f"{context}\nUser: {st.session_state.user}"

        def run_agent():
            return agent.run(prompt)

        response = make_request_with_retry(run_agent)
        st.session_state.prompts.append(prompt)
        st.session_state.responses.append(response)


st.title(':blue[FLM Analysis Chatbot] 📊')

df = pd.read_csv("flm_data.csv")

st.dataframe(df.sample(5))

agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k"),
    df, openai_api_key=OPENAI_API_KEY,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

st.text_input("Ask Something:", key="user")
st.button("Send", on_click=send_click)

if st.session_state.prompts:
    for i in range(len(st.session_state.responses) - 1, -1, -1):
        message(st.session_state.responses[i], key=str(i), seed='Milo')
        user_input = st.session_state.prompts[i].split("User: ")[-1]
        message(user_input, is_user=True, key=str(i) + '_user', seed=83)
