from typing import List
from urllib import response
from fastapi import APIRouter, Response , status
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import json
from config.env import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from config.db import conn
from model.sensor import Sensor
from schemas.sensor import sensorEntity, sensorsEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_400_BAD_REQUEST

route = APIRouter()

@route.get('/api/v1.0/sensors',response_model=List[Sensor],tags=["sensors"])
async def find_all_sensors():
    return sensorsEntity(conn.local.sensor.find())

@route.get('/api/v1.0/sensors/{id}',response_model=Sensor,tags=["sensors"])
async def find_sensor(id:str):
    return sensorEntity(conn.local.sensor.find_one({"_id":ObjectId(id)}))

@route.post('/api/v1.0/sensors',status_code=HTTP_200_OK,tags=["sensors"])
async def send(sensor: Sensor):
    return sensorEntity(conn.local.sensor.insert_one(sensor.dict()))

@route.put('/api/v1.0/sensors/{id}',response_model=Sensor,tags=["sensors"])
def update_sensor(id:str, sensor:Sensor):
    conn.local.sensor.find_one_and_update(
        {"_id":ObjectId(id)},{"$set":dict(sensor)})    
    return sensorEntity(conn.local.sensor.find_one({"_id":ObjectId(id)}))

@route.delete('/api/v1.0/sensors',status_code=status.HTTP_204_NO_CONTENT,tags=["sensors"])
def delete_all_sensors():
    conn.local.sensor.delete_many({})    
    return Response(status_code=HTTP_204_NO_CONTENT)

@route.delete('/api/v1.0/sensors/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["sensors"])
def delete_sensor(id:str):
    sensorEntity(conn.local.sensor.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
