#
#   --------------------------------
#      reddit-new-post-notify  
#      notifier.py
#   -------------------------------- 
#
#        Author: Jacob Causon            
#                July 2014 
#
#   Licensed under the Apache License, Version 2.0 (the "License"); 
#    you may not use this file except in compliance with the License. 
#    You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software distributed
#    under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#    CONDITIONS OF ANY KIND, either express or implied. See the License for the
#    specific language governing permissions and limitations under the License.
#
#

import urllib.request
import re
import time

sub = "funny"       # Which sub to check
delay = 120         # How often to do check (in seconds)

# Function defining what to do when there is a new post
def on_new_post(post_name, post_time_utc):
    print("New post!")
    print(post_name)

### There is not need to touch anything below this point for standard usage ###
url = "http://www.reddit.com/r/"+sub+"/new.json?sort=new"
lastPost = 0
req = urllib.request.Request(url, headers={"User-Agent": "reddit-new-post-notifier"})
while True:
    data = urllib.request.urlopen(req)
    pattern = re.compile("\"title\": \"(?P<Name>[^\"]*)\".*\"created_utc\": (?P<Time>[0-9]+)")
    match = pattern.search(str(data.read()))
    if int(match.group("Time")) > lastPost:
        lastPost = int(match.group("Time"))
        on_new_post(match.group("Name"), lastPost)
    time.sleep(delay)

