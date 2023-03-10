import requests
import os

#--- https://docs.polygonscan.com/
def get(params: dict):
    x = "&".join([f"{k}={v}" for k,v in params.items()])
    url = f"{os.environ['EndpointURL']}?apikey={os.environ['API_KEY']}&{x}"
    # print(url)

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        error_msg = f"Error fetching data. Status code: {response.status_code}"
        raise requests.exceptions.HTTPError(error_msg, response=response)

# if __name__ == "__main__":
#     params = {
#        "module": "account",  
#        "action": "balance"
#     }
  
#     get(params)