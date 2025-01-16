''' Split artwork from an RFC XML file and feed them to a command.
'''
import os
import sys
import logging
import argparse
import subprocess
import lxml.etree as etree

LOGGER = logging.getLogger()


def main():
    ''' Main entry for the tool. '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', default='info',
                        help='The minimum logging severity displayed.')
    parser.add_argument('--lines', default=None, choices=['combine', 'separate'],
                        help='If combine, replace all newlines with whitespace and send to one command process as separate lines. If separate, split all values on newlines and send each input line to a command process.')
    parser.add_argument('infile', help='The file to read from.')
    parser.add_argument('xpath', help='The XPath expression to match.')
    parser.add_argument('command', nargs=argparse.REMAINDER,
                        help='The command and its arguments to run and pass to stdin.')

    args = parser.parse_args()
    logging.basicConfig(
        level=args.log_level.upper(),
        stream=sys.stderr
    )
    logging.root.debug('command args: %s', args)

    with open(args.infile, 'rb') as infile:
        xml_parser = etree.XMLParser()
        doc = etree.parse(infile, xml_parser)

    parts = []
    if args.lines == 'combine':
        parts.append('')
    for elem in doc.xpath(args.xpath):
        text = elem.text.strip()

        if args.lines == 'combine':
            parts[0] += text + '\n'
        elif args.lines == 'separate':
            parts += text.splitlines()
        else:
            parts.append(text)

    exitcodes = []
    for part in parts:
        LOGGER.info('Processing text:\n%s', part)
        proc = subprocess.Popen(args.command, stdin=subprocess.PIPE)
        proc.communicate(part.encode('utf8'))
        proc.stdin.close()
        status = proc.wait()
        exitcodes.append(status)
        LOGGER.info('Finished with exit code: %s', status)

    return max(exitcodes) if exitcodes else 0


if __name__ == '__main__':
    sys.exit(main())
