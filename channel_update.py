#!/usr/bin/env python3
# channel_update.py

import requests, json

tabloIP = '192.168.2.171'
playlistIP = '127.0.0.1'

try:
	#get list of currently configured channels
	url = 'http://' + tabloIP + ':8885/guide/channels'
	channels = requests.get(url).json()
except Exception:
	print('Could not retrieve channel list from Tablo')
	exit()

f = open("playlist.m3u", "w")
f.write("#EXTM3U\n\n")

for ch in channels:
	ch_url = 'http://' + tabloIP + ':8885' + ch
	ch_info = requests.get(ch_url).json()
	channel = ch_info['channel']
	f.write('#EXTINF:-1 tvg-id="{}" tvg-chno="{}.{}",{}\nhttp://{}/watch/{}\n\n'.format(channel['call_sign'],channel['major'],channel['minor'],channel['call_sign'],playlistIP,ch_info['object_id']))

f.close()
