from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("yaswanth-demo", json_response=True)

# Simple tool: add two numbers
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

# Simple tool: echo back a message
@mcp.tool()
def echo(text: str) -> str:
    """Echo the given text."""
    return f"You said: {text}"

def main():
    # Run the server over stdio (how MCP hosts talk to it)
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
