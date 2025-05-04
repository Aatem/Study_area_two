import requests


class DelObject:
    response = None
    def del_by_id(self, id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{id}')
        self.response_after_del = requests.get(f'https://api.restful-api.dev/objects/{id}')
    
    def check_response_is_200(self):
        assert self.response.status_code == 200
    
    def check_response_is_404(self):
        assert self.response_after_del.status_code == 404