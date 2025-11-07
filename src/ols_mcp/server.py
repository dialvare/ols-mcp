"""Main MCP server implementation."""

import asyncio
import logging
from typing import Any, Sequence

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from .models import LLMRequest, LLMResponse
from .client import query_openshift_lightspeed

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server instance
server = Server("openshift-lightspeed-mcp")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="openshift-lightspeed",
            description="Query OpenShift LightSpeed for assistance with OpenShift, Kubernetes, and related technologies",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The question or query to send to OpenShift LightSpeed"
                    },
                    "conversation_id": {
                        "type": "string",
                        "description": "Optional conversation ID for maintaining context across queries"
                    }
                },
                "required": ["query"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> Sequence[TextContent]:
    """Execute a tool call."""
    if name != "openshift-lightspeed":
        raise ValueError(f"Unknown tool: {name}")

    try:
        # Extract arguments
        query = arguments.get("query")
        if not query:
            raise ValueError("Query is required")

        conversation_id = arguments.get("conversation_id")

        # Create request model
        request = LLMRequest(query=query, conversation_id=conversation_id)

        # Call OpenShift LightSpeed
        response = await query_openshift_lightspeed(request)

        # Return response
        return [
            TextContent(
                type="text",
                text=response.response
            )
        ]

    except Exception as e:
        logger.error(f"Error calling OpenShift LightSpeed: {e}")
        return [
            TextContent(
                type="text",
                text=f"Error: {str(e)}"
            )
        ]


async def main():
    """Main entry point for the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())