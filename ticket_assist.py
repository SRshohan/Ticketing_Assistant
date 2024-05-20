from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain_core.prompts import PromptTemplate
import keyboard



passw = os.getenv('ENV', 'local')
load = f".env.{passw}"
load_dotenv(load)


def load_llm():
    llm = GoogleGenerativeAI(
        model="gemini-pro",
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    return llm

def template_of():
    template = """I want you to act like professional IT expert and guide me through daily IT problems. I dont Understand what that mean, can you help me understand without yapping and precise respond: {question}

    Answer: Let's think of the problem in fundamental level. Then, Suggest me a professional reply for the ticketing system update. Then Ask related questions to more specify the service. Make sure couple things for reply:
    1. Hi and full name of the person. Thanks the person for reaching out for first time respond.
    "Ask a follow up questions if needs to", "Suggest appropriate reply based on the problem", "Rewrite my message"
    Sign my name Sohanur

    """
   

    prompt = PromptTemplate.from_template(template)

    chain = prompt | load_llm()

    question = """HI, there,
this is a follow-up to the advice Kevin Clancy gave (see below) about asking for your guidance to save the emails I'd like to keep before having my computer(s) wiped. 

Many thanks, as always.
Sister Remigia, Ask like questions, she want to backup all the emails in drive or related to it"""
    print(chain.invoke({"question": question}))



if __name__ == '__main__':
    template_of()