# Foreign Function Interfaces for Web Developers

Language interoperability for coders with impatient users.

---

Python is a general-purpose programming language that is well-suited for a web application stack.  That said, there are sometimes opportunities to increase performance or productivity by mixing the benefits of different languages,
such as the expressiveness of Python with the speed of C++.


This repository contains the implementations of the techniques and ideas that were explored in a talk I gave at PyGotham 2015.  If you missed the talk, it focused on interactions between Python and other programming languages within the context and contraints of coding for web applications.

The slides should be uploaded within a day of the talk and the video should be linked here when available (please open a GH issue if this is not the case).

----

![screenshot of the web application](https://raw.github.com/tristanfisher/ffi4wd/master/ffi4wd.png)

This repository contains a web application useful for testing various FFI approaches.

----

## Requirements

	- Python 3.4
	- OS X or Linux
	- A C and C++ compiler
	    - If OS X, probably Xcode command-line tools
	    - Buyer's choice on Linux (gcc is popular)

## Installation and setup

#### Git clone the repo:

    git clone https://github.com/tristanfisher/ffi4wd.git


Use a [virtual environment](https://docs.python.org/3/library/venv.html) to create a clean environment so our work and package installations don't affect other things on the system.

    cd ffi4wd
    pyvenv-3.4 env
    source env/bin/activate

Make sure that you're in Python 3.4 and that your virtualenv is activated.

Run the `makefile`:

	make all

this will install the Python requirements and compile several shared objects.

## Run tests

This will give us some certainty that we've installed correctly.

#### Other Notes

I appreciate feedback.  Please open pull requests, issues, and/or contact me.
