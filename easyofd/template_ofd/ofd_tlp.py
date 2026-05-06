"""
#!/usr/bin/env python
-*- coding: utf-8 -*-
PROJECT_NAME: F:\opensource\easyofd\easyofd\template_ofd
CREATE_TIME: 2026-04-30 
E_MAIL: renoyuan@foxmail.com
AUTHOR: reno 
note:  
"""

from tlp_base import FileBase, NodeBase

# 14. OFD 总文件
class OFDFile(FileBase):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.ofd   = OFDLabel()

class OFDNode(NodeBase):
    def __init__(self):
        self.doc_type = "OFD"    # DocType 属性
        self.version = "renoyuan"     # Version 属性
        self.doc_body = DocBody()# <ofd:DocBody>