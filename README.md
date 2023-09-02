# FLM Analysis Chatbot
## By Damilola Esan

The FLM Analysis Chatbot is a project that utilizes the GPT-3.5-Turbo language model to provide conversational insights and analysis for a transportation dataset related to the First and last Mile Scheme (FLM) of the Lagos State Bus Reform Initiative (BRI) in Nigeria. The chatbot allows users to interact with the dataset through natural language conversations and obtain information about bus deployment, ridership, revenue, and other relevant metrics.


## Project Overview
The main components of the project include:

* **Data Processing:** The project involves loading, cleaning, and processing data from Excel sheets corresponding to different years (2021, 2022, and 2023). The cleaned dataset is used as input for the chatbot.

* **Chatbot Interface:** The core feature of the project is a web-based chat interface using Streamlit powered by the GPT-3.5-Turbo language model. Users can input questions or prompts related to the FLM dataset, and the chatbot responds with relevant analysis and insights.

## Getting Started

### Prerequisites
Python 3.x

OpenAI Python library

Pandas

Streamlit

LangChain

## Installation
* Clone this repository to your local machine.
* Install the required dependencies using the following command:
`pip install -r requirements.txt`

## Usage
Ensure you have the necessary Excel sheets containing the FLM dataset for the years 2021, 2022, and 2023.

1. Run the data processing script to clean and consolidate the dataset:
`data_clean.py`
* This script will create a cleaned dataset named "flm_data.csv."

2. Set your OpenAI API key as an environment variable:
`export OPENAI_API_KEY=your_api_key_here`
* Replace your_api_key_here with your actual OpenAI API key.

3. Run the Streamlit app to launch the chatbot interface:
`streamlit run FLM_Bot.py`
* Access the chatbot interface in your web browser.

## Example Conversations
User: "What was the ridership in April 2022?"

Chatbot: "In April 2022, the ridership was..."

User: "Can you compare revenue between 2021 and 2023?"

Chatbot: "Sure, the total revenue in 2021 was X, and in 2023, it was Y..."

## Customization
You can customize the chatbot's behavior, prompts, and responses by modifying the FLM_Bot.py script. Additionally, you can experiment with different GPT-3.5-Turbo settings to enhance the quality of responses.

## Acknowledgments
* This project utilizes the OpenAI GPT-3.5-Turbo language model.
* Special thanks to [Yeyu Huang](https://twitter.com/Yeyu2HUANG) for his informative articles about using LangChain for language model-powered applications.
* Also, thanks to the creators of Streamlit for providing an easy way to build interactive web applications.

For any questions or inquiries, please visit my **[website](https://www.bit.ly/damiesan)**.