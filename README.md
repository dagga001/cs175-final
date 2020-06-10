# cs175-final

Project Requirements:

Python 3.8.3

How to set up:
1. Git clone repo
2. Create and start a virtual environment
3. virtualenv env --no-site-packages (run in command line)
4. source env/bin/activate (run in command line)
5. pip install -r requirements.txt (run in command line)
6. touch secrets.sh
7. obtain a secret key from MiniWebTool
8. add secret key to secrets.shh and add secrets.sh to .gitignore file
9. create postgres db and add credentials to settings.py

How to run:
1. run "python manage.py migrate" on command line
2. run "python manage.py createsuperuser"
3. run "python manage.py migrate"
4. run "python manage.py runserver"
5. open localhost:8000 on browser

Back-end how to run:
1. python yelp.py




Project Description:

To develop the Quest web application we needed to build a front-end interface that users could interact with as well as a backend web crawler that scrapes information from yelp. To do this we utilized Django web framework. Our group divided the work by splitting into front-end and back-end teams. Daniel Na and Justin Le led the front-end team while Devang Aggrawal, Usman Ahmed, and Luis Chelala developed the back-end program. 


Front-end: 

For the front-end development we utilized Bootstrap, a front-end framework. We decided to use Bootstrap because it is a very popular front-end framework that is fast and efficient. Also you do not need extensive html and css knowledge to use Bootstrap.

The first part was to integrate Bootstrap within our Django project. To install a Bootstrap template we first had to make a new “static” folder that contains all the necessary bootstrap template files such as “index.html”. After we need to go to the “settings.py” file to add a new path directory to the bootstrap template files that are located in the new “static” folder.  Using bootstrap we were able to implement a html/css template. The bootstrap template provided our web application with the ui interface and buttons. As of now the buttons within the menu navigation do not perform any functions. 

One of the biggest drawbacks was setting the proper paths for the css, javascript components within the “Index.html” file. Since the template consisted of many different buttons and components we had to search through the whole “Index.html” file and modify all the paths for those css and javascript components. To do this we had to add a path for each component to our “static” folder. 



Back-end: 

For the back-end development we utilized the Yelp fusion API to gather reviews for the particular restaurant. Once we obtained the API key, we were able to obtain the reviews as json objects. After we obtained the Json objects, we were able to write the data into a csv file. All this code was done in Python. 
The biggest drawback here is that the Yelp Fusion API only allows us to gather up to 3 reviews for each restaurant. This means that it isn’t as effective as we need it to be. To counter this, we need to implement a web crawler as well. This crawler will be able to extract all the reviews for the reviews. We hope to use Scrapy for this. 
Completed as of now: 
Yelp Fusion API review gathering
WIP:
Web Crawler to gather ALL reviews for the restaurant

