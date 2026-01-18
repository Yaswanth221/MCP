# MCP + Ollama (Local LLM Tool Integration)

This repository demonstrates a **local setup of Model Context Protocol (MCP)** integrated with a **local LLM (Ollama)**.

The goal is to enable an LLM to safely interact with external tools (Python functions) without giving unrestricted system access.

---

## What is MCP

Model Context Protocol (MCP) is a structured way for an LLM to call **explicitly exposed tools** (functions, files, commands, APIs).

By default, LLMs:
- cannot access local files
- cannot run scripts
- cannot execute commands

MCP solves this by exposing **only approved tools** through a controlled interface.

---

## Architecture

Ollama (qwen2.5:7b)
↓
ollmcp (MCP client)
↓
MCP Server (Python / FastMCP)
↓
Custom Tools (add, echo, etc.)


Everything runs locally.

---

## Tech Stack

- Python
- MCP (FastMCP)
- Ollama
- qwen2.5:7b
- ollmcp

---

## Setup

### Pull model
```bash
ollama pull qwen2.5:7b

### Python environment

python -m venv .venv
.venv\Scripts\activate
pip install "mcp[cli]" ollmcp

Run MCP server

mcp dev server.py

Connect LLM to MCP

ollmcp --mcp-server server.py --model qwen2.5:7b
