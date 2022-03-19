#each array is a node
#not completely live, a burst of data
#SOURCE OpenBCI documentation from OpenBCI.com

from platform import node
from pyOpenBCI import OpenBCICyton

def print_raw(sample):
    print(sample.channels_data)
board=OpenBCICyton(daisy=True)
board.start_stream(print_raw)

