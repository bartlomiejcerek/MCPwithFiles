import base64
import os
import tempfile
from typing import Dict

from fastmcp import FastMCP

mcp = FastMCP(name="Barteks MCP Server")


@mcp.tool()
def add_numbers(a: int, b: int) -> Dict[str, int]:
    """
    Adds two integers and returns the result.

    Arguments:
      a: First integer.
      b: Second integer.

    Returns:
      A dict with the sum of a and b.
    """
    return {"sum": a + b}


@mcp.tool()
def read_first_line(file_as_b64: str) -> Dict[str, str]:
    """
    Accepts a base64‑encoded file content as a string.
    Saves it in the root folder, reads only the first line,
    and returns it alongside full length and file location.

    Arguments:
      file_as_b64: Base64‑encoded content of a text file.

    Returns:
      A dict with keys 'first_line', 'length', and 'path'.
    """
    tmp_path = "tmp.txt"

    print(file_as_b64)

    with open(tmp_path, "wb") as f:
        f.write(base64.b64decode(file_as_b64))

    with open(tmp_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        first_line = lines[0].rstrip("\n") if lines else ""
        length = len(lines)

    return {"first_line": first_line, "length": str(length), "path": tmp_path}


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
