# Heroku Demo

Distribute your app as a web application.

Docs: https://devcenter.heroku.com/articles/git

```bash
# develop app (code, virtual env)
conda create -n heroku python=3.6
pip install flask flask_sqlalchemy

# install gunicorn, create requirements.txt, create Procfile
pip install gunicorn
pip freeze > requirements.txt
echo 'web: gunicorn app:app' > Procfile

# create git remote (recommended)
git add -A
git commit -m ':tada: Initial'
git push origin master

# create heroku remote
heroku update
heroku login
heroku create dataviz-todo-list
heroku git:remote -a dataviz-todo-list
git remote -v  # note you mapped to two different remotes
git push heroku master

# test heroku app
heroku open
heroku info
heroku status
```


