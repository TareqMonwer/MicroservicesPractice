import requests
import base64
from publisher_config import env


class HttpClient:
    def __init__(self):
      self.headers = {
        "Accept": "*/*",
        "Authorization": f"Basic {self._get_client_credential()}",
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded" 
      }
      self.payload = "grant_type=client_credentials"
      # self.token = self._get_token()

    def _get_client_credential(self):
      credential = "{0}:{1}".format(env.CLIENT_ID, env.CLIENT_SECRET)
      credential = base64.b64encode(credential.encode('utf-8'))
      return credential.decode('utf-8')
    
    def _get_token(self):
      api_url = env.AUTH_ISSUER_URL + '/token/'
      
      try:
        response = requests.request("POST", api_url, data=self.payload, headers=self.headers, verify=False)
        print(response)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        return response.json().get('access_token')
      except Exception as e:
        raise e

    def post(self, endpoint):
      self.headers['Authorization'] = f'Bearer {self._get_token()}'
      return requests.request("POST", endpoint, data=self.payload, headers=self.headers)
    
    def get(self, endpoint, **kwargs):
      token = self._get_token()
      self.headers['Authorization'] = f'Bearer {token}'
      print(">>>>>>>>>>>>>>>>>>>>")
      print(token)
      return requests.request("GET", endpoint, headers=self.headers, **kwargs)


http_client = HttpClient()
