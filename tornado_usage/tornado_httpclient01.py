from tornado import httpclient
from talospider.utils import get_random_user_agent


http_client = httpclient.HTTPClient()

try:
    headers = {"User-Agent":get_random_user_agent()}
    response = http_client.fetch("http://www.baidu.com/",headers=headers)
    print(response.body.decode())
except httpclient.HTTPError as e:
    # HTTPError is raised for non-200 responses; the response
    # can be found in e.response.
    print("Error: " + str(e))
except Exception as e:
    # Other errors are possible, such as IOError.
    print("Error: " + str(e))
http_client.close()