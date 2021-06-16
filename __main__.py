# file package/__main__.py

import os
from multiprocessing import Process
from main import run

if __name__ == '__main__':
    os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;0"
    p = Process(target=run)
    p.start()
    p.join()
