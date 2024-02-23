from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    title="vpn",
    description="vpn",
    order_by=["item.rating.value,asc"],
    filters=[
        ["item.rating.value",">",4]
    ],
    internal_list_limit=3,
    limit=3
)
# POST /v3/app_data/google/app_listings/search/live
# POST /v3/app_data/apple/app_listings/search/live
response = client.post("/v3/app_data/google/app_listings/search/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))