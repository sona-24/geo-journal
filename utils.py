from math import radians, cos, sin, asin, sqrt
import httpx

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two lat/lon pairs (in kilometers).
    """
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    # Radius of Earth in km
    r = 6371
    return c * r


async def get_location_from_ip() -> tuple[float, float] | None:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://ipapi.co/json/")
            data = response.json()
            return data["latitude"], data["longitude"]
    except Exception as e:
        print(f"❌ Failed to get location from IP: {e}")
        return None
