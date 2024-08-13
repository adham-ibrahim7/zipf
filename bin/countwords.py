import argparse
import string
from collections import Counter
import utilities as util

def count_words(reader):
   """Count the occurrences of words in a string."""
   chunks = reader.read().split()
   npunc = [word.strip(string.punctuation) for word in chunks]
   word_list = [word.lower() for word in npunc if word]
   word_counts = Counter(word_list)
   return word_counts


def main(args):
   """Run the command line program."""
   word_counts = count_words(args.infile)
   util.collection_to_csv(word_counts, args.num)


if __name__ == '__main__':
   USAGE = 'Brief description of what the script does.'
   parser = argparse.ArgumentParser(description=USAGE)
   parser.add_argument('infile', type=argparse.FileType('r'),
                       nargs='?', default='-',
                       help='Input file name')
   parser.add_argument('-n', '--num',
                       type=int, default=None,
                       help='Output n most frequent words')
   args = parser.parse_args()
   main(args)
