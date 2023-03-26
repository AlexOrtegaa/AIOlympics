"""
response.py
-----------------
Answers users question in the chat
"""

import openai
import os
openai.api_key = "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"        # YOUR API KEY GOES HERE (replace)

# In this function, you will accept a question from the user and generate a response using GPT
def answer_question(user_question):
    """
    Answer to questions in the chatbox
    :param user_question: Question of user in the chat
    """

    text_prompt = "Act as a professional economist, give a quick two minute summary of the most important stock trends of the company " + user_question
    text_prompt += ". Based on that suggest to buy or sell stocks of such company and write in a brief paragraph how such decision influences the stock trend of such company. Approximate expected earnings based on a 1,000 CAD dollars investment in a spredsheet for 1, 5 and 10 years."

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": text_prompt}],
    temperature=0.1,
    max_tokens=2000,
    top_p=0.95)

    response = response['choices'][0]['message']['content'].strip()

    # TODO: generate response based on user_question and return as a single string
    return response

# In this function, you will generate an image based on the user prompt
def generate_image(prompt):
    try:
        # TODO: generate one image which relates to prompt, and return the url of the image as a string
        return ""
    except:
        # DO NOT DELETE!
        return ""