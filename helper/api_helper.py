import httpx
from server import USER_AGENT
async def make_nws_request(url: str) -> dict:
    """
    Makes a request to the National Weather Service API.
    This is our universal way to talk to the weather API.
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            # If something goes wrong, we return an empty dict
            return {}

def format_alert(feature: dict) -> str:
    """
    Takes the messy weather alert data and makes it human-readable.
    This is where we clean up the data for Claude to understand.
    """
    props = feature.get("properties", {})
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}  
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions')}
"""