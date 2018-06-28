#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import traceback, os, json, os, uuid, time
from conf import config
from base import BaseHandler


class UploadImagesPDFHandler(BaseHandler):
    def get(self):
        try:
            self.write(config.UPLOADPDFPAGE)
        except Exception as e:
            self.send_status_message(-3, traceback.format_exc())
            self.log.error(traceback.format_exc())

    def post(self):
        try:
            upload_path = config.FILEPATH
            file_metas = self.request.files.get('file', None) or self.request.files.get('body', '')
            if not file_metas:
                return self.send_status_message(-2, 'invalid file content or file name.')
            meta = file_metas[0]
            cT = meta.get('type', 'ImgPdf2TextPdf')
            if cT not in config.SUPPORT_CONVERT_TYPE:
                return self.send_status_message(-2, 'only support types:' + ",".join(config.SUPPORT_CONVERT_TYPE))
            uname_pfix = str(uuid.uuid1())
            sfile = cT + "_" + uname_pfix + os.path.splitext(meta['filename'])[1]  # 
            with open(os.path.join(upload_path, sfile), 'wb') as f:
                f.write(meta['body'])
                f.flush()
            self.send_data("/download?f=c_"+sfile)
            self.finish()
        except Exception as e:
            self.log.error(traceback.format_exc())
            self.send_status_message(-2, traceback.format_exc())
            print traceback.format_exc()


class UploadApiHandler(BaseHandler):
    def get(self):
        try:
            self.send_json({"type":"|".join(config.SUPPORT_CONVERT_TYPE) ,"filename":"xxx.pdf", "content": "xxx"})
        except Exception as e:
            self.send_status_message(-3, traceback.format_exc())
            self.log.error(traceback.format_exc())

    def post(self, cvttype):
        try:
            upload_path = config.FILEPATH
            filename = self.get_argument("filename", "")
            content = self.request.body
            if not filename or not content:
                return self.send_status_message(-2, 'invalid file content or file name.')
            if not filename or not cvttype or cvttype not in config.SUPPORT_CONVERT_TYPE:
                return self.send_status_message(-2, 'invalid filename or convert type')
            uname_pfix = str(uuid.uuid1()).replace("-", "0")
            sfile = cvttype + "_" + uname_pfix + os.path.splitext(filename)[1]  # 
            with open(os.path.join(upload_path, sfile), 'wb') as f:
                f.write(content)
                f.flush()
            self.send_data("/download?f=c_"+ os.path.splitext(sfile)[0] + config.SUPPORT_CONVERT_TYPE_MAP.get(cvttype,".pdf"))
            self.finish()
        except Exception as e:
            self.log.error(traceback.format_exc())
            self.send_status_message(-2, traceback.format_exc())
            print traceback.format_exc()