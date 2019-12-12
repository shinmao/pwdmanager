# pwdmanager
This open source password manager is based on framework of **django-allauth**, then I add the secret management system to it.

## Please create the `settings.py` by yourself
Remember to start your app after creating the project. Don't show your key in `settings.py` to any other people. I put the sample file of `settings.py` in subdirectory, take a look at `.sample_setting.py` if you have no ideas about it.  
```python
...
# start app then you would get one key
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
...
# With this setting, you could only see email on the console
# Or you would need to set up the mail server
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## Core function of our pwdmanager
About the website you want to remember about:  
* View your stored secret in the mail  
* Edit your stored secret  
* Add new secret

## Reference
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
