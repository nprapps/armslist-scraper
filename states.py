#!/usr/bin/env python
"""Print state names for use in the scraper script.

The function uses us package to print states for running the listing script.
Runs check for NJ, Puerto Rico and Guam due to inconsistantcies in armslist URLs.
"""
import us


def print_states():
    for state in us.states.STATES:
        if state.name == 'New Jersey':
            print('nj')
        else:
            name = state.name.lower().replace(' ', '-')
            print(name)

    print('puerto-rico-usa')
    print('guam-usa')


if __name__ == '__main__':
    print_states()
