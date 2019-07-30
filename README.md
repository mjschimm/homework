# Homework Project

## Lagunitas Brewing Co.

*Disclaimer: The task we are asking you to perform is not going to provide us with any value. We are using this solely for purposes of evaluation job applicants.*

### Assignment
You have been given a Django web application that allows the user to create beer ratings. Please extend this to:

1. Allow the user to edit an existing rating. Each rating in the list at `/home/` should have a link that can be clicked on that takes the user to a page where the rating can be edited and changes saved. Editing should be cancelable.
2. Allow the user to delete a beer rating from the application.
3. Add a field to the beer rating that lets the user set the name of the brewery that created the beer being rated. This value is persisted in the database. This must also be editable. Note that Django has support for database schema changes, called "migrations".
4. Change the functionality of the "New" button so that it shows the beer rating creation form on the same page, instead of linking to a different page. The form should be hidden until the button is pressed.
5. The form for entering rating information looks pretty bad. Can you make it look better? (This is obviously subjective.)
 
Some of this will likely involve client-side coding.

You will be graded on the correctness and style of your solution, the cleanliness/readability of your code, and the computational complexity of your implementation.

This is open-book! Feel free to look up anything you want. The [Django documentation](https://docs.djangoproject.com/en/2.2/) is very thorough.

When you are done, please send an email to matthew.wyatt@lagunitas.com with instructions for retrieving and running your submission. Emailed submissions won't be accepted. (Please do not submit a PR to this repo - that would be sharing your hard work with the other applicants.)

### Installation instructions
The instructions assume you are running on a *nix OS, either OS X or Linux (they were only tested on OS X). If you are running on Windows, contact matthew.wyatt@lagunitas.com for support.

Prerequisites:

* Python 3.7.x
* Virtualenv (See [the installation page](https://virtualenv.pypa.io/en/stable/installation/) for instructions). (Technically, virtualenv isn't required, but this can help prevent library version conflicts with whatever other python software is on your system, and is strongly recommended.)

The app's current dependencies are specified in `requirements.txt`.

## Setup

These instructions should help you get started if you aren't familiar with `pip`. `virtualenv`, or Django. If you are, feel free to skip these.

(These are assumed to be run from within the directory where this file is.)

1. `virtualenv ./venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `./manage.py migrate`
5. `./manage.py runserver`
6. Navigate your browser to [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You should see a table with two beer ratings already present.

If you want to install any additional python libraries, please use the `pip` installed with virtualenv, and update the `requirements.txt` appropriately, so we can run the same code.

Feel free to include any third-party libraries (server-side or client-side) that you think would be useful to help with this problem. Make sure you include them in your solution properly, so that we can use them.

Have fun!


