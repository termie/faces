FROM debian:jessie

#RUN export http_proxy=http://www-proxy.us.oracle.com:80; apt-get update
#RUN export http_proxy=http://www-proxy.us.oracle.com:80; apt-get install -y python python-dev python-pip
#RUN export http_proxy=http://www-proxy.us.oracle.com:80; apt-get install -y libopencv-calib3d2.4 libopencv-core2.4 libopencv-features2d2.4 libopencv-flann2.4 libopencv-highgui2.4 libopencv-imgproc2.4 libopencv-legacy2.4 libopencv-ml2.4 libopencv-objdetect2.4  libopencv-video2.4 libv4l-0 libv4lconvert0 python-opencv libdc1394-22

RUN apt-get update
RUN apt-get install -y python python-dev python-pip
RUN apt-get install -y libopencv-calib3d2.4 libopencv-core2.4 libopencv-features2d2.4 libopencv-flann2.4 libopencv-highgui2.4 libopencv-imgproc2.4 libopencv-legacy2.4 libopencv-ml2.4 libopencv-objdetect2.4  libopencv-video2.4 libv4l-0 libv4lconvert0 python-opencv libdc1394-22

RUN pip install pubnub
RUN pip install Algorithmia

WORKDIR /func
ADD . /func

ENTRYPOINT ["python", "func.py"]
