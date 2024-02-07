class Conexion:
    def __init__(self,URL):
        self.url=URL

    def send(self,payload: dict):
        try:
            response = request.post(self.url,json=payload)
            print(f'INFO {response.status_code}: payload {payload}')
            attempt = 0
            while response.status_code >=400 and attempt < 5:                
                response = request.post(self.url,json=payload)
                print(f'INFO {response.status_code}: atteempt {attempt+1}')
                attempt+=1
                sleep(2)                
            
        
        except HTTPError as http_err:
            print(f'ERROR HTTP {http_err}')
        except Exception as e:
            print(f'ERROR {e}')