from client import RestClient
from dotenv import load_dotenv
import os
import json

load_dotenv()
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient(os.getenv('API_LOGIN'), os.getenv('API_PASSWORD'))
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    categories=[
        "pizza_restaurant"
    ],
    description="pizza",
    title="pizza",
    is_claimed=True,
    location_coordinate="53.476225,-2.243572,10",
    initial_dataset_filters=[
        ["rating.value",">",3]
    ],
    internal_list_limit=10,
    limit=3
)
# POST /v3/business_data/business_listings/categories_aggregation/live
response = client.post("/v3/business_data/business_listings/categories_aggregation/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(json.dumps(response, indent=2))
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
