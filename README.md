Copyright 2016 NPR. All rights reserved. No part of these materials may be reproduced, modified, stored in a retrieval system, or retransmitted, in any form or by any means, electronic, mechanical or otherwise, without prior written permission from NPR.

(Want to use this code? Send an email to nprapps@npr.org!)

# Armslist

* [What is this?](#what-is-this)
* [Assumptions] (#assumptions)
* [Requirements] (#requirements)
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

For more details on the technology stack used with the app-template, see our development environment blog post.

## Requirements <a id="requirements"></a>

* Parallel -- a shell tool to execute multiple commands from standard input simultaneously

## Installation <a id="installation"></a>

If you don’t already have parallel, get it like this:

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

The scraper will output the listings into a csv format. Running script will make two main csv files: cache/index.csv is a master of all listings with the URL, state and date; and listings.csv will be the bulk of the data with each listing and the associated details.

Don't worry if the script is taking a long time to run. There's a lot of data coming so that's expected. 
