# OpenShift LightSpeed MCP Server

## Project Overview
This is a Model Context Protocol (MCP) server that integrates OpenShift LightSpeed capabilities with Claude Code. It enables AI-powered OpenShift assistance, troubleshooting, and best practices directly within development workflows.

## Current Status
✅ **PRODUCTION READY** - MVP implementation 100% complete. All tests passed successfully!

## Architecture & Components

### Project Structure
```
ols-mcp/
├── pyproject.toml              # uv project configuration
├── .env.example               # Environment configuration template
├── README.md                  # User documentation
├── CLAUDE.md                  # Development notes (this file)
├── src/ols_mcp/
│   ├── __init__.py
│   ├── models.py              # Pydantic models for LLMRequest/LLMResponse
│   ├── client.py              # HTTP client for OLS API communication
│   └── server.py              # MCP server with stdio transport
└── agent_reports/mcp-plan.md  # Implementation plan
```

### Key Components
1. **MCP Server** (`server.py`): Implements the Model Context Protocol for Claude Code integration
2. **HTTP Client** (`client.py`): Handles communication with OpenShift LightSpeed API
3. **Data Models** (`models.py`): Pydantic models ensuring type safety and validation
4. **Configuration**: Environment-based configuration with sensible defaults

## Implementation Details

### Completed Features (All Steps 1-6)
- ✅ **Project Setup**: Modern Python project with `uv` and Python 3.12
- ✅ **Data Models**: Type-safe Pydantic models for request/response handling
- ✅ **MCP Integration**: Full MCP server implementation with `openshift-lightspeed` tool
- ✅ **HTTP Client**: Robust HTTP client with comprehensive error handling
- ✅ **Configuration Management**: Flexible environment-based configuration
- ✅ **Production Testing**: Live API integration with SSL configuration validation
- ✅ **Documentation**: Complete user and developer documentation

### Technical Implementation
- **Protocol**: Model Context Protocol (MCP) with stdio transport
- **HTTP Library**: `httpx` for async HTTP client functionality
- **Validation**: Pydantic v2 for runtime type checking and data validation
- **Environment**: Python 3.12+ with `uv` for modern dependency management
- **Error Handling**: Comprehensive error handling for network, auth, and timeout scenarios

## Development Usage

### Local Development
```bash
# Install dependencies
uv sync

# Configure environment (optional)
cp .env.example .env
# Edit .env with your OLS API details

# Run server for testing
uv run python -m ols_mcp.server
```

### Environment Configuration
Configuration can be provided via environment variables or a `.env` file:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OLS_API_URL` | OLS API endpoint | `http://localhost:8080` | No |
| `OLS_API_TOKEN` | Bearer token for authentication | None | Yes* |
| `OLS_TIMEOUT` | Request timeout in seconds | `30.0` | No |
| `OLS_VERIFY_SSL` | SSL certificate verification | `true` | No |

*Required for most production deployments

## Claude Code Integration 🔌

### Configuration Setup
Add to your Claude Code config file (`~/.config/claude-code/config.json`):

```json
{
  "mcpServers": {
    "openshift-lightspeed": {
      "command": "uv",
      "args": ["run", "python", "-m", "ols_mcp.server"],
      "cwd": "/path/to/your/ols-mcp",
      "env": {
        "OLS_API_URL": "https://your-ols-instance.com",
        "OLS_API_TOKEN": "your-token-here",
        "OLS_TIMEOUT": "30.0",
        "OLS_VERIFY_SSL": "true"
      }
    }
  }
}
```

### Integration Benefits
- **Seamless OpenShift Help**: Get expert guidance directly in Claude Code
- **Context-Aware Assistance**: Troubleshooting help tailored to your specific issues
- **Best Practices**: Receive OpenShift best practices and recommendations
- **Real-Time Support**: Live integration with OpenShift LightSpeed knowledge base

### Example Queries
Once integrated, users can ask:
- "Help me troubleshoot a pod that's failing to start"
- "How do I scale a deployment in OpenShift?"
- "My application is getting 503 errors, what should I check?"
- "Show me how to create a route for my service"

## Production Deployment 🚀

### Status: PRODUCTION READY ✅
The server has been thoroughly tested and is ready for production use.

### Testing Summary
- ✅ **Dependencies**: All dependencies install and resolve correctly
- ✅ **Server Startup**: MCP server starts and registers tools properly
- ✅ **API Integration**: Live OLS API communication verified
- ✅ **SSL Handling**: Both verified and self-signed certificate scenarios tested
- ✅ **Error Handling**: Network failures, timeouts, and auth errors handled gracefully
- ✅ **Configuration**: Environment-based configuration working as expected

### Deployment Considerations
1. **API Access**: Ensure Claude Code environment can reach your OLS API endpoint
2. **Authentication**: Use proper bearer tokens for production environments
3. **SSL Configuration**: Configure `OLS_VERIFY_SSL` appropriately for your environment
4. **Network Security**: Consider firewall rules and network policies
5. **Monitoring**: Monitor API usage and response times

## Development Notes

### Code Quality
- **Type Safety**: Full Pydantic v2 type checking and validation
- **Error Handling**: Comprehensive error scenarios covered
- **Modern Python**: Uses Python 3.12+ features and best practices
- **Dependency Management**: Modern `uv` for fast, reliable dependency resolution

### Future Enhancements
Potential areas for future development:
- Caching for frequently asked questions
- Metrics and telemetry collection
- Support for multiple OLS endpoints
- Advanced authentication methods (OAuth, mTLS)
- Rate limiting and request queuing

### Maintenance
- Dependencies are pinned for stability
- Configuration is externalized for flexibility
- Error messages are descriptive for troubleshooting
- Code is well-documented for maintainability

## Success Criteria ✅
All MVP success criteria have been met:
1. **✅ Functional MCP Server**: Responds to Claude Code requests
2. **✅ OpenShift Integration**: Successfully communicates with OLS API
3. **✅ Error Handling**: Graceful handling of various failure scenarios
4. **✅ Configuration**: Flexible environment-based configuration
5. **✅ Documentation**: Complete user and developer documentation
6. **✅ Testing**: Validated against live OLS API instance

**Ready for immediate production deployment and use! 🎉**