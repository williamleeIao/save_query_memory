Install the code by putting the below command

```json
{
  "mcpServers": {
      "query_memory": {
			  "type": "stdio",
			  "command": "uvx",
			  "args": [
				  "--from",
				  "git+https://github.com/williamleeIao/save_query_memory.git",
				  "query_save_memories"
			  ],
        "env":{
          "OPENAI_API_KEY" : {replace with your OPENAI_API_KEY}
        }
  }
}

or 

#download from github
{
  "mcpServers": {
   "Query_Save_Memory":{
     "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\{your_folder_location}\\Documents\\PythonProject\\MCP_Memories",
        "run",
        "memories"
      ]
    }
  }
}