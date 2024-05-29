import ast
import json
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def generate(topic, quantity):
    """
    Generates an exam in JSON format based on the provided topic.

    Args:
        topic (str): The topic of the exam.

    Returns:
        dict: The JSON representation of the exam.
    """
    template = """
    You will create a JSON file containing information about an exam on the following topic: {topic}. The exam will consist of {quantity} multiple-choice questions (3 incorrect options and one correct option). The structure of the JSON is an array where each element (each question of the exam) contains the following structure:

    [
        (insert opening curly brace here)
        "question": Here goes the question in a string,
        "answers": [
            (insert opening curly brace here)"answer": Here goes the first answer in a string, "correct": put "True" in quotes if it is correct and "False" if it is incorrect(insert closing curly brace here),
            (insert opening curly brace here)"answer": Here goes the second answer in a string, "correct": put "True" in quotes if it is correct and "False" if it is incorrect(insert closing curly brace here),
            (insert opening curly brace here)"answer": Here goes the third answer in a string, "correct": put "True" in quotes if it is correct and "False" if it is incorrect(insert closing curly brace here),
            (insert opening curly brace here)"answer": Here goes the fourth answer in a string, "correct": put "True" in quotes if it is correct and "False" if it is incorrect(insert closing curly brace here)
        ]
        (insert closing curly brace here)
    ]

    Generate the questions and answers based on the language in which the exam topic is stated. The only thing you will change based on the language is the language of the value of the key. If you cannot identify the language, assume the exam is in English.

    """

    prompt_template = PromptTemplate(input_variables=["topic", "quantity"], template=template)

    llm_google = ChatGoogleGenerativeAI(model="gemini-pro")
    chain = LLMChain(llm=llm_google, prompt=prompt_template)

    response = chain.invoke(input={
        "topic": topic,
        "quantity": quantity
    })

    output = response["text"].replace("```", "").replace("json", "").replace("JSON", "")
    print(output)
    return json.loads(output)

