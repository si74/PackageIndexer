# PackageIndexer

## Setup
Make Sure you have vagrant and virtualbox installed:
(If you have homebrew cask and or on MacOSX for example):
`brew cask install virtualbox`
`brew cask install virtualbox-extension-pack`
`brew cask install vagrant`

Go to directory with vagrantfile and do the following: 
`vagrant up`
`vagrant ssh`

## Run index.py to begin tcp server
`cd var/www`
`python index.py`

## Basic Tests

very simple (non-load) tests of TCP server

`python test_client.py`

very simple tests of models

`python tests.py`

###Design Rationale

I broke this down into a few aspects. 

(1) Determining the data structure in which the packages and relevant details will be stored. 
I considered traditioanl 2 traditional graph approaches - the array of linked lists and the multi-dimensional array.
...But I wasn't happy with either one. So instead I decided to treat each package as a node with 'pointers' - aka a list of names of packages depending on this package as well as dependencies. The packageGraph class then aggregated the packages with a python dictionary. 
If I had more time, I would clean this code up a bit further. 

(2) Actually developing the socket server. 
Full honesty - I have no experience with this and engaged in substantial googling. I realized that I could use the python standard socket library and either have multiple threads for concurrent messages along with some sort of queue...or use the existing SocketServer which I decided to go with. 

Initial Thoughts: 

I could have using an asynchronous SocketServer with threading mixins or go for something synchronous which I believe uses queues for concurrent situations. I decided to go with the synchronous option initially as I identified that I would be accessing a shared memory resource - the packageGraph. I could use locks and an asynchronous socketserver but would that have any advantage over my other option? I didn't think so at the time. Once I got the thing up and running, I added in a few functions to ensure that the messages were formatted correctly and pass back the appropriate response. 

After Dealing with Concurrency Errors: 

Well, shit. I then used the test harness and realized that for synchronous socket server, I kept get incredibly annoying blocks with a larger number of concurrent requests. 

I then decided to try using a multi-threaded SocketServer from the python library. Unfortunately I repeatedly was getting i/o timeout errors. I tried setting the timeout value explicitly and doing a variety of other things but could not figure out what was happening for the life of me. 

At this point, I investigated further and saw that python had another standard way of implementing a socket server. I decided to then use asyncore and tweak some sample code. My simple unit tests with a single client seem to worse and I wasn't getting the same error as before. My feeble machine, however seemed to have trouble handling all the testing that was happening...

(3) Testing 
There are a couple of things I did here. I wanted to test the actuall package and graph modules and then the socket server. I know that Python does have a proper unittest module which I could have utilized to have more formal unit tests but in the interest of time, I did some one-off assertions. 
And then of course - I used the appropriate testing harness provided. It mostly seemed to work but my machine also seemed to struggle with a large volume of concurrent client requests. 

(4) Vagrant vs. Docker
Initial suggestion was to use docker containers. Unfortunately I am more experienced with Vagrant/Virtualbox so in the interest of time, I decided to use that. 
