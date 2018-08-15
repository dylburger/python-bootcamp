## Installing Python 3 and software for the course

### Pre-requisities

Before reviewing this guide, make sure you've watched these lecture videos from the Udemy course:

* [Python 2 vs. Python 3](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/9373030?start=0)
* [Command Line Basics](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/9431354?start=0)

*We are not going to install Python 3 using Anaconda, which the course recommends*. Anaconda can seem easier to use at first,
but it complicates future work with Python. We'll walk you through our alternate setup step-by-step.

### Installing Python 3

Your Mac only comes with Python 2 out of the box, so we'll need make sure we have Python 3 for the course.

First, it's possible you might already have installed Python 3. Before we move on, open your terminal (e.g. the Terminal application on your Mac),
and run

  which python3

`which` tells you the location of the program you ask it about, in this case `python3`. If you see any output from this command on a new line, e.g.

  ╰─$ which python3
  /usr/local/bin/python3

**move to the section on installing `pipenv` below**. If you run this command and do not see any output, you do not have Python 3 installed, so read on.

We're going to use a program called [Homebrew](https://brew.sh/#install) to install Python 3 and other software we'll use in this class. 
To check if you have Homebrew installed, run this command in your terminal:

  which brew

If this doesn't print any output to the screen, copy and paste this command in your terminal, and press Enter:

  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Wait for Homebrew to finish installing. Once done, run

  brew install python

which will install Python 3.

### Installing `pipenv`

Warning: this is going to get a little weird, but we'll walk through this step-by-step.

Python has a concept of "packages": Python code that someone else has written and "packaged" to share with others. 
If someone else has written code that does exactly what you want, you should use that code instead of re-inventing the wheel.

We'll be using packages throughout the course: some are already installed when you install Python; others you have to install yourself.
The latter are typically called "third-party" packages.

When you work on a new project, you want to make sure you clearly define all the packages that are required for your software to run.
This way, if someone else teams up with you to work on the project, they can see a list of the packages they need to install 
before they start. These are commonly known as "dependencies" (my project _depends on_ this package to run), or "requirements".

Different projects have different dependencies, so you need a way to install package A for one project, and package B for another.
The programming we do for the course will have its own set of dependencies, so we'll want to keep those separate from projects
you do for work. To manage the dependencies for different project, we'll create a new "environment" for each project. This helps
separate everything related to a project in its own bucket.

[`pipenv`](https://docs.pipenv.org/) faciliates a few things related to environments:

* Creating a new environment for a new project
* Installing new third-party packages for a project
* Listing all the third-party packages we've installed for a project
* And more
