### MCP with Files

This is a demo of a functionality that allows agent to operate on files using MCP tools but:
- LLM does not need to load file into its context  
- MCP server does not need to pull file from any external location

### How To

- I used env like in the environment.yml it might contain a bit of random trash i installed on the way that is not relevant 
- Run mcp_server.py in the 1st terminal to expose 2 sample tools 
- You can create .secrets file and place you API keys there to that utils.py functions can load them or set them on your own
- Run demo notebook