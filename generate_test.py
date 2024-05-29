from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from IPython.display import display
from IPython.display import Markdown
import textwrap
import ast
import json

def to_markdown(text):
    text = text.replace('·', '*')
    return Markdown(textwrap.indent(text, ">", predicate=lambda _: True))

def generate(topic):
    template = """Vas a crear un json que va a contener informacion sobre un examen sobre el siguiente tema: {tema}. El examen va a constar de 3 preguntas de opcion multiple (3 opciones incorrectas y una correcta). La estructura del json es un array donde cada elemento (cada pregunta del examen) contiene la siguiente estructura:
    [
    (inserta aqui signo de llave de apertura)
    "pregunta" : Aqui va en un string la pregunta,
    "respuestas": [
        (inserta aqui signo de llave de apertura)"respuesta": Aqui va en un string la primera respuesta, "correcta": colocar entre comillas True si es correcta y False si es incorrecta(inserta aqui signo de llave de cierre),
        (inserta aqui signo de llave de apertura)"respuesta": Aqui va en un string la segunda respuesta, "correcta": colocar entre comillas True si es correcta y False si es incorrecta(inserta aqui signo de llave de cierre),
        (inserta aqui signo de llave de apertura)"respuesta": Aqui va en un string la tercera respuesta, "correcta": colocar entre comillas True si es correcta y False si es incorrecta(inserta aqui signo de llave de cierre),
        (inserta aqui signo de llave de apertura)"respuesta": Aqui va en un un string la cuarta respuesta, "correcta": colocar entre comillas True si es correcta y False si es incorrecta(inserta aqui signo de llave de cierre)
        ]
    (inserta aqui signo de llave de cierre)
    ]

    """

    prompt_template = PromptTemplate(input_variables=["tema"], template=template)

    llm_google = ChatGoogleGenerativeAI(model="gemini-pro")
    chain = LLMChain(llm=llm_google, prompt=prompt_template)

    respuesta = chain.invoke(input={
        "tema": topic
    })

    output = respuesta["text"].replace("```","")
    output = output.replace("json","")
    return json.loads(output)