#!/bin/env python3
# Read stdin and verify it as valid text against an ABNF schema.
import argparse
import logging
import os
import sys
from abnf import Rule, ParseError


LOGGER = logging.getLogger()


class FromFileRule(Rule):
    pass
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('schema')
    args = parser.parse_args()
    logging.basicConfig(level='INFO')

    LOGGER.debug('Loading schema from %s', args.schema)
    FromFileRule.from_file(args.schema)
    
    anyerr = False
    for inline in sys.stdin:
        inline = inline.strip()
        LOGGER.debug('Checking text: %s', inline)
        try:
            tparser = FromFileRule('eid-pattern')
            tparser.parse_all(inline)
        except ParseError as err:
            LOGGER.error('Failed to parse "%s" with result: %s', inline, err)
            anyerr = True
    
    return 2 if anyerr else 0


if __name__ == '__main__':
    sys.exit(main())
