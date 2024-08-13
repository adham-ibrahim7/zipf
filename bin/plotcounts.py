"""Plot word counts from csv."""

import argparse
import pandas as pd


def plotcounts(input_csv_name, outfile, xlim):
    df = pd.read_csv(input_csv_name, header=None,
                     names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                           method='max')
    df['inverse_rank'] = 1 / df['rank']
    scatplot = df.plot.scatter(x='word_frequency',
                               y='rank', loglog=True,
                               figsize=[12, 6],
                               xlim=[xlim[0], xlim[1]] if xlim else None,
                               grid=True)
    fig = scatplot.get_figure()
    fig.savefig(outfile)


def main(args):
    plotcounts(args.infile, args.outfile, args.xlim)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('--outfile', type=str,
                        nargs='?', default='plotcounts.png')
    parser.add_argument('--xlim', type=int, nargs=2)
    args = parser.parse_args()
    main(args)