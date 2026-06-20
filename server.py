#!/usr/bin/env python
#from mcp.server import Server
from mcp.server.fastmcp import FastMCP


# This is like the "business card" of our server
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "WeatherMCPServer/1.0"

# Create the server instance
mcpserver = FastMCP("weather-server")
