import tempfile

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from openai import OpenAI

load_dotenv()

mcp = FastMCP("Memories")

#create client object
client = OpenAI()

#create vector_store_name
VECTOR_STORE_NAME = "MEMORIES"

#get or create vector store
def get_or_create_vector_store():
    stores = client.vector_stores.list()  # Get a the store list
    for store in stores:
        if store.name == VECTOR_STORE_NAME:
            return store
        
    return client.vector_stores.create(name = VECTOR_STORE_NAME)


@mcp.tool()
def save_memories(memory:str):
    """Save the memory in to the vector store"""
    vector_store = get_or_create_vector_store()
    #file inside the vector
    with tempfile.NamedTemporaryFile(mode = "w+",delete= False, suffix=".txt") as f:
        f.write(memory)
        f.flush()
        #upload the file in the store
        client.vector_stores.files.upload_and_poll(
            vector_store_id=vector_store.id,
            file = open(f.name,"rb")
        )
    return {"status":"saved","vector_store_id":vector_store.id}


@mcp.tool()
def query_memories(query:str):
    """Query memory using query string"""
    # get the vector_store
    vector_store = get_or_create_vector_store()
    results = client.vector_stores.search(
        vector_store_id=vector_store.id,
        query = query
    )
    #return results
    contents_result =[
        content.text
        for item in results.data
        for content in item.content
        if content.type == "text"
    ]

    return {"contents":contents_result}
