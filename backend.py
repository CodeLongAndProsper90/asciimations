import os.path
import os

def twodit(file_contents):
	final1 = file_contents.split('\n')
	final = []
	for l in final1:
		final.append([c for c in l])
	return final
def readconf(config):
  lines = config.rstrip().split('\n')
  config = {}
  for l in lines:
    configs = l.split(':')
    frame = configs[0]
    sleep = configs[1]
    config[frame] = int(sleep)
  return config
def read_frames():
  frames = []
  files = os.listdir('frames')
  files.remove('config.txt')
  for file in files:
    with open(os.path.join(os.getcwd(), f"frames/{file}")) as f:
      frames.append(twodit(f.read()))
  return frames
