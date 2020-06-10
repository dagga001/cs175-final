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
