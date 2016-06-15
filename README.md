Copyright 2016 NPR. All rights reserved. No part of these materials may be reproduced, modified, stored in a retrieval system, or retransmitted, in any form or by any means, electronic, mechanical or otherwise, without prior written permission from NPR.

(Want to use this code? Send an email to nprapps@npr.org!)

# Armslist

* What is this?
* Assumptions
* Requirements
* Installation
* Run the project
* What to expect

## What is this?

Armslist is a tool for aggregating listings from Armslist.com, a site used as a marketplace for buying and selling guns.  

## Assumptions

The following things are assumed to be true in this documentation.
* You are running OSX.
* You are using Python 2.7. (Probably the version that came OSX.)
* You have virtualenv and virtualenvwrapper installed and working.

For more details on the technology stack used with the app-template, see our development environment blog post.

## Requirements

* Parallel -- a shell tool to execute multiple commands from standard input simultaneously

## Installation

If you don’t already have parallel, get it like this:

```
brew install parallel
```

Then clone the project:

```
git clone git@github.com:nprapps/armslist.git
cd armslist
```

## Run the project

Next, create a virtual environment and install the requirements:

```
mkvirtualenv armslist
pip install –r requirements.txt
```

Finally, run the script:

```
./scrape.sh
```

## What to expect

The scraper will output the listings into a csv format. Running script will make two main csv files: cache/index.csv is a master of all listings with the URL, state and date; and listings.csv will be the bulk of the data with each listing and the associated details.
