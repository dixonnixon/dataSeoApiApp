from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    target="newmouth.com",
    location_name="United States",
    language_name="English",
    intersecting_domains=[
        "dentaly.org",
        "health.com",
        "trysnow.com"
    ],
    filters=[
        ["metrics.organic.count", ">=", 50]
    ],
    limit=3
)
# POST /v3/dataforseo_labs/google/competitors_domain/live
# POST /v3/dataforseo_labs/bing/competitors_domain/live
response = client.post("/v3/dataforseo_labs/google/competitors_domain/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
