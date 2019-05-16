FROM python:3
MAINTAINER Roman Ryabchun <r.ryabchun@bpmonline.com>
ADD sysinfo.py /sysinfo.py
RUN pip3 install psutil
ENTRYPOINT [ "python3", "/sysinfo.py" ]
CMD ["cat"]
