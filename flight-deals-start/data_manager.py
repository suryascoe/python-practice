import requests

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/e21222121c0fbfc2bbc2121212c92d49c212161bd84d7293c/flightDeals/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/e212c0121f1212bfc1bb2c22112121121c6bd84d7293c/flightDeals/users"
BEARER = "p01o9iu8y176tr54gt1#%&F517TfY&%16&"

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json",
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}", json=new_data, headers=headers)
            print(response.text)

    def get_customer_data(self):
        customer_endpoint = SHEETY_USER_ENDPOINT
        response = requests.get(url=customer_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
