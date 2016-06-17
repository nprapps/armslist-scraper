# Armslist scraper

* [What is this?](#what-is-this)
* [Assumptions] (#assumptions)
* [Installation] (#installation)
* [Run the project] (#run)
* [What to expect] (#what-to-expect)

## What is this? <a id="what-is-this"></a>

Armslist is a tool for aggregating listings from Armslist.com, a site used as a marketplace for buying and selling guns.  

## Assumptions <a id="assumptions"></a>

The following things are assumed to be true in this documentation.
* You are running OSX.
* You are using Python 2.7. (Probably the version that came OSX.)
* You have virtualenv and virtualenvwrapper installed and working.
* You have GNU Parallel installed -- a shell tool to execute multiple commands from standard input simultaneously.

For more details on the technology stack used with the app-template, see our [development environment blog post](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html).

This code should work fine in most recent versions of Linux, but package installation and system dependencies may vary.

## Installation <a id="installation"></a>

If you don’t already have GNU Parallel, get it like this:

```
brew install parallel
```

Then clone the project:

```
git clone git@github.com:nprapps/armslist.git
cd armslist
```

## Run the project <a id="run"></a>

Next, create a virtual environment and install the requirements:

```
mkvirtualenv armslist
pip install –r requirements.txt
```

Finally, run the script:

```
./scrape.sh
```

## What to expect <a id="what-to-expect"></a>

The scraper will output the listings into a csv format. 

Running script will make two main csv files as well as some extra files that may be handy for testing:

* `cache/index.csv` is a master index of listings with the URL, state and date. This file is used to scrape each page individually.
* `cache/listings.csv` is the bulk of the data. Each row represents a listing and the associated details.
* `cache/state/1/<statename>` includes the log messages in a file called `stderr` and scraped index page data in a file called `stdout` on a per state basis.

The script could take a long time to run. We recommend using a fairly powerful Amazon EC2 instance in the Virginia/us-east-1 region to run the scraper.
