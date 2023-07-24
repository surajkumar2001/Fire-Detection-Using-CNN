import cv2


def FrameCapture(path, i):
    pathout = "D:/AI Project/imgs"

    vidObj = cv2.VideoCapture(path)

    count = 0
    frame_skip = 2

    success = 1

    while success:

        success, image = vidObj.read()

        if count % frame_skip == 0 and success and image is not None:
            try:
                cv2.imwrite(pathout + "/fire"+str(i) +
                            "frame%d.jpg" % count, image)
            except cv2.error as e:
                print("End of video reached")

        count += 1


if __name__ == '__main__':

    for i in range(1, 12):
        FrameCapture(
            "D:/AI Project/vids/video_data/fire"+str(i)+".mp4", i)
