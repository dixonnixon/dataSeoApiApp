from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
# get the task results by id
# GET /v3/merchant/amazon/sellers/task_get/advanced/$id
id = "06141103-2692-0309-1000-980b778b6d25"
response = client.get("/v3/merchant/amazon/sellers/task_get/advanced/" + id)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"])) 
