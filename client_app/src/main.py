if __name__=='__main__':
    #Default conexion: localhots in port 8000
    HOST="localhost"# input your IP
    PORT=8000
    
    sensor_one = Sensor("ESP-32-1500")    
    url=f'http://{HOST}:{PORT}/api/v1.0/sensors'    
    conn = Conexion(url)
    rand_tmp = [temp for temp in range(10,100+1)]
    
    while 1:
        try:
            sensor_one.temperature = choice(rand_tmp)
            sensor_one.timestamp =  int(time()*1000)
            #print(sensor_one.payload())
            conn.send(sensor_one.payload())
            sleep(2)
        except KeyboardInterrupt:
            input("\nPress any key then into to exit: ")
            sleep(2)
            break
        except Exception as e:
            print(f'INFO: Exit for exception, {e}')
            sleep(2)
            break