🧠 MCP + Ollama (Local LLM Tooling from Scratch)

This repository documents my hands-on exploration of Model Context Protocol (MCP) by building everything locally instead of relying on tutorials or paid tools.

The goal was simple:

Understand how an LLM can safely interact with external tools, files, and scripts — by building it myself.

❓ What is MCP (in simple words)

Large Language Models (LLMs) are powerful, but by default they:

cannot read local files

cannot run scripts

cannot execute commands

cannot safely access external tools

MCP (Model Context Protocol) provides a safe, structured bridge between:

an LLM

and external tools (Python functions, files, commands, APIs)

Instead of giving the LLM raw system access, MCP exposes explicit tools that the model can call.

🧩 What I built

Since ChatGPT local MCP support was not available on my account and Claude Desktop required a paid subscription, I built a fully local setup using Ollama.

Architecture
🧠 Ollama (local LLM: qwen2.5:7b)
        ↓
🔌 ollmcp (MCP client / bridge)
        ↓
🧰 MCP Server (Python – FastMCP)
        ↓
🛠 Custom Tools (add, echo, etc.)


The local LLM can now:

discover available tools

decide when to use them

call Python functions safely

receive structured responses

All running entirely on my machine.

⚙️ Tech Stack

Python

MCP (FastMCP)

Ollama

qwen2.5:7b

ollmcp (MCP client for Ollama)

🚀 Setup & Commands
1️⃣ Install Ollama
ollama --version

2️⃣ Pull a tool-capable model
ollama pull qwen2.5:7b


(Optional)

ollama run qwen2.5:7b

3️⃣ Create Python virtual environment
python -m venv .venv
.venv\Scripts\activate

4️⃣ Install MCP + CLI
pip install "mcp[cli]"

5️⃣ Create MCP Server (server.py)
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("yaswanth-demo", json_response=True)

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def echo(text: str) -> str:
    return f"You said: {text}"

if __name__ == "__main__":
    mcp.run(transport="stdio")

6️⃣ Run MCP Inspector (optional, for debugging)
mcp dev server.py

7️⃣ Install Ollama ↔ MCP bridge
pip install ollmcp

8️⃣ Connect local LLM to MCP server
ollmcp --mcp-server server.py --model qwen2.5:7b


You should now see:

qwen2.5/2-tools❯


And the model will have access to:

server.add

server.echo

🧪 Example Usage
Add 10 and 25 using the tool

Use the echo tool to repeat: MCP is working


The model automatically decides to call the correct MCP tool.