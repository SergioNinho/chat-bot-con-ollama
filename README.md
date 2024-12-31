# chat-bot-con-ollama
Este proyecto es un chatbot AI llamado Checho, que responde preguntas de manera simple y contesta acorde al contexto proporcionado.
Requisitos
Python 3.7+

Bibliotecas:

langchain_community.llms

langchain_core.messages

langchain_core.prompts

Instalación
Clona este repositorio.

Instala las bibliotecas necesarias utilizando pip:

bash
pip install langchain_community langchain_core
Uso
Para ejecutar el chatbot, simplemente corre el script chat_ollama.py.

Ejemplo de uso
El chatbot se inicia y espera preguntas del usuario en un bucle hasta que se ingresa "adios". Aquí tienes un ejemplo de interacción:

you: ¿Cómo estás?
--------------------------------------------------
AI: Estoy aquí para ayudarte. ¿Qué necesitas saber?
Descripción del Código
Importaciones: Se importan las bibliotecas necesarias.

Inicialización de LLM: Se crea una instancia del modelo Ollama de langchain_community.

Plantilla de Prompts: Se define una plantilla de prompts con el contexto del sistema y el historial de chat.

Función chat:

Ejecuta un bucle donde se reciben preguntas del usuario.

Si la pregunta es "adios", el bucle se termina.

La respuesta del chatbot se obtiene y se imprime, y el historial de chat se actualiza.

Contribución
Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y abre un Pull Request con tus cambios.

Licencia
Este proyecto está bajo la licencia MIT.
