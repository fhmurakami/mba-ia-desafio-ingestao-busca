from search import search_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.3)  # type: ignore
    chain = search_prompt | model

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    user_input = input("PERGUNTA: ")
    if user_input.lower() in {"sair", "exit", "quit"}:
        print("Encerrando o chat. Até mais!")
        return

    response = chain.invoke(user_input)
    print(f"RESPOSTA: {response.content}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Encerrando o chat. Até mais!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")