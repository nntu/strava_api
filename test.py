
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = '86cefb828370764d41c194ab8328b77a95f1509f'
 
# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 10336109605 # Long | The identifier of the activity.
includeAllEfforts = True # Boolean | To include all segments efforts. (optional)

try: 
    # Get Activity
     
    thread = api_instance.get_activity_by_id(id, async_req=True)
    result = thread.get()
    pprint(result)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)