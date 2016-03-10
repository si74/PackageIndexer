# PackageIndexer

## Run index.py to begin tcp server

`python index.py`

## Basic Tests

very simple (non-load) tests of TCP server

`python test_client.py`

very simple tests of models

`python tests.py`

###Design Rationale

I broke this down into two aspects. 

(1) Determining the data structure in which the packages and relevant details will be stored. 
I considered traditioanl 2 traditional graph approaches - the array of linked lists and the multi-dimensional array.
...But I wasn't happy with either one. So instead I decided to treat each package as a node with 'pointers' - aka a list of names of packages depending on this package as well as dependencies. The packageGraph class then aggregated the packages with a python dictionary. 
If I had more time, I would clean this code up a bit further. 

(2) Actually developing the socket server. 
Full honesty - I had little experience with this and engaged in substantial googling. I realized that I could use the python standard socket library and either have multiple threads for concurrent messages along with some sort of queue...or use the existing SocketServer which I decided to go with. I could have using an asynchronous SocketServer with threading mixins or go for something synchronous which I believe uses queues for concurrent situations. I decided to go with the synchronous option as I identified that I would be accessing a shared memory resource - the packageGraph. I could use locks and an asynchronous socketserver but would that have any advantage over my other option? I didn't think so at the time. Once I got the thing up and running, I added in a few functions to ensure that the messages were formatted correctly and pass back the appropriate response. 

Testing - 
There are a couple of things I did here. I wanted to test the actuall package and graph modules and then the socket server. I know that Python does have a proper unittest module which I could have utilized to have more formal unit tests but in the interest of time, I did some one-off assertions. 
And then of course - I used the appropriate testing harness provided. 