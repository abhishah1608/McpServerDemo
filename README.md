uv init <proj_name>
uv add mcp-cli
uv add mcp

add like this configuration in claude.configuration.json file:

"weatherForecast": {
    "command": "cmd",
    "args": [
      "/c",
      "uv",
      "--directory",
      "E:\\mcp_proj\\weather_forecast",
      "run",
      "python",
      "-u",
      "main.py"
    ]
  }
}
