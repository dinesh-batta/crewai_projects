from langchain_ollama import OllamaLLM 
model_list = ["gemma3:1b","llama3.2:1b","mistral:latest"]
llm = OllamaLLM(model=model_list[0])
response = llm.invoke("use of generative ai for automation in business. limit your response to 100 words")
print(response)