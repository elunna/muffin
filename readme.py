def make_readme(info_dict):
    """
    Creates the README.md file and uses the passed in dictionary to fill in the fields.
    Returns the filepath of the created file.
    """
    filename = info_dict['projectname'] + '/' + 'README.md'
    twitter = info_dict.get('twitter', None)
    email = info_dict.get('email', None)
    date = get_date()
    license = info_dict['license']

    with open(filename, 'w') as f:
        f.write('# Project Name: {}'.format(info_dict['projectname']))
        f.write('\n')
        f.write('> {}'.format(info_dict['description']))
        f.write('\n')
        f.write('\n')

        # Add in standard template here.
        f.write(TEMPLATE)

        f.write('## Meta')
        f.write('\n')
        f.write('##### Author: {}'.format(info_dict['author']))
        f.write('\n')
        f.write('##### Start Date: {}'.format(date))
        f.write('\n')
        if twitter:
            f.write('##### Twitter -- [@{}](https://twitter.com/{})'.format(twitter, twitter))
            f.write('\n')
        if email:
            f.write('##### Email -- {}'.format(email))
            f.write('\n')
        f.write('\n')
        f.write('[![](http://img.shields.io/badge/license-{}-blue.svg)]'.format(license))
        f.write('\n')
        f.write('[{}]: See ``LICENSE`` for full text.'.format(info_dict['license']))
        f.write('\n')

    return filename


def get_date():
    import datetime as dt
    now = dt.datetime.now()
    return str(now.date())


TEMPLATE = """
## What's it?

[Project summary]

![](screenshot.png)

### Features
- **Feature 1** Description
- **Feature 2** Description

---

### Prerequisities
Python 2

#### Uses
* argparse, logging, pytest


### Installing
- **Linux:**
- **Max OS X:** n/a
- **Windows:** n/a

---

## Usage
```
$ python main.py
```
For help: python main.py -h

***EXAMPLES:***
> Example 1:
```
$ python main.py 1
```

> Example 2:
```
$ python main.py 2
```

---

### TODO

- [ ] Fill in README details.
- [ ] First commit: README
- [ ] First branch:
- [ ] Create first functional test
- [ ] Add a screenshot to the README
- [ ] Configure konch to be really sexy with iPython
- [ ] Generate requirements.txt with $ pip freeze --local > requirements.txt
- [ ] Setup sphinx docs: $ python manage.py docs
- [ ] Build sphinx docs: $ project/doc/make html
- [ ] Start first sphinx documentation!

---

"""
