from fastapi import APIRouter
import requests
from requests import Response
from constants import *
import json

router = APIRouter(tags=["openSenseMap"])

@router.get("/temperature")
async def get_temperature():
    sensor_ids = ['5eba5fbad46fb8001b799786', '5eb99cacd46fb8001b2ce04c', '5e60cf5557703e001bdae7f8']
    temperatures = [get_temp(id) for id in sensor_ids]
    return sum(temperatures) / len(temperatures)

def get_temp(sensor_id):
    response = requests.get(OPEN_SENSE_API_URL + sensor_id)
    data = response.json()
    for sensor in data.get('sensors'):
        if sensor.get('title') == "Temperatur":
            temperature = float(sensor.get('lastMeasurement')['value'])
    return temperature