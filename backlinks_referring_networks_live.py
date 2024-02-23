from client import RestClient
# You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip?202197
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    target="backlinko.com",
    network_address_type="subnet",
    exclude_internal_backlinks=True,
    filters=["referring_domains", ">", 10],
    backlinks_filters=["dofollow", "=", True],
    order_by=["rank,desc"],
    limit=5
)
# POST /v3/backlinks/referring_networks/live
# the full list of possible parameters is available in documentation
response = client.post("/v3/backlinks/referring_networks/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))