# @Author: ananayarora
# @Date:   2016-10-10T11:16:45+05:30
# @Last modified by:   ananayarora
# @Last modified time: 2016-10-10T11:21:33+05:30



import artikcloud
from artikcloud.rest import ApiException
import sys, getopt
import time, random, json
from pprint import pprint

# SDK reference for more details
# https://github.com/artikcloud/artikcloud-python
def main(argv):

	DEFAULT_CONFIG_PATH = 'config.json'

	with open(DEFAULT_CONFIG_PATH, 'r') as config_file:
		config = json.load(config_file)['metroBeaconSensor']
	print(config)

	# Configure Oauth2 access_token for the client application.  Here we have used
	# the device token for the configuration
	artikcloud.configuration = artikcloud.Configuration();
	artikcloud.configuration.access_token = config['deviceToken']

	# We create an instance of the Message API class which provides
	# the send_message() and get_last_normalized_messages() api call
	# for our example
	api_instance = artikcloud.MessagesApi()

	# Device_message - data that is sent to your device
	device_message = {}
	device_message['train1'] = random.randrange(0,200);

	# Set the 'device id' - value from your config.json file
	device_sdid = config['deviceId']

	# set your custom timestamp
	ts = time.time()

	# Construct a Message object for your request
	data = artikcloud.Message(device_message, device_sdid, ts)

	try:
	    # Debug Print oauth settings
	    pprint(artikcloud.configuration.auth_settings())

	    # Send Message
	    api_response = api_instance.send_message(data)
	    pprint(api_response)
	except ApiException as e:
	    print "Exception when calling MessagesApi->send_message: %s\n" % e


if __name__ == "__main__":
   main(sys.argv[1:])
