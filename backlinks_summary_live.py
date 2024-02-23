from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    target="explodingtopics.com",
    internal_list_limit=10,
    include_subdomains=True,
    backlinks_filters=["dofollow", "=", True],
    backlinks_status_type="all"
)
# POST /v3/backlinks/summary/live
response = client.post("/v3/backlinks/summary/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))