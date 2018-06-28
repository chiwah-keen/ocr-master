#!/usr/bin/env python
# coding: utf-8

import os
from config_loader import load_global_conf

conf_dict = load_global_conf()


# '''mysql configuration'''
# MYSQL_SERVER = conf_dict["mysql_host"]
# MYSQL_USER = conf_dict["mysql_user"]
# MYSQL_PORT = int(conf_dict["mysql_port"])
# MYSQL_PASSWORD = conf_dict["mysql_pwd"]
# MYSQL_TYPE = conf_dict["mysql_type"]
# MYSQL_DB_MESSAGE = "siterec_center"
#
#
# '''redis configuration'''
# REDIS_IP = conf_dict["redis_online_host"]
# REDIS_PORT = conf_dict["redis_online_port"]
# REDIS_PASSWD = conf_dict["redis_online_pwd"]
# REDIS_TYPE = conf_dict["redis_online_type"]

LISTEN_PORT = 8001

UPLOADPAGE = '''
            <html>
              <head><title>Upload File</title></head>
              <body>
                   <form action='/uploadimgpdf' enctype="multipart/form-data" method='post'>
                   <input type='file' name='file'/><br/>
                   <input type='submit' value='submit'/>
                   </form>
              </body>
            </html>
            '''


UPLOADPDFPAGE = '''
            <html>
              <head><title>Upload PDF File</title></head>
              <body>
                   <form action='/upload' enctype="multipart/form-data" method='post'>
                   <input type='file' name='file'/><br/>
                   <input type='submit' value='submit'/>
                   </form>
              </body>
            </html>
            '''

settings = {
    'template_path': os.path.join('', 'templates')
}

FILEPATH = "D:\\datagrand\\pdffiles"
SUPPORT_CONVERT_TYPE = ["imgpdf2textpdf", "imgpdf2textfile", "img2xml"]

SUPPORT_CONVERT_TYPE_MAP = {
    "imgpdf2textpdf": ".pdf", 
    "imgpdf2textfile": ".txt", 
    "img2xml": ".xml"
}