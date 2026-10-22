from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
ok_anime = '/home/imad/Programming/Project/py_project/Moviepy/data/samples/inputs/okanime-2372-HD-08.mp4'
imgs_dir = os.path.join(SAMPLE_OUTPUTS, "imgs")
os.makedirs(imgs_dir, exist_ok=True)

clip = VideoFileClip(ok_anime)
fps = clip.reader.fps
duration = clip.duration
fpsh = int(fps)*10

for frame_index ,frame in enumerate(clip.iter_frames()):
    second = int(frame_index/fps) + 1
    img_path = os.path.join(imgs_dir, f"{second}.jpg")
    new_img = Image.fromarray(frame)
    new_img.save(img_path)
    print(img_path)
