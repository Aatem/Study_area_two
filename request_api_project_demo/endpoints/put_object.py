import requests

class PutObgect:
    response = None
    def put_by_id(self, id, payload):
        self.response = requests.put(
            f'https://api.restful-api.dev/objects/{id}',
            json=payload)
        self.response_json = self.response.json()
    
    def check_response_name(self, name):
        assert self.response_json['name'] == name
    
    def check_response_is_200(self):
        assert self.response.status_code == 200