from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = Ollama(model = 'llama3')
chat_history = []
prompt_template = ChatPromptTemplate.from_messages(
    [(
        'system',
        """Eres un AI llamado checho, respondes preguntas de manera simple
        y ademas debes contestar de vuelta preguntas acordes al contexto""",
    ),
    MessagesPlaceholder(variable_name= 'chat_history'),
    ('human', '{input}'),
    ]
)
chain = prompt_template | llm
def chat():
    while True:
        pregunta = input("you: ")
        if pregunta == 'adios':
            return
        
        response = chain.invoke({"input": pregunta, "chat_history": chat_history})
        chat_history.append(HumanMessage(content = pregunta))
        chat_history.append(AIMessage(content = response))
        print('-'*50)
        print('AI: ' + response)

chat()

#usar con from ollama, chat sin menoria
# def chat_whit_ollama():
#     print('Bienvenido, mi nombre es checho, digita salir si quieres abandonar el chat')

#     while True:
#         user_inpot = input('tu: ')

#         if user_inpot.lower()== 'salir':
#             print('Hasta la proxima')
#             break

#         response = ollama.generate(model='llama3.2:3b', prompt= user_inpot)
#         print('Bot:', response['response'])


# chat_whit_ollama()

