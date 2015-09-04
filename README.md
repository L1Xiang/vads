# vads

. Install python 3.4.3
. Install pip
. Install virtualenv
. Create a virtual env with python 3.4.3
    virtualenv -p /Library/Frameworks/Python.framework/Versions/3.4/bin/python3 ~/envtest
    source ~/envtest/bin/active
. Install all needed library via pip, all needed library is in requirements.txt
    pip install -r requirements.txt
. Migrate and run server
    python manage.py makemigrations
    python manage.py migration
    python manege.py runserver
. Goto http://localhost:8000/ and create user
