from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
# using this method you can get a list of completed tasks
# GET /v3/keywords_data/google_ads/search_volume/tasks_ready
# in addition to 'search_volume' you can also set other parameters
# the full list of possible parameters is available in documentation
response = client.get("/v3/keywords_data/google_ads/search_volume/tasks_ready")
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
