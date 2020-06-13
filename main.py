import curses
import sys
import shutil
import os.path
import backend

def main():
  if len(sys.argv) > 1 and sys.argv[1].startswith('init:'): # Init number of frames
    for i in range(2, int(sys.argv[1].replace('init:',''))): # Don't include frames 0 or 1
      shutil.copy(os.path.join(os.getcwd(), 'frames/1.txt'), os.path.join(os.getcwd(), f"frames/{i}.txt"))
      exit()

  def run(screen, frames, config):
    x = 0
    y = 0

    for i, frame in enumerate(frames):

      for f in frame:
        for c in f:
            screen.addstr(y, x, c) # char
            x += 1
        y += 1
        x = 0
      x, y = (0, 0) # Reset
      screen.refresh() #Display changes

      if  str(i) in list(config.keys()): #User defined delay
        curses.napms(config[str(i)])
      else:
        curses.napms(config['all']) #Default delay
      screen.clear()

          
  with open(os.path.join(os.getcwd(), 'frames/config.txt')) as f:
    config = f.read()
  curses.wrapper(run, backend.read_frames(), backend.readconf(config))

main()
