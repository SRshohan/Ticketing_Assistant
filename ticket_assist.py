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

    data = {}

    template1 = """I want you to act like professional IT expert and client service expert but give answer based on what i am looing for and guide me through daily IT problems or emails. Like question I "dont Understand what that mean", "can you help me understand" without yapping and precise respond. I will peovide email or a problem to trouble shoot: {question}

    Answer: Let's think of the problem in fundamental level and high level first. 
    1. Explain possible reason behind it with bullet points precise explaination. """
    
    template2 =""" I will feed some data and I want you act like expereience client service expert (Usually IT) .Ask for possible follow question (Give multiple option). Then Ask related questions to more specify the service or to the problem has been reffered. {question}"""
    
    template3 ="""  I will feed some data and I want you act like expereience client service expert (Usually IT). Then, Suggest me a professional reply for the ticketing system update. Hi and full name of the person. Thanks the person for reaching out for first time respond. Sign my name Sohanur. {question} """

    prompt1 = PromptTemplate.from_template(template1)
    prompt2 = PromptTemplate.from_template(template2)
    prompt3 = PromptTemplate.from_template(template3)

    chain1 = prompt1 | load_llm()
    chain2 = prompt2 | load_llm()
    chain3 = prompt3 | load_llm()

    c1 = chain1.invoke({"question": question})
    c2 = chain2.invoke({"question": question})
    c3 = chain3.invoke({"question": question})

    data["reason"] = c1
    data["options"] = c2
    data["response"] = c3


    return data




if __name__ == '__main__':
    question = "Hello, I have a second monitor that suddenly stopped connecting to my laptop and I'm struggling to figure out why. Could someone stop by this week to assist? I am available between 2-4PM today and between Noon and 3:30 PM tomorrow. Thank you! Best, Chloe"
    generated = template_of(question)
    print(generated['reason'])
    