from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# simple way to set a task
post_data[len(post_data)] = dict(
    location_code=1023191,
    language_code="en",
    hotel_identifier="ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE"
)
# POST /v3/business_data/google/hotel_info/live/advanced
response = client.post("/v3/business_data/google/hotel_info/live/advanced", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))