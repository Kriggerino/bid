from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_transformers.openai_functions import (
    create_metadata_tagger,
)
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


schema = {
    "properties": {
        "device":{
            "type": "string",
        }
    },
    "required": ["device"],
}

# Must be an OpenAI model that supports functions
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
prompt = ChatPromptTemplate.from_template(
    """Extract relevant information from the following text. Attach the devices mentioned to the metadata.

{input}
"""
)
document_transformer = create_metadata_tagger(metadata_schema=schema, llm=llm, prompt=prompt)