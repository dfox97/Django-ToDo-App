# Intro #
Using Django framework to make a ToDo app after following the cs50 lecture 3 course on python web development.

Front end in Html,CSS+Bootstrap , Backend server using Django

![mainToDo](https://user-images.githubusercontent.com/61083107/136714286-83598dbe-aa13-4960-b03a-705a3787d5a9.jpg)


# ToDo App ##
This time we added a models.py databse for the todo app

python manage.py makemigrations

After: 
when dealing with sessions
python manage.py migrate

python manage.py startapp tasks
python manage.py runserver



## New Findings/Learnings ##

Task.save()
Saved changes to an object performs an INSERT SQL statement behind the scenes. 
Django doesn’t hit the database until you explicitly call save().

Ajax,Async is important for real time updating.

Adding bootstrap css in main html file before calling css file

Creating databases using classes in the models.py file and forms.py

url patterns update/<str:pk>/ became useful to update/delete individual tasks (pk is a common name but this can be changed to anything), we can see pk be used in views.py functions

## Next Steps ## 
Modifying this program to impliment Ajax so deleted and update can be done asynchronously without redirecting to other pages.


