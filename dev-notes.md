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
