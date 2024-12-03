from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class LangChainHandler:
    def __init__(self, api_key):
        self.llm = OpenAI(api_key=api_key)

    def run_chain(self, prompt: str):
        """
        Запуск цепочки LangChain для обработки запроса.
        """
        template = "Ответь на следующий вопрос: {question}"
        prompt_template = PromptTemplate(input_variables=["question"], template=template)

        chain = prompt_template | self.llm
        response = chain.invoke({"question": prompt})
        return response
