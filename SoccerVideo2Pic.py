# -- encoding:utf-8 --

import cv2
import os


def save_img(video_path):
    # 输入：视频所在文件夹路径，注意最后带有/
    # 输出：每隔timeFms存视频，在文件夹img内保存图像
    videos = os.listdir(video_path)
    for video_name in videos:
        # file_name = video_name.split('.')[0]
        # folder_name = video_path + file_name
        folder_name = 'img2'
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(video_path + video_name)  # 读入视频文件
        c = 0
        rval = vc.isOpened()
        timeF = 25  # 视频帧计数间隔频率
        while rval:  # 循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name + '/'
            if rval:
                if (c % timeF == 0):  # 每隔timeF帧进行存储操作
                    # cv2.imwrite('../image/' + str(c) + '.jpg', frame)  # 存储为图像
                    cv2.imwrite(pic_path + str('%06d' % c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg

            # cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)


video_path = '../videos/'  # 存放视频的文件夹，要带

save_img(video_path)
