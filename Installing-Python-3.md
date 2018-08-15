## Installing Python 3 and software for the course

### Prerequisities

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

The `which` command tells you the location of the program you ask it about, in this case `python3`. If you see any output from this command on a new line, e.g.

    ╰─$ which python3
    /usr/local/bin/python3

**move to the section on installing `pipenv` below**. If you run this command and do not see any output, you do not have Python 3 installed, so read on.

We're going to use a program called [Homebrew](https://brew.sh/#install) to install Python 3 and other software we'll use in this class. 
To check if you have Homebrew installed, run this command in your terminal:

    which brew

If this doesn't print any output to the screen, copy and paste this command in your terminal, and press Enter:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

This installs Homebrew. Wait for Homebrew to finish installing. Once done, run

    brew install python

which will install Python 3.

### Installing `pipenv`

*Warning*: things are going to get a little weird, but we'll walk through this step-by-step to reinforce all the new terms and concepts.

Python has a concept of *packages*: Python code that someone else has written and "packaged" to share with others. 
If someone else has written code that does exactly what you want, you should use that code instead of re-inventing the wheel.

We'll be using packages throughout the course: some are already installed when you install Python; others you have to install yourself.
The latter are typically called *"third-party" packages*.

When you work on a new project, you want to make sure you clearly define all the packages that are required for your software to run.
This way, if someone else teams up with you to work on the project, they can see a list of the packages they need to install 
before they start. These are commonly known as *dependencies* (my project _depends on_ this package to run), or *requirements*.

Different projects have different dependencies, so you need a way to install package `A` for one project, and package `B` for another.
The programming we do for the course will have its own set of dependencies, so we'll want to keep those separate from projects
you do for work. To manage the dependencies for different project, we'll create a new *environment* for each project. This helps
separate everything related to a project in its own bucket.

We'll use a tool called [`pipenv`](https://docs.pipenv.org/), which faciliates a few things related to environments:

* Creating a new environment for a new project
* Installing new third-party packages for a project
* Listing all the third-party packages we've installed for a project
* And more!

To install `pipenv`, run

    brew install pipenv

### Setting up a working directory for the class

We'd like to keep a consistent structure for where we keep code for the class. We'll create a new *directory* (this is just a fancy name for a folder)
where everything will live.

You can keep this new directory anywhere you want. We'll just try to keep what's _inside_ the directory consistent.

Open your terminal. You might remember the `pwd` command from the Command Line Basics lecture. Unless you've changed directories using the `cd` command,
`pwd` should print your "home" directory, e.g.

    ╰─$ pwd
    /Users/dylansather

Your home directory will look something like `/Users/<your username>`. If your output looks different, you can always just type

    cd

on its own, and press Enter, and you'll return home (you can confirm by running the `pwd` command again).

I'll be keeping the class directory in my home directory. To create a new directory from the command line, run
  
    mkdir python-bootcamp

`mkdir` stands for: "make directory". Again, *you can create this directory anywhere on your computer you want*. If you want to keep this on your Desktop, for instance, run

    cd Desktop
    mkdir python-bootcamp

which will move you into your Desktop and make the new directory there.

Now that this directory exists, `cd` into it:

    cd python-bootcamp

### Installing `git`, downloading the code for class.

For more information on `git`, watch the lecture video on [Git and Github Overview](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/3422026?start=0).
