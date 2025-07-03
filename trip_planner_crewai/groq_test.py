from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
print("api key: ",groq_api_key)
# client = Groq(api_key=groq_api_key) 
# try:
#     chat_completion = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[{
#                 "role": "user",
#                 "content": "Explain the importance of low latency LLMs",
#             }],
#         temperature=1,
#         max_completion_tokens=1024,
#         top_p=1,
#         stream=False,
#         #response_format={"type": "json_object"},
#         stop=None,
#     )

#     print(chat_completion.choices[0].message.content)
# except Exception as e:
#     print("Error:",e)    

from langchain_groq import ChatGroq
llm = ChatGroq( model="llama-3.3-70b-versatile",api_key = groq_api_key)
response = llm.invoke("explain the unity in diversity in the context of global cultures")
print(response.content)