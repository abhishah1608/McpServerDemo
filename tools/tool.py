from helper.api_helper import make_nws_request, format_alert
from server import mcpserver, NWS_API_BASE
from decorator.log_tool import log_tool

@mcpserver.tool()
@log_tool
async def get_alerts(state: str) -> str:
    """
    Get weather alerts for a US state.
    
    Args:
        state: Two-letter US state code (e.g. CA, NY, TX)
    """
    # Build the API URL
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    
    # Get the data
    data = await make_nws_request(url)
    
    # Handle the case where we get no data
    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."
    
    # Handle the case where there are no active alerts
    if not data["features"]:
        return "No active alerts for this state."
    
    # Format each alert and join them together
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)


@mcpserver.tool()
@log_tool
async def get_forecast(latitude: float, longitude: float) -> str:
    """
    Get weather forecast for a location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location  
    """
    # The National Weather Service API is a bit quirky
    # We need to first get the "grid point" for our coordinates
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)
    
    if not points_data:
        return "Unable to fetch forecast data for this location."
    
    # Now we can get the actual forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)
    
    if not forecast_data:
        return "Unable to fetch detailed forecast."
    
    # Format the forecast periods (we'll show the next 5)
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    
    for period in periods[:5]:  # Just the next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)
    
    return "\n---\n".join(forecasts)