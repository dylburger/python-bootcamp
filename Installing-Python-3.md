## Installing Python 3 and software for the course

There are a few things we'd like you to install before the course, to make sure you're well-prepared to start coding.
If you've never programmed before, many of these concepts will be new, but we'll try to explain what we're installing and why
we're installing it along the way.

If you have trouble at any point, don't hesitate to reach out to the group Slack channel with questions. Someone else may have
experienced and fixed the same issue.

### Prerequisities

Before reviewing this guide, make sure you've watched these lecture videos from the Udemy course:

* [Python 2 vs. Python 3](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/9373030?start=0)
* [Command Line Basics](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/9431354?start=0)
* [Running Python Code](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/9373062?start=15) (up to 7:34)

**We are not going to install Python 3 using Anaconda, which the course recommends**. Anaconda can seem easier to use at first,
but it complicates future work with Python. We'll walk you through our alternate setup step-by-step.

### Installing Python 3

Your Mac only comes with Python 2 out of the box, so we'll need make sure we have Python 3 for the course.

First, it's possible you might already have installed Python 3. Before we move on, open your terminal (e.g. the Terminal application on your Mac),
type the following code and press Enter:

    which python3

From now on, when I say "run this code", it means: type the code specified, and press Enter.

The `which` command tells you the location of the program you ask it about, in this case `python3`. If you see any output from this command on a new line, e.g.

    ╰─$ which python3
    /usr/local/bin/python3

**move to the section on installing `pipenv` below**. 

If you run this command and **do not** see any output, you do not have Python 3 installed, so read on.

We're going to use a program called [Homebrew](https://brew.sh/#install) to install Python 3 and other software we'll use in this class. 
To check if you have Homebrew installed, run this command in your terminal:

    which brew

If this doesn't print any output to the screen, copy and paste this command in your terminal, and press Enter:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

This installs Homebrew. You may be prompted to enter your computer's password. When you type, you may also not see any characters
printed to the screen as you type it. This is OK - keep typing it and press Enter. It should continue.

You'll see quite a bit of output as Homebrew installs. Wait it to finish. Once done, run

    brew install python

which will install Python 3.

**Note**: if you encounter any strange errors or warnings installing Python 3 with `brew`, don't hesitate to reach out with questions!

### Installing `pipenv`

**Warning**: things are going to get a little weird, but we'll walk through this step-by-step to reinforce all the new terms and concepts.

Python has a concept of **packages**: Python code that someone else has written and "packaged" to share with others. For instance,
[Flask](http://flask.pocoo.org/) helps you build a website with just a few lines of code. If you had to implement this functionality
on your own, you'd write hundreds. If someone else has written code that does exactly what you want, you should use that code instead of re-inventing the wheel.

We'll be using packages throughout the course. Some are already installed when you install Python; others you have to install yourself.
The latter are typically called **"third-party" packages**.

When you work on a new project, you want to make sure you clearly define all the packages that are required for your software to run.
This way, if someone else teams up with you to work on the project, they can see a list of the packages they need to install 
before they start. These are commonly known as **dependencies** (my project _depends on_ this package to run), or **requirements**.

Different projects have different dependencies, so you need a way to install package `A` for one project, and package `B` for another.
The programming we do for the course will have its own set of dependencies, so we'll want to keep those separate from projects
you do for work. To manage the dependencies for different project, we'll create a new **environment** for each project. This helps
separate everything related to a project in its own bucket.

We'll use a tool called [`pipenv`](https://docs.pipenv.org/), which faciliates a few things related to environments:

* Creating a new environment for a new project
* Installing new third-party packages for a project
* Listing all the third-party packages we've installed for a project
* And more!

To install `pipenv`, run

    pip3 install pipenv

There will be a lot of output here. To confirm `pipenv` was installed correctly, run

    pipenv --version

which should print something like:

    ╰─$ pipenv --version
    pipenv, version 2018.7.1

### Setting up a "working directory" for the class

We'd like to have a consistent structure for where we keep code for the class. We'll create a new **directory** (this is just a fancy name for a folder)
where everything will live.

You can keep this new directory anywhere you want. We'll just try to keep what's _inside_ the directory consistent.

Open your terminal. You might remember the `pwd` command from the Command Line Basics lecture. Unless you've changed directories using the `cd` command,
`pwd` should print your "home" directory, e.g.

    ╰─$ pwd
    /Users/dylansather

Your home directory will look something like `/Users/<your username>`. If your output looks different, you can always just type

    cd

on its own, and press Enter, and you'll return home (you can confirm by running the `pwd` command again).

Once I'm home, I'll create my directory here, so I can easily find it. To create a new directory from the command line, run
  
    mkdir python-bootcamp

`mkdir` stands for: "make directory". Again, **you can create this directory anywhere on your computer you want**. If you keep most of your work on your Desktop, for instance, run

    cd Desktop
    mkdir python-bootcamp

which will move you into your Desktop and make the new directory there.

A quick aside: you may have noticed that both `cd` and `mkdir` **print nothing to the screen, but they still run successfully**. This can seem strange at first.
The idea is: you should be able to do your work as fast as possible, and having to read output from commands (e.g. "Directory successfully created!") just takes
time. If the default is to print nothing to the screen, you have to think less and you can move faster. **Key takeaway**: if you type a command and press Enter, and
the terminal just moves to the next line, your command probably worked! In the case of `mkdir`, you can always run

    ls

and confirm that the new directory you created shows up in the list of files and directories.

Now that this directory exists, `cd` into it:

    cd python-bootcamp

### Using `pipenv` to create a new Python project

First, remember how to tell where you currently are inside your terminal?

    pwd

Run this to confirm you're within the new, `python-bootcamp` directory.

Once there, run

    pipenv --three

This tells `pipenv` to create a new Python environment using Python 3.

You'll see *a lot* of output on your screen. Here's what happened when I ran this command:

```
Creating a virtualenv for this project...
Pipfile: /Users/dylansather/python-bootcamp/Pipfile
Using /usr/local/bin/python3 (3.7.0) to create virtualenv...
⠋Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7'
/usr/local/Cellar/pipenv/2018.7.1/libexec/lib/python3.7/site-packages/virtualenv.py:1041: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  import imp
New python executable in /Users/dylansather/.virtualenvs/python-bootcamp-ie19AHT2/bin/python3.7
Also creating executable in /Users/dylansather/.virtualenvs/python-bootcamp-ie19AHT2/bin/python
Installing setuptools, pip, wheel...done.
Setting project for python-bootcamp-ie19AHT2 to /Users/dylansather/python-bootcamp

Virtualenv location: /Users/dylansather/.virtualenvs/python-bootcamp-ie19AHT2
Creating a Pipfile for this project...
```

When you start programming, it's normal to be completely overwhelmed by this output. The dirty secret is that even professional programmers can get overwhelmed
with this output. Throughout the course, we'll try to help you build skills to understand 1.) how to interpret errors and 2.) what output to ignore, so you don't
get stuck trying to find errors in the wrong place.

If you run

    ls

and see a `Pipfile` in your `python-bootcamp` directory, **you're good to move on**.

### Installing `git`, downloading the code for class.

For more information on `git`, watch the lecture video on [Git and Github Overview](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/3422026?start=0).

For now, we'll only use `git` to download the code we need for class. As the course progresses, we'll see the real power of `git`.

Like before, let's confirm whether or not you already have `git` installed. Run

    which git

If you get no output, run

    brew install git

To confirm `git` is installed correctly, run

    git --version

which should print the version of `git` you just installed.

Now, confirm you're still in the `python-bootcamp` directory and run

    git clone https://github.com/Pierian-Data/Complete-Python-3-Bootcamp.git

This tells `git` to "clone" the files hosted at the specified URL. Effectively, this just downloads the code we'll be using for the course
to the current directory. If you see output like this:

```
Cloning into 'Complete-Python-3-Bootcamp'...
remote: Counting objects: 381, done.
remote: Total 381 (delta 0), reused 0 (delta 0), pack-reused 381
Receiving objects: 100% (381/381), 360.30 KiB | 687.00 KiB/s, done.
Resolving deltas: 100% (190/190), done.
```

you should be good. Confirm that the directory of code downloaded successfully by running `ls`. You should see something like this now:

    ╰─$ ls
    Complete-Python-3-Bootcamp Pipfile

### Installing `jupyter` to run the code for the class.

We're almost at the finish line.

In your `python-bootcamp` directory, run

    pipenv install jupyter

As with all of these commands, this will generate a lot of output. `pipenv install` installs the specified Python package to your
class environment (the one we created above with `pipenv --three`). `jupyter` is a Python package that lets us open and run "Jupyter notebooks",
which you might remember from the "Running Python Code" lecture.

Once this command finishes, run

    pipenv shell

This command actually tells our computer to "step into" our Python environment, using the version of Python we specified when we created the
environment, as well as any packages (like `jupyter`) that we specified as requirements for that environment.

Generally, you know that you're inside of a given environment if you see something in parentheses before the "prompt" in your terminal:

    (python-bootcamp-ie19AHT2) ╭─dylansather@IC-C02WV0VTHTDD ~/python-bootcamp ‹2.3.7›

The name of your environment, and the prompt that follows it, will look different for everyone. The important part is that you see some
name in parentheses at the start of the line.

Finally, after running `pipenv shell`, run

    jupyter notebook

This should open a new tab in your computer's default web browser automatically, likely at a URL that looks something like [http://localhost:8888/tree](http://localhost:8888/tree).

If this new tab opens successfully, you're good to go with all of the software we'll need for the first part of the course. **Congrats!**
