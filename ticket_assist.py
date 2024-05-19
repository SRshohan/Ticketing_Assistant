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

    Answer: Let's think of the problem in fundamental level. Then, Suggest me a professional reply for the ticketing system update. Make sure couple things for reply:
    1. Hi and full name of the person. Thanks the person for reaching out for first time respond.
    "Ask a follow up questions if needs to", "Suggest appropriate reply based on the problem", "Rewrite my message"
    Sign my name Sohanur

    """
   

    prompt = PromptTemplate.from_template(template)

    chain = prompt | load_llm()

    question = """When ITS connected my computer to the printer in Marcom, I'm allowed to send a document for printing, but I cannot scan documents on the printer and send to my laptop. I will be in the office on Thursday. Thank you!!! """
    print(chain.invoke({"question": question}))

def main():
    # Print a message to indicate that the AI Writer is running and how to activate AI assist.
    print("AI Writer is running. Press 'Ctrl+Shift+A' to activate AI assist.")
    
    # Initialize an empty string to store the user input prompt.
    prompt = ""
    
    # Continuously listen for keyboard events.
    while True:
        event = keyboard.read_event()
        
        # Check if the backspace key is pressed to remove the last character from the prompt.
        if event.event_type == keyboard.KEY_DOWN and event.name == 'backspace':
            prompt = prompt[:-1]
        
        # Check if any key is pressed.
        elif event.event_type == keyboard.KEY_DOWN:
            # Append a space if the space key is pressed.
            if event.name == 'space':
                prompt += ' '
            # If the enter key is pressed, process the prompt using the AI for summarization.
            elif event.name == 'enter':
                print("Processing...")
                # Call the get_ai_response function with the 'summarize' task and print the summary.
                summary = get_ai_response(prompt, task="summarize")
                print("Summary:", summary)
                # Reset the prompt to an empty string for the next input.
                prompt = ""
            # Skip the shift and ctrl keys.
            elif event.name == 'shift' or event.name == 'ctrl':
                continue
            # Append the pressed key to the prompt.
            else:
                prompt += event.name
        
        # Check if the Ctrl+Shift+A combination is pressed to activate AI assist.
        if keyboard.is_pressed('ctrl+shift+a'):
            print("AI Assist Activated!")
            # Call the get_ai_response function without a specific task and print the AI-generated text.
            ai_text = get_ai_response(prompt)
            print("AI Generated Text:", ai_text)
            # Reset the prompt to an empty string for the next input.
            prompt = ""


if __name__ == '__main__':
    template_of()