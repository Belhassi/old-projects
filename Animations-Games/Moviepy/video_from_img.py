from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import * 
from PIL import Image


video_dir = os.path.join(SAMPLE_OUTPUTS, "video")
os.makedirs(video_dir, exist_ok=True)
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "imgs")
file_name = str(input('Enter File name:'))
video = os.path.join(video_dir, f"{file_name}.mp4")


diroctory = {}

for root, dir, files in os.walk(thumbnail_dir):
  for fname in files:
      filename = os.path.join(thumbnail_dir ,fname)
      key = float(fname.replace(".jpg", ""))
      diroctory[key] = filename

paths = []
for k in sorted(diroctory.keys()):
  paths.append(diroctory[k])

my_clips = []
for path in paths:
  Clip = ImageClip(path)
  my_clips.append(Clip.img)

clip = ImageSequenceClip(my_clips, fps=5)
clip.write_videofile(video)
