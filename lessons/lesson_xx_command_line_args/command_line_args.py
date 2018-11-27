from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                    action="store_false", dest="verbose", default=True,
                    help="don't print status messages to stdout")

args = parser.parse_args()


# https://gis.stackexchange.com/questions/208430/trying-to-extract-a-list-of-unique-values-from-a-field-using-python
