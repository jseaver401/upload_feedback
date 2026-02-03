#! /usr/bin/env python3
import os
import requests
import json

all_entries = []                                    #initialize list to eventually store json


data_path =  "/data/feedback"                       #create a path object to get the data
feedback_data = os.listdir(data_path)               #turn the data into a list

for file in feedback_data:
    if file.endswith('.txt'):                       #error check to make sure is .txt file
        full_path = os.path.join(data_path, file)   
        with open(full_path, 'r') as f:
            lines = f.readlines()
            #strip away whitespace from data fields
            entry = {"title": lines[0].strip(),"name": lines[1].strip(), "date": lines[2].strip(), "feedback": lines[3].strip()}
            #upload feedback using json as parameter
            response = requests.post("http://ip.address.to.upload.to/feedback/", json=entry)
            #raise error message in case of failure to upload (handle errors gracefully per instructions)
            if response.status_code == 201:
                print(f"Feedback successfully uploaded for {file}")
            else:
                print(f'Error uploading {file}: {response.status_code}')
