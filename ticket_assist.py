from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain_core.prompts import PromptTemplate


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

def template_of(question):
    template = """I want you to act like professional IT expert but give answer based on what i am looing for and guide me through daily IT problems. Like question I "dont Understand what that mean", "can you help me understand" without yapping and precise respond. I will peovide email or a problem to trouble shoot: {question}

    Answer: Let's think of the problem in fundamental level and high level first. 
    1. Explain possible reason behind it with bullet points precise explaination.
    2. Ask for possible follow question (Give multiple option). Then Ask related questions to more specify the service or to the problem has been reffered.
    3. Then, Suggest me a professional reply for the ticketing system update.  
    Make sure couple things for reply: Hi and full name of the person. Thanks the person for reaching out for first time respond. Sign my name Sohanur

    """
   

    prompt = PromptTemplate.from_template(template)

    chain = prompt | load_llm()

#     question = """HI, there,
# this is a follow-up to the advice Kevin Clancy gave (see below) about asking for your guidance to save the emails I'd like to keep before having my computer(s) wiped. 

# Many thanks, as always.
# Sister Remigia, Ask like questions, she want to backup all the emails in drive or related to it"""
    return chain.invoke({"question": question})



if __name__ == '__main__':
    template_of()