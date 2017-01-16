
0rmuc0, a tool to add your favorite pets according to their color into world database :-D

# Introduction
This is a very simple program to add records into a sqlite DB. This is a demo project and it have been made in few hours, in way to demonstrate the way the developper can create a (very) simple webapp.


# Documentation

## Quick installation
Create a root directory and go inside:
```
mkdir ~/prj-0rmuc0/
cd ~/prj-0rmuc0/
```
Create a new virtual environment:
```
virtualenv 0rmuc0-python
```
Enable this new environment:
```
. 0rmuc0-python/bin/activate
```
Install flask:
```
pip install flask
```

Install sources:
```
git clone https://github.com/mrjk/0rmuc0-app.git 0rmuc0-app
```
You have setup everything correctly :-)

## Quick prod


## Quick dev
Instanciate the application database (It will destroy any existing data!):
```
run_init.sh
```
When database is initialized, just run the other script:
```
run_dev.sh
```
Then you can test the application on http://localhost:5000.

# Other

## Releases
There is a list of the releases:

 - 0.6:
	 - Better UI
	 - DB implementation
	 - User validation
	 - New documentation
 - 0.5:
	 - Initial version
	
## Legal
This code has been developed by mrjk, and everything is licensed under the MIT license.
