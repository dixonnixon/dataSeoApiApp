from random import Random
from client import RestClient
# You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip
client = RestClient("login", "password")

post_data = dict()
# simple way to get a result
post_data[len(post_data)] = dict(
    url="https://dataforseo.com/solutions/seo-software"
)
# POST /v3/on_page/content_parsing/live
# the full list of possible parameters is available in documentation
response = client.post("/v3/on_page/content_parsing/live", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
