[![Build Status](https://travis-ci.org/alchemist2016/DjangoEcommerceProject.svg?branch=master)](https://travis-ci.org/alchemist2016/DjangoEcommerceProject)
## Django Final Project - Code Institute
---
# QuickMart
Hello from our online shop QuickMart. We have a range of products new and secondhand to meet any need. From household items to vehicles we have it all.
With our easy registration and payment form you can surf and shop on our website within minutes.
Feel free to look around and Thank you for your visit.


---
## Summary
* [Project Background](#project-background)
* [User Experience](#ux)
    * [User Stories](#user-stories)
    * [Five planes](#strategy)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Information Architecture](#information-architecture)
* [Technology used](#technology-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

---
## Project Background

Welcome to a Milestone 4 Project.

The main aim of this endevour is to provide CRUD Create, Read, Update and Delete functionality to a website.
Also the aim is to provide user with ability to manipulate cart and profile.

This project theme is based on a small online shop idea. Shop that will provide wide range of products.

There is much to say about this topic but my priorities were to present skills in creating a fully operational website connected to PostGress DB and deplayed on Heroku server and AWS S3.

 [Back to top](#summary)

---

## UX
### User Stories
#### From the users perspective I would like to be able to:

* **see products**
  - all products listed on main page

* **see cart**
  - access current products in cart and add, delete or edit them

* **Admin can Add New Members**
  - Adding new Members into DB 

* **User purchase a product**
  - user can fill out the form and purchase safely

* **User can Contact the Shop Admin**
  - user can write an email to the shop and short description 

#### As a shop, I would like to:
* **attract as many customers as possible**
Promoting wide range of products with a space to advertise

[Back to top](#summary)

### Strategy

**QuickMart** is designed to give oportunity and safety for customers who are interested in buying our products.

### Scope

When I was designing this website I was planing first from backend functionality then the mobile first front end and UI design. The customer can easily surf through the pages and find relevant information about the shop and it's products. Drop down menu in Nav Bar is available as well as burger menu on mobile sizes. All media queries are set to industry standars.

### Structure

User is greated at home page with a list of products with images and description and price. The user has nav bar with menu of all pages available as well as links in the footer. By clicking on a Nav Bar Logo user will be brought to home page.

Next page is Register page where user can get registered if he/she decides to purchase a product. At the Register form  user can use Submit button that will submit his form and create his account. Form is standard style.

Reseting password will affect the information stored in a database also.

If Login button is used user is brought to a new page where user can input his credentials and login into his/hers account.


Next page is Contact Us page where a user can fill out the form and send inquiries to Admin of the shop.

If user is member of the staff after login there is a link for Admin in navbar that takes user to Admin side of the shop app.
If logged in user can logout with a link in navbar.

Once a product has been chosen the user is then taken to Cart by following the link in navbar.

On the checkout page user can see all the products that were chosen and their cost calculated. Also he can fill out the payment form that will process payment through Stripe.

Footer is visible on any page and icons themselves are clickable and leading to clubs LinkedIn and GitHub pages.
All links are target_blank marked and will bring user to a new page opening thus keeping the integrity of the website.

#### Further description of buttons, icons and elements used is in the next section [Features](#existing-features).

### Wireframes

### Surface 
I am using throughout the website consistent coloring of Nav Bar and Footer as well as colouring of the forms, buttons, and fonts.


[Back to top](#summary)

---
## Features
### Existing Features
* Navigation bar
  -On the top of the Pages is Navigation Bar that is consisted of Logo which is wired to bring back to home page if clicked from any other page. Also on the right hand side is the drop down menu with burger effect and displaying links to all pages. On Mobile size the navbar contains Logo and on the left side a burger menu that links to all pages.

* Footer
  - Footer is always present on all sizes and displays social links that open in new tab.

* Products
  - Products page is consisting of list of products with their price, image, and description. Also there is a button to add that product to your cart.

* Register
  - The form for registration. All fields are required.

* Login/Logout
 - The user can login with the credentials supplied in registration form. After login user have option to logout.
    
* Profile
 - User can visit Profile page.

* Contact Us 
  - User can use contact form to send an email to Admin. On this page we have a form for the user if they decide to write to the club with their enquiries and questions. The form is connected to EmailJS API and emails to specific address all the queries. It will also print out Success in console window of dev tools.

* Password Reset
 - User can reset password on Login form

* Add User
  - Admin or members of staff can manipulate products and users and all other dutie through Django platform.


* Social icons
  - I have included 2 icons in the Footer that once clicked lead to a new tab with appropriate address and keeping the website always available to the user. For this I have used target=_blank attribute.

[Back to top](#summary)

### Future Features
  - For the future development I would certainly consider to use much more validation and backfeed to user if anything goes wrong. Also I could reduce the number of pages by introducing more action buttons in some of the forms. Further and more comprehensive testing is needed. UX should be improved with more appealing styling and advertising.
  - 
[Back to top](#summary)

---
## Information Architecture

### Database
- For the Backend I have used the PostGress database on Heroku Server [Heroku](https://www.heroku.com/). 


[Back to top](#summary)

---
## Technology used

* HTML5 & CCS3: 
* FontAwesome - 
 - https://fontawesome.com
 - Icons
 - Nav Bar
 - Footer
 - Social links
* JavaScript and jQuery:
    - Used for form validation, calendar gui, EmailJS API
    - https://jquery.com/
* EmailJS: API that is free and easy to apply.
    - https://www.emailjs.com/
* Python: Python is used as a programming language which is a back bone of the Backend and logical functionality
    - https://www.python.org/
* Django 
    - https://www.djangoproject.com
* Postgresql
    - https://www.heroku.com/postgres
* Github: Provides hosting for software development version control using Git and is used to store this projects repository.
    - https://github.com/
* Heroku: Cloud platform as a service supporting several programming languages and is used to deploy this project
    - https://www.heroku.com
* Amazon AWS: 
    - https://aws.amazon.com
[Back to top](#summary)

---

## Testing

### Testing section is located [here](https://github.com/alchemist2016/DjangoEcommerceProject/blob/master/testing.md)

### Validating code
HTML
 - code is validated through [W3 validator](https://validator.w3.org/).

CSS
 - code is validated through [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

JavaScript
 - code is validated through [JS Hint](https://jshint.com/).

Python
 - code is validated through [PEP8](http://pep8online.com/).

 [Back to top](#summary)

---

## Deployment
The project was written and developed in the Gitpod IDE.

A local repository was intialized using Github. Regular changes were commited to the local repository.

The process for deployment on Heroku was:

  -Create a new app in Heroku with "west-cork-trail-runners"
  - In the workspace, log into Heroku with command Line and the set of commands provided to create a connection between the application and Heroku.
  - Create a new Git repository and add the files, then associate the Heroku application and push to Heroku once the requirements.txt file and Procfile have been created.
  - Configuration variables had to be set in order to get the project running. These had to be set in both the Gitpod IDE and on Heroku. These included, PORT, IP and Mongo URL.
  - Open the app to test successful deployment.

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/alchemist2016/Milestone3.git` into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.  

Further help with cloning can be found on this GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## Some of the commands used in deployment
The app was written and developed on Gitpod and was regularly committed and pushed to Github and Heroku.
The following pip commands are necessary for the app to function properly. pip3 install django==1.11.29
pip3 freeze > requirements.txt
django-admin startproject file_name .
django-admin startapp app_name
python3 manage.py migrate
python3 manage.py runserver
python3 manage.py createsuperuser
pip3 install django_forms_bootstrap
pip3 install Pillow
pip3 install dj_database_url
pip3 install psycopg2
pip3 install django-storages
pip3 install boto3
pip3 install stripe
pip3 install gunicorn
Add all secret keys to heroku config vars and add DISABLE_COLLECTSTATIC and make it’s value 1
python3 manage.py collectstatic
Need to run this after any changes to static files in the IDE
Heroku required that some variables are set up in order to deploy the app. All secret keys and passwords used in the env.py file which is ignored by Github in the .gitignore file are stored in the config vars section of Heroku. In order to send the app to Heroku I first had to login into Heroku through the Gitpod IDE and then push all the commits to Heroku so any changes could be added to the app, on the last few pushes the Debug was set to False
To set up and install AWS I followed the instruction video on the Code Institutes training and the following steps were taken. If you don't have an amazon account you need to open one and select amazon web services (AWS) and then S3.
In AWS S3
Create Bucket
Unique name ie - vladimir-ecommerce Ireland Allow public access
Create
Open bucket Properties - staic website hosting Index.html
Error.html
Permissions Cors configuraton Add our arn keeping /*
IAM Create a group Name it close to buket name - neils ecommerce-group Next and create group
Greate policy Import managed polcy Choose S3 full policy Import Change string to a list [ ] The first item in the list is going to be our own ARN which we used earlier, but it has been closed in quotes The second item in the list again in quotes is going to be the same ARN This time we append a forward slash and an asterisk Review and name it in association with the bucket - vladimir-eccomerce-policy
Add policy to group Got to groups and select my group, goto permissions tap in group search for the policy we created and check the box and attach
Create user New user Name - vladimir-eccomerce-user Allow programatic access No keys or tags Download CSV file
Change our files Pip3 install django-storages Pip3 install boto3 Add this to settings.py above static_url
AWS_S3_OBJECT_PARAMETERS = {
'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
'CacheControl': 'max-age=94608000'
}
AWS_STORAGE_BUCKET_NAME = 'ecommerce'
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
Add AWS keys to env.py file using CSV information next Python3 manage.py collectstatic Yes to change warning
Custom_storages.py file
from django.conf import settings from storages.backends.s3boto3 import S3Boto3Storage class StaticStorage(S3Boto3Storage):
location = settings.STATICFILES_LOCATION class MediaStorage(S3Boto3Storage): location = settings.MEDIAFILES_LOCATION ADD these changes to staticfiles in settings.py
STATICFILES_LOCATION = 'static' STATICFILES_STORAGE = 'custom_storages.StaticStorage' And Python3 manage.py collectstatic
Do similar action for media To fix console errors In permissions - Cors configuration Copy the GET line and change it to HEAD to read font awesome CSS properly
[Back to top](#summary)

---

## Credits
### Content
+ All content was written by myself and by users. Many thanks to Code Institute Team of Tutors and their patientce and desire to help and guide.

### Acknowledgement
* Videos on [CodeInstitute](https://codeinstitute.net/).
* Thanks to my tutor Cormac and Stephen for feedback and ideas.
* w3 Schools.
* StackOverflow
*Background photos are used from [Unsplash](https://unsplash.com/) and from [Wikipedia](https://www.wikipedia.org)
* Big thanks to tutors in CodeInstitute.

#### This is for educational use.
[Back to top](#summary)