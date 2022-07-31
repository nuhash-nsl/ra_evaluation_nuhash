import sys
import os 

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root_dir, 'musicplayer'))


import musicplayer
from musicplayer import audio,bar, foo
from musicplayer.audio import read_audio
#from tests import test_musicplayer


if __name__ == "__main__":
    print("Hello, World!")