#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import traceback, os, json, os, uuid, time
from conf import config
from base import BaseHandler


class DownloadFileHandler(BaseHandler):
    def get(self):
        try:
            filename = self.get_argument('f', '')
            spath = os.path.join(config.FILEPATH, filename.replace("c_", ""))
            tpath = os.path.join(config.FILEPATH, filename)
            if not filename:
                return self.send_status_message(-1, '图片名称不能为空!')
            print '---- file name:', spath, os.path.isfile(spath)
            if os.path.isfile(spath) or os.path.isfile(tpath):
                print '----- will downlad pdf file -------'
                self.log.info('start to download pdf file!')
                self.set_header('Content-Type', 'application/octet-stream')
                self.set_header('Content-Disposition', 'attachment; filename=' + filename)
                with open(os.path.join(config.FILEPATH, filename), 'rb') as f:
                    while True:
                        data = f.read(2048)
                        if not data:
                            break
                        self.write(data)
                return self.finish()
            if os.path.isfile(spath) and not os.path.isfile(tpath):
                return self.send_status_message(-1, '图片识别中...')    
            if not os.path.isfile(spath) and not os.path.isfile(tpath):
                return self.send_status_message(-1, '图片不存在...可能已经被清理')            
            return self.send_status_message(-1, '图片限制下载')
        except Exception as e:
            self.send_status_message(-3, traceback.format_exc())
            self.log.error(traceback.format_exc())

    def post(self):
        try:
            self.send_status_message(-1, 'not allowed')
        except Exception as e:
            self.log.error(traceback.format_exc())
            self.send_status_message(-2, traceback.format_exc())
            print traceback.format_exc()