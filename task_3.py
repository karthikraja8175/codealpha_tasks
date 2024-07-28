import requests

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching IP information: {e}")
        return None

def get_geolocation(ip):
    ip_info = get_ip_info(ip)
    if ip_info and "loc" in ip_info:
        location = ip_info["loc"].split(',')
        return {
            "latitude": location[0],
            "longitude": location[1],
            "city": ip_info.get("city"),
            "region": ip_info.get("region"),
            "country": ip_info.get("country")
        }
    else:
        return {"error": "Unable to retrieve location data"}

ip_address = '55.25.25.0'  # Example IP address
geolocation = get_geolocation(ip_address)
print(geolocation)
