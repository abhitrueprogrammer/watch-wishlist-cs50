# Watch Wishlist 
#### Video Demo: https://youtu.be/IPq7j9Uu658
#### Description:

This is a sweet project, that allows you to create a watch wishlist of your very own! 

![homepage](/home/abhi/git/WW/homepage.png)

This project is hosted on flask 🐍  and uses sqlite3 for its Database. It can be run using

```bash
flask run
```

from the command line. 

It also uses the bootstrap🥾 framework for styling. This project derives from the week 9 project [finance](https://cs50.harvard.edu/x/2023/psets/9/finance/) as I figured it would allow me to show all the things(except C) I learnt so far.

The project directory is split into following folders and files:

1. .venv -> this has the virtual environment needed to make this project portable. Also with the python executable, this has the various libraries like flask, [Google Image Search](https://pypi.org/project/Google-Images-Search/)(GIS), [flask](https://pypi.org/project/Flask/), [flask cors](https://pypi.org/project/Flask-Cors/) and [werkzeug](https://pypi.org/project/Werkzeug/) packages and their dependencies to make sure the project works as intended

2. static -> This contains the static files for the websites. It has 2 folders:

   1. pics: It used to contain images back when I used to manually add images, but right now this is an empty folder since I use GIS to automatically fetch images from the web

   2. Styles: this contain the :dancer: css for my project. All in all, it has 3 files:

      1.  style.css 👗  : The major css file containing all the custom css needed to style up the project and make it look awesome.

      2. grid.css 🎩 : It contains code to create a beautiful custom homepage watch gallery.

      3. fireship-card.css: It contains cards directly copied over from https://github.com/fireship-io/224-animated-css-grid, but understood thoroughly. (I copied it over since this can be treated like the bootstrap framework)
   
   3. favicon.ico: Icon for the website. 
3. Templates -> It contains all the html files with jinja syntax having all the html pages constituting major part of the frontend. A few notable of these are:
   * template.html: Contains the html copied over to everypage, containing the navbar and few other boilerplate code. 
   * index.html: The homepage of the project, contains the html to display all the images that we got from the backend and make them clickable.
   * search.html: displays search results we got from backend, along with buttons  posting to add to cart or get the info. I added hidden files to submit the watchid, a mechanism I am particularly proud of.
   * register, login.html: Mostly contain code that I wrote in week 9, adjusted to suite this project's needs.

4. app.py: Brain 🧠 of the programme.  It contains most of the backend code. Here 's a brief summary for it: 
   1. First it imports all the nesessary libraries.
   2. Then it creates a flask app and sets it to allow cross website contents.
   3. It sets up the method to make cookies (taken from CS50 week 9)
   4. It sets up a base method that pushes if the user is logged in or not to template.html
   5. The index method gets random data from watch.db and sends it to index.html
   6. search, addcart and info method is pretty self explanatory
   7. cart method first checks if the method is post, and then deletes the entry from the db if that's the case, if not renders cart.html passing data to it. 
   8. login and register methods do what they say, and have been modified to use python's inbuilt sqlite library instead of cs50's
   9. Finally the creator.html template is rendered

5. Helper.py -> This file contains some helper functions for main app.py file. 

   1. The login required decorator is copied over from CS50 finance pset. 

   2. apology function makes it easier to render a error message incase something is wrong. The return is a plain html file with red styling for error message.

   3. then there's the code to update watch database with images of watches from google search, using GIS module. This code only runs when the user manually runs the helper.py file. Make sure to add in your Google API key and project CX in

      ```
      gis = GoogleImagesSearch('api_key', 'project_cx')
      ```

      go to  https://github.com/arrrlo/Google-Images-Search for more info

6. watch.db ->  It contains the following tables:

      1. watches: Contains a exhaustive list of watches for the demo project. More need to be added if this is used in production.
      1. users:  Contains the id, username and passwords of the users 
      1. cart: Contains a list of which user have which watch in its cart.

7. pseudocode.psu: Contains pseudocode I wrote in the 1st night to kickstart this project. Just there for sentimental perposes.

8. tips.md: Tips for someone who is in a place where I was and had no idea on how to start on their final project.

The early draft of this website had a category carousel instead of a search system, but it was discarded due to inviability of implementing in a one man project. The earliest draft of it was just a watch guide website, but it was also discarded as it was just a selection of html pages and nothing more. 

I wish this project brings joy to you.

Credits: David Melan and team behind CS50, fireship and my relations, friends included that motivated me to complete it. Also myself for dragging through the hard parts of this project and not giving up on the way.[![Obama Awards Obama a Medal](https://i.kym-cdn.com/entries/icons/mobile/000/030/329/cover1.jpg)](https://i.kym-cdn.com/entries/icons/original/000/030/329/cover1.jpg)

Signing off,

abhitruechamp