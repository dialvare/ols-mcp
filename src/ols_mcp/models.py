"""Pydantic models for OpenShift LightSpeed MCP server."""

from typing import Optional
from pydantic import BaseModel, Field


class LLMRequest(BaseModel):
    """Request model for OpenShift LightSpeed API."""

    query: str = Field(..., description="The query to send to OpenShift LightSpeed")
    conversation_id: Optional[str] = Field(None, description="Optional conversation ID for context")


class LLMResponse(BaseModel):
    """Response model from OpenShift LightSpeed API."""

    response: str = Field(..., description="The response from OpenShift LightSpeed")
    conversation_id: Optional[str] = Field(None, description="Conversation ID if provided")