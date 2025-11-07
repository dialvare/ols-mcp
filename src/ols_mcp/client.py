"""HTTP client for OLS API communication."""

import os
import httpx
from typing import Optional
from dotenv import load_dotenv

from .models import LLMRequest, LLMResponse

# Load environment variables from .env file
load_dotenv()


async def query_openshift_lightspeed(request: LLMRequest) -> LLMResponse:
    """Query the OpenShift LightSpeed API."""
    # Get configuration from environment
    api_url = os.getenv("OLS_API_URL", "http://localhost:8080")
    api_token = os.getenv("OLS_API_TOKEN")
    timeout = float(os.getenv("OLS_TIMEOUT", "30.0"))
    verify_ssl = os.getenv("OLS_VERIFY_SSL", "true").lower() == "true"

    # Build request URL
    url = f"{api_url.rstrip('/')}/v1/query"

    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    if api_token:
        headers["Authorization"] = f"Bearer {api_token}"

    # Prepare request data
    data = {
        "query": request.query
    }

    if request.conversation_id:
        data["conversation_id"] = request.conversation_id

    # Make HTTP request
    async with httpx.AsyncClient(timeout=timeout, verify=verify_ssl) as client:
        try:
            response = await client.post(url, json=data, headers=headers)
            response.raise_for_status()

            # Parse response
            response_data = response.json()

            # Return LLMResponse
            return LLMResponse(
                response=response_data.get("response", "No response received"),
                conversation_id=response_data.get("conversation_id", request.conversation_id)
            )

        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error {e.response.status_code}: {e.response.text}")
        except httpx.RequestError as e:
            raise Exception(f"Request error: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected error: {str(e)}")