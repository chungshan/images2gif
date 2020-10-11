from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse
import cv2
import imageio
import os

parser = argparse.ArgumentParser()
parser.add_argument('--type', dest='file_type', action='store', help='Images or video')
parser.add_argument('--file', dest='file', action='store', help='Path to your images(folder) or video to generate gif', default=None)
parser.add_argument('--start', dest='start_time', action='store', help='Start time of video', default=0)
parser.add_argument('--end', dest='end_time', action='store', help='End time of video', default=0)
parser.add_argument('--interval', dest='interval', action='store', help='Interval of pictures in gif', default=0)
parser.add_argument('--fps', dest='fps', action='store', help='frame rate of gif', default=30)
args = parser.parse_args()

file = args.file
if file is not None:
    path = os.path.normpath(file)
    file = path.split(os.sep)[-1]
else:
    raise RuntimeError("Please enter your path to files")

start_time = int(args.start_time)
end_time = int(args.end_time)
interval = float(args.interval)
file_type = args.file_type
fps = args.fps
def clip_viedo(video, start_time, end_time):
    target_name = "clipped_" + str(video)
    ffmpeg_extract_subclip(video, start_time, end_time, targetname=target_name)
    return target_name

def video_to_gif(video, interval, duration, fps):
    vidcap = cv2.VideoCapture(video)
    num_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) # frames of video

    if interval != 0:
        num_frames_to_pick = duration / interval
    else:
        num_frames_to_pick = num_frames # pick all frames

    if num_frames_to_pick < num_frames:
        duration_pic = int(num_frames / num_frames_to_pick)
    else:
        duration_pic = 1

    success, image = vidcap.read() # read image from video
    images = []
    count = 1

    while success:
        if (count % duration_pic == 0):
            images.append(image)
        success, image = vidcap.read()
        count += 1
    images_to_gif(images, fps)

def images_to_gif(imgs, frame_rate):
    imageio.mimsave('movie3.gif', imgs, fps=frame_rate)  # save images to gif

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

if __name__ == '__main__':
    if file_type == 'video':
        print("Convert video to gif")
        if (end_time <= start_time):
            raise RuntimeError("Your end time is smaller thant start time!")
        clipped_video = clip_viedo(file, start_time, end_time)
        video_to_gif(clipped_video, interval, (end_time - start_time), fps)
        os.remove(clipped_video) # remove clipped video
    elif file_type == 'image':
        print("Convert images to gif")
        images = load_images_from_folder(file)
        images_to_gif(images, fps)
    else:
        raise RuntimeError("Please enter your file's type (video or image)")
