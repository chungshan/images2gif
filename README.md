# Images to GIF
Convert your images (video) to GIF
No limitations and watermark, for free!
## Requirement
1. It require modules ```moviepy``` and ```opencv-python```
```python
pip install -r requirement.txt
```

## Usage
1. Convert images to GIF
```python
python main.py --type image --file "folder to your images" --fps "frame rate of GIF"
```
2. Convert video to GIF
```python
python main.py --type video --file "your video" --start "start time" --end "end time" --interval "Interval of pictures in gif" --fps "frame rate of GIF"
```

## Troubleshooting
1. What argument ```--interval``` for?
For example, if your video has 60 frames and I set ```--interval 5```.
This means that I will take one picture in 5 frames for generating GIF.