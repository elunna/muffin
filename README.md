                      .d888 .d888d8b         
                     d88P" d88P" Y8P         
                     888   888               
88888b.d88b. 888  88888888888888888888888b. 
888 "888 "88b888  888888   888   888888 "88b
888  888  888888  888888   888   888888  888
888  888  888Y88b 888888   888   888888  888
888  888  888 "Y88888888   888   888888  888

# muffinX Python project template wizard
> Makes starting up new projects with bells and whistles a breeze!

### What should a good python template engine have????
* Should have a modern directory structure:
    /src and /tests for separated source and testing.
    /data, /temp, and /logs for managing all the crap that will be pouring in.

* Should have *inpeccable documentation*:
    - README.md for git
    - Sphinx docs ready to use, and a config file to make the setup really quick.

* *Git* ready
    - .gitigore with the essential crap ignored.
    - some all-around useful git-hooks
    - Really nice README.md
    - A LICENSE that we can choose from a list of the most popular.

* Some *AWESOME utilities* included by default:
    - Sphinx documentation
    - Pytest
    - ipython
    - Konch, with some premade great defaults.

* Should have SCARY *virtual environment support*
    - Create a custom virtual environment!
    - Includes
    - Choose from different Python versions
    - Choose different modules to include in the pip install

* Should be *FLEXIBLE!*
    - The wizard lets you keep defaults saved so you can just "Enter" through the common ones.
    - The templates folder can be tweaked for your preference,
    - or make your own templates directory structure, it just has to start with 'template'

* Should be like other AMAZING systems, like Django!
    - Yup, we have a *manage.py* - and it rocks.
    - Cut down on boring, mundane project maintenance, use manage.py fool!


### usage: 
$ python pystart 

### TODO
- [X] Setup the directory structure 
- [X] /project/
- [X] /project/src
- [X] /project/tests
- [X] /project/data
- [X] /project/temp
- [X] /project/logs  (still need this)

- [X] Write startup files:
- [X] __init__.py files for root, src, and tests to indicate packages.
- [X] initial README.md file.
- [X] .gitignore
- [ ] Command line option to only create a README.md

- [X] Basic wizard to specify project info:
- [X] wizard: Project name
- [X] wizard: Author - Default in my settings
- [X] wizard: Purpose
- [X] wizard: Description
- [X] wizard: License: type
- [X] wizard: Ask for starting modules(Beautiful Soup, Scrapy, requests)
- [x] wizard: Ask for Python version(2.7, 3.4, 3.5, etc)(can we list the available ones???)
- [X] wixard: show available choices if user makes a mistake
- [X] Remember project defaults for wizard
- [X] Update defaults when new ones are input from wizard
- [ ] Allow None for some wizard choices

- [x] Main.py: Create empty
- [x] Main.py: Module doc
- [x] Main.py: import logger
- [x] main.py: config file
- [x] Main.py: argparse
- [x] Main.py: main method, "hello project!"

- [x] Complete check of system requirements to run this script (and to have the ideal environment)
# Sys libs
- [x] is git installed?
- [x] is virtualenv installed?
- [x] is python/python3 installed?
# Pip libs
- [x] is pip installed?
- [x] is autoenv installed?
- [x] is konch installed?
- [x] is py.test installed?
- [x] is ['urllib3[secure]', 'requests[security]',  installed for py2?

- [x] Setup virtualenv
- [x] Autoenv config file(.env)?
- [x] Setup.sh script that executes program installs
- [x] Setup.sh: update pip
- [x] Setup.sh: initialize git repo 
- [x] Setup.sh: pip install basic packages(autoenv, konch, pytest)
- [x] Use Python 2(later option to use python3)
- [ ] Option to use PyPy?
- [ ] Option to use Anaconda?


# Functional tests for addons
- [ ] Functional test for Selenium
- [ ] Functional test for Beautiful Soup
- [ ] Functional test for requests

- [ ] manage.py - Create a utility to make managing mundane tasks much easier
- [ ] cleanup - clear out the temp, data directories
- [ ] archive - archive the data directory into a gzip/bz, then clear it out.
- [ ] new module(pop): Create Basic template for a new module and it's corresponding test.
- [ ] freeze: create/regenerate requirements.txt for virtualenv
- [ ] setup docs(sphinx)

- [ ] CC-BY-SA 3.0 : http://creativecommons.org/licenses/by-sa/3.0/
- [ ] argparse - debug option, verbose built in 

Other modules to ask about:
    lxml, pillow, 

How to check coverage, with pytest?
Travis CI?
PyPi?
Attach githooks? 
