
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import os

load_dotenv()


def main() -> None:
    information = """
    Elon Musk is a South African-born entrepreneur, engineer, and investor widely recognized as one of the world's wealthiest individuals and a pioneering figure in modern technology. Born in 1971 in Pretoria, he immigrated to Canada and later the United States, earning degrees in economics and physics from the University of Pennsylvania. Musk built his early fortune during the dot-com boom, co-founding Zip2 and X.com (which later became PayPal). The successful sales of these companies provided the foundational capital for his later, highly ambitious ventures aimed at transforming global industries.
    
    Today, Musk leads several revolutionary companies pushing the boundaries of transport, aerospace, and artificial intelligence. He is the founder and CEO of SpaceX, the CEO and product architect of Tesla, and the founder of xAI, Neuralink, and The Boring Company. Beyond his engineering pursuits, Musk owns the social media platform X (formerly Twitter) and actively engages in global socio-political discourse. His ultimate long-term ambitions include securing a sustainable energy future for Earth and establishing a human colony on Mars to ensure the survival of consciousness.
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about him
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
        
    )

    llm = ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3.2:1b"), 
                     base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                     temperature=0.2,
                     reasoning=False)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
