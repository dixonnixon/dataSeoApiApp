from client import RestClient
from dotenv import load_dotenv
import os

load_dotenv()

"""
    categories
    categories_aggregation
    locations
    search/live
"""



# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient(os.getenv('API_LOGIN'), os.getenv('API_PASSWORD'))
# GET /v3/business_data/business_listings/categories
response = client.get("/v3/business_data/business_listings/categories")

# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:

    #keysTask = [key for key in response["tasks"][0]]
    #print(keysTask)
    print(type(response))

    task = response["tasks"][0]

    print(task['path'])
    print(task['data'])
    print(task['result'][0])
    
    print("listing task keys\n\n"    )
    for key in task.keys():
        length = 'total length= ' + str(len(task[key])) if isinstance(task[key], list) else ''
        print(key, type(task[key]),  length)
        
    print("\n\n")


    print("listing response keys\n\n"    )
    for name in response:
        print(name, type(response[name]))
    #for task in response["tasks"]:
        #print(task)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
