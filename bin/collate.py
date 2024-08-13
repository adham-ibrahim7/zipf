"""Get word counts from multiple files and collate into a single csv."""

import argparse
import csv
from collections import Counter
import utilities as util


def update_counts(word_counts, reader):
    """Update word counts with data from a file reader."""
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)


def main(args):
    """Run the command line program."""
    word_counts = Counter()
    for infile in args.infiles:
        update_counts(word_counts, infile)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infiles', type=argparse.FileType('r'),
                        nargs='*', help='Input file names')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output n most frequent words')
    args = parser.parse_args()
    main(args)