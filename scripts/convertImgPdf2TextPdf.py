#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import traceback, os, json, os, uuid, time, sys, requests
curr_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curr_path, "../conf"))
import config
ESCAP_LIST = []


def convertImgPdf2TextPdf(sname):
    if not sname.strip().endswith(".pdf"): return False
    tname = "c_" + os.path.splitext(sname)[0] + ".pdf"
    tpath = os.path.join(config.FILEPATH, tname)
    os.system("C: && cd C:\\ProgramData\\ABBYY\\SDK\\11\\FineReader Engine\\Samples\\Java\\Hello && call RunImgImgPdf2TextPdf.cmd %s %s" % (sname, tname))
    if not os.path.isfile(tpath):
        print 'convert to pdf failed, file name:' + tname
        return False
    return True

def convertImgPdf2Text(sname):
    if not sname.strip().endswith(".pdf"): return False
    tname = "c_" + os.path.splitext(sname)[0] + ".txt"
    tpath = os.path.join(config.FILEPATH, tname)
    os.system("C: && cd C:\\ProgramData\\ABBYY\\SDK\\11\\FineReader Engine\\Samples\\Java\\Hello && call RunImgPdf2Text.cmd %s %s" % (sname, tname))
    if not os.path.isfile(tpath):
        print 'convert to pdf failed, file name:' + tname
        return False
    return True

def convertJpg2Xml(sname):
    # print sname, "=======0000000=======" , os.path.splitext(sname)[-1],os.path.splitext(sname)[-1] not in ["png", "jpg"]
    if os.path.splitext(sname)[-1] not in [".png", ".jpg"]: return False
    #print sname, "=======1111111======="
    tname = "c_" + os.path.splitext(sname)[0] + ".xml"
    tpath = os.path.join(config.FILEPATH, tname)
    os.system("C: && cd C:\\ProgramData\\ABBYY\\SDK\\11\\FineReader Engine\\Samples\\Java\\Hello && call RunImgImg2Xml.cmd %s %s" % (sname, tname))
    if not os.path.isfile(tpath):
        print 'convert to pdf failed, file name:' + tname
        return False
    return True

def hasConverted(fname):
    preFix = "c_" + os.path.splitext(fname)[0]
    return any([f for f in os.listdir(config.FILEPATH) if preFix in f])

def listPreConvertPdfFiles():
    reload(sys)
    needCvtFiles = []
    for f in os.listdir(config.FILEPATH):
        if f.startswith("c_") or hasConverted(f):continue
        ctime = os.path.getctime(os.path.join(config.FILEPATH, f)) 
        if int(time.time()) - int(ctime) > 60 * 60:continue
        if f in ESCAP_LIST: continue
        if any([cT for cT in config.SUPPORT_CONVERT_TYPE if cT in f]):
            needCvtFiles.append(f)
    return needCvtFiles

def sendStatus2Font(status):
    try:
        #requests.get("", timeout=10)
        pass
    except Exception as e:
        print traceback.format_exc()


while True:
    if not listPreConvertPdfFiles():
        print '--- sleep 1 sec ---'
        time.sleep(1)
        continue
    print '---start to convert ---'
    try:
        for f in listPreConvertPdfFiles():
            if f.startswith("imgpdf2textpdf"):
                status = convertImgPdf2TextPdf(f)
            if f.startswith("imgpdf2textfile"):
                status = convertImgPdf2Text(f)
            if f.startswith("img2xml"):
                status = convertJpg2Xml(f)
            if status is False:
                ESCAP_LIST.append(f)
                print ESCAP_LIST
            time.sleep(1)
    except Exception as e:
        print traceback.format_exc()