from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import StreamingHttpResponse
import cv2
import os


from pyzbar.pyzbar import decode


def scaner():
    dic,header = dictprint()
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    to_print = None
    while True:
        ret, frame = cap.read()
        for code in decode(frame):
            to_print = code.data.decode('utf-8')
        #cv2.imshow('Testing scaner', frame)
        #cv2.waitKey(10)
        if to_print:
            break
    cap.release()
    cv2.destroyAllWindows()
    dict = {}
    header.pop()
    lst = []
    if to_print in dic:
        real = True
        loop_lst = []
        for i , ele in enumerate(header) :
            loop_lst.append(ele.capitalize())
            loop_lst.append(' : ')
            loop_lst.append(dic[to_print][i])
            str = ' '.join(loop_lst)
            lst.append(str)
            loop_lst = []

        dict["header"] = header
        dict["data"] = lst

        dict["auth"] = real
        return dict
    else:
        real = False
        return {"auth" : real}

def index(request):
    return render( request, "hello/home.html")

def scan(request):
    dic = scaner()
    return render(request,"hello/scan.html", context= dic)

def dictprint():
    module_dir = os.path.dirname(__file__)  # get current directory
    #df = pd.read_csv(module_dir + '/data.csv')
    import csv
    file = open(module_dir + '/data.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)
    dict = {}
    for row in csvreader:
        dict[row[-2]] = row[:]
    file.close()

    return dict, header

def createdb(request):
    dic = {}
    return render(request,"hello/createdb.html",context = dic )
