from mcp.server.fastmcp import FastMCP

# Create the MCP app
app = FastMCP("barts-mcp-server")


# Define a simple tool
@app.tool()
def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


@app.tool()
def subtract(a: int, b: int) -> int:
    """Return the subtraction of two numbers."""
    return a - b


if __name__ == "__main__":
    # Start HTTP server on port 8000
    app.run(transport="streamable-http")
