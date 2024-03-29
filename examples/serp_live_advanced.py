from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# You can set only one task at a time
post_data[len(post_data)] = dict(
    language_code="en",
    location_code=2840,
    keyword="albert einstein"
)
# POST /v3/serp/google/organic/live/advanced
# in addition to 'google' and 'organic' you can also set other search engine and type parameters
# the full list of possible parameters is available in documentation
response = client.post("/v3/serp/google/organic/live/advanced", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
