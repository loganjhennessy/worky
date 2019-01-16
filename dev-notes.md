# 2018-01-11

Stopped halfway through implementing 'update'.

This is going to be challenging since I'll have to figure out what the user
has passed in and only update those fields.

To dos:
* ~Implement list~
* ~Implement delete~
* ~Implement retrieve~
* ~Implement unique name check on create~
* ~Implement update~
* ~Add a project scratch location ('scratch_dir')~
* ~Change 'directory' to 'repo'~
* ~Add a 'ticket' field~
* ~Add a 'branch' field~
* ~Update project printout to vertical instead of horizontal~
* Write bash scripts
* Write tests
* Write documentation
* Publish via PyPi
* Write a blog post introducing the app
* Write a blog post on using and testing a SQLite database
* Write a blog post on using and testing the Click library
* Setup configuration
* Make it possible to change the name
* Allow the nickname to be used to lookup a project

# 2018-01-09

To dos:
* ~Implement list~
* ~Implement delete~
* Implement retrieve
* Implement update
* Implement unique name check on create
* Setup configuration
* Write tests
* Write documentation
* Write bash scripts
* Publish via PyPi
* Write a blog post introducing the app
* Write a blog post on using and testing a SQLite database
* Write a blog post on using and testing the Click library

# 2018-01-07

Productive day. 

Create is complete. Still need delete, list, and update.

Now that I have more-or-less figured out the project layout and the
technologies I want to use, I'm really just left with the fun part of
implementing everything. And since I know what needs to be done and how to
do it, I can write a pretty descriptive TODO list that should remain valid
until I finish everything.

To dos:
* Implement list
* Implement delete
* Implement retrieve
* Implement update
* Implement unique name check on create
* Setup configuration
* Write tests
* Write documentation
* Write bash scripts
* Publish via PyPi
* Write a blog post introducing the app
* Write a blog post on using and testing a SQLite database
* Write a blog post on using and testing the Click library

# 2018-01-05

What columns do I need?

* id
* name
* nickname
* directory
* ide_exec

I need an id and name, obviously. Maybe a shortcut or nickname. A directory,
an IDE.

Nice. Got a database up and running, hard-coded for now, but it works!

# 2018-01-03

I now have a working `pywky` script that uses the `click` library.

Next step is to create a database that will store these projects.

Got sidetracked trying to figure out the best way to import configuration
values since I'll need those for connecting to the database. I'm still not too
sure about this so I think next time I'll spend a bit of time poking around and
looking for a good way to do this.

One more note for tomorrow. I should be using SQLite as opposed to PostgreSQL.
