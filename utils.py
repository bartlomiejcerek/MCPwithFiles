import os


def init_openai() -> None:
    with open(".secrets/openai-key.txt", "r") as f:
        os.environ["OPENAI_API_KEY"] = f.read().strip()


def init_tavily() -> None:
    with open(".secrets/tavily-key.txt", "r") as f:
        os.environ["TAVILY_API_KEY"] = f.read().strip()


def init_langsmith() -> None:
    with open(".secrets/langchain-key.txt", "r") as f:
        os.environ["LANGCHAIN_API_KEY"] = f.read().strip()
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "mcp-experiments"
