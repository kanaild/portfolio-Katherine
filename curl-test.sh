#!/bin/bash


curl --request GET kanaild.duckdns.org:5000/api/timeline_post

curl -X POST http://167.71.253.200:5000/api/timeline_post -d 'name=name&email=email&content=content'
