"""

OpenSenseMap Controller 

"""

from fastapi import APIRouter
import requests
from constants import OPEN_SENSE_API_URL

router = APIRouter(tags=["OpenSenseMap"])


@router.get("/temperature", description="Get average temperature of three sensors")
async def get_temperature():
    """
    Get temperature API
    """
    sensor_ids = [
        "5eba5fbad46fb8001b799786",
        "5eb99cacd46fb8001b2ce04c",
        "5e60cf5557703e001bdae7f8",
    ]
    temperatures = [get_temp(id) for id in sensor_ids]
    return {"Avg Temperature": round(sum(temperatures) / len(temperatures), 2)}


def get_temp(sensor_id):
    """
    Function to get temperature for each box
    """
    temperature = 0
    response = requests.get(OPEN_SENSE_API_URL + sensor_id, timeout=1000)
    data = response.json()
    for sensor in data.get("sensors"):
        if sensor.get("title") == "Temperatur":
            temperature = float(sensor.get("lastMeasurement")["value"])
    return temperature
