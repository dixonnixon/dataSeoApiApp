from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    target="dataforseo.com",
    location_name="United States",
    language_name="English",
    filters=[
        ["keyword_data.keyword_info.search_volume", ">", 10],
        "and", 
        [
            ["ranked_serp_element.serp_item.type", "<>", "paid"],
            "or",
            ["ranked_serp_element.serp_item.is_paid", "=", False]
        ]
    ],
    limit=3
)
# POST /v3/dataforseo_labs/google/ranked_keywords/live
# POST /v3/dataforseo_labs/bing/ranked_keywords/live
# POST /v3/dataforseo_labs/amazon/ranked_keywords/live
# for amazon use 'asin' instead of 'target'
response = client.post("/v3/dataforseo_labs/google/ranked_keywords/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
