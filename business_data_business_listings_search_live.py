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
        # "pizza_restaurant"
        "cafe"
    ],
    # description="піцца",
    # title="піца",
    is_claimed=True,
    # location_coordinate="50.476225,-2.243572,10",
    location_coordinate="50.908248,34.797201,100",
    order_by=["rating.value,desc"],
    filters=[
        ["rating.value",">",1],
        # 'and',
        # ["local_business_links.url","",""]
        # ["address","like","Sum"],
        "and",
        ['url','regex', 'coffe']
    ],
    limit=10
)
# POST /v3/business_data/business_listings/search/live
response = client.post("/v3/business_data/business_listings/search/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    # print(json.dumps(response, indent=2))
    print("result items len= ", len(response['tasks'][0]['result'][0]["items"]))
    for item in response['tasks'][0]['result'][0]["items"]:
    
        target = {
            "title": item["title"],
            "category": item["category"],
            "rating": item["rating"],
            "category_ids": item['category_ids'],
            "additional_categories":  item['additional_categories'],
            "cid":  item['cid'],
            "feature_id":  item['feature_id'],
            "address":  item['address'],
            "address_info":  item['address_info'],
            "place_id": item['place_id'],
            "phone": item['phone'],
            "url": item['url'],
            "domain": item['domain'],
            "logo": item['logo'],
            "snippet": item['snippet'],
            "latitude": item['latitude'],
            "longitude": item['longitude'],
            "is_claimed": item['is_claimed'],
            "local_business_links": item['local_business_links'],
            "contact_info": item['contact_info'],
            "check_url": item['check_url'],
            "last_updated_time": item['last_updated_time'],
        }
        print(json.dumps(target, indent=2))
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
