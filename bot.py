import os
import simplejson as json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

# python3.4 bot.py

consumer_key="6cuEp8qNCh0CYJQBr8VRkSoc9"
consumer_secret="OyJMdmhdxsjiIIzmz3ahDiJOIpNYgvJekxLg8VAtdIvupmsaZ9"
access_token="831260987961573378-CJMUdsPo6DXUfQ4uFSpmWkSK05LKyD6"
access_token_secret="NpSupcvuyCk8fYND5rnG16bebhtUtw9iQyKYVDwqsPsTF"

base_dir = 'images'
midi_dir = 'midi'

list = os.listdir("midi/") # dir is your directory path
number_files = len(list)
print(number_files)

n = 1 + number_files # counter for image downloaded


def midi(trackname, fullname):
    callpy = 'python midi.py %s %s' % (fullname, trackname)
    os.system(callpy)

class StdOutListener(StreamListener):

    def on_data(self, data):
        data = json.loads(data)
        global n
        if 'entities' in data and 'media' in data['entities']:
            for m in data['entities']['media']:
                tweetId = data.get('id_str')
                media_url = m['media_url']
                #print("Username: " + data['user']['screen_name'])
                #print(media_url)
                output_file = '%s/%s.jpg' % (base_dir, str(n).zfill(8))
                cmd = 'wget %s -O %s' % (media_url, output_file)
                #print(cmd)
                os.system(cmd)
                name = str(n).zfill(8)
                #print(name)
                imgfile = "images/" + name + ".jpg"
                print(imgfile)
                #make_midi(imgfile, "test.mid")
                tname = str(n).zfill(8)
                midi(tname, output_file)
                n += 1
            print('') # extra newline for formating
        #print("ID: " + tweetId)
        replyText = "@" + data['user']['screen_name'] + " http://45.55.73.14/bbcounter/midi/" + tname + ".mid"
        #api.update_with_media(filename, "here you go: @" + username)
        api.update_status(status=replyText, in_reply_to_status_id=tweetId)
        #print(data['user']['screen_name'] + " : " + data['text'] + "\n" + tweetId)    



        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    stream = Stream(auth, listener)
    stream.filter(track=['#image2midi'], async=True)