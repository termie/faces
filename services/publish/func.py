import json
import sys
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-1e453968-bc05-11e0-9cf9-cbaf6932e4b8"
pnconfig.publish_key = "pub-025536de-c773-415a-9961-3d5c2bec5f26"
pnconfig.ssl = False
pn = PubNub(pnconfig)

def getPayload():
    return json.loads(sys.stdin.read())

def callback(message):
     print message

def main():
    # get payload
    payload = getPayload()
    message_json = json.loads(payload["Message"])

    # extract data
    bucket_name = message_json["Records"][0]["s3"]["bucket"]["name"]
    print "Bucket: " + bucket_name

    image_key = message_json["Records"][0]["s3"]["object"]["key"]
    print "Image Key: " + image_key

    url = "https://s3.amazonaws.com/"+bucket_name+"/" + image_key;

    message = {'url': url, 'id': image_key}
    message_json = json.dumps(message)

    print "message: " + str(message_json)

    pn.publish().channel(bucket_name).message([message_json]).use_post(True).sync()

if __name__ == "__main__":
    main()
