# -*- coding: utf-8 -*-

import base64
import urllib, urllib2
import json

oauth_consumer_key = ''     # your consumer key
oauth_consumer_secret = ''  # your consumer secret


def authenticate():
    url = 'https://api.twitter.com/oauth2/token'
    
    token_credential = urllib.quote(oauth_consumer_key) + ':' + urllib.quote(oauth_consumer_secret)
    credential = 'Basic ' + base64.b64encode(token_credential)

    value = {'grant_type': 'client_credentials'}
    data = urllib.urlencode(value)
    
    req = urllib2.Request(url)
    req.add_header('Authorization', credential)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8')

    response = urllib2.urlopen(req, data)
    json_response = json.loads(response.read())
    access_token = json_response['access_token']
    return access_token

        
def search(access_token):
    url = 'https://api.twitter.com/1.1/search/tweets.json'

    query = {'q': 'japan'}
    req = urllib2.Request(url+'?'+urllib.urlencode(query))
    req.add_header('Authorization', 'Bearer ' + access_token)

    response = urllib2.urlopen(req)
    json_response = json.loads(response.read())
    json_str = json.dumps(json_response)
    print json_str
  

if __name__ == '__main__':
    
    access_token = authenticate()

    # search api rate limit : 450
    for i in range(451):
        search(access_token)
        print i
