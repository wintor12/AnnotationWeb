# AnnotationWeb

Install django

pip install django-jquery

Clone the project to local machine, cd to the project directory

sudo python manage.py runserver

Go to website: http://127.0.0.1:8000/annot/tong/  or  http://127.0.0.1:8000/annot/aaa/.  'tong' and 'aaa' are username, different user has
his own annotation website

If you want to add more user, or change labels, class, subclass, etc, go to admin page 

Admin page: http://127.0.0.1:8000/admin/  username: admin  password: password123456

If you want to modify label, subclass, class. For example, change 'Ending Summary'(Endings->Ending situation) to 'Summary', you have to modify both in 

1, database(admin page), in Labels table, change Ending Summary to Summary

2  in the code: annotation/annot/templates/annot/index.html, at the very end, change: "li class = 'label' Ending Summary li" to "li class = 'label' Summary li"

The labels, subclasses, classes must be same in database and in the index.html, otherwise may cause error

If you want to add stories, you can add directly from the admin database. An easier way is : 

python manage.py shell

Then write python code to save stories to database, you can reference here: https://docs.djangoproject.com/en/1.10/intro/tutorial02/
