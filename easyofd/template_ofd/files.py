"""
#!/usr/bin/env python
-*- coding: utf-8 -*-
PROJECT_NAME: F:\opensource\easyofd\easyofd\template_ofd
CREATE_TIME: 2026-04-24 
E_MAIL: renoyuan@foxmail.com
AUTHOR: reno 
note:  
"""

"""
OFD
  └── DocBody
       ├── DocInfo
       │     ├── DocID
       │     ├── Author
       │     ├── CreationDate
       │     └── ModDate
       └── DocRoot
       
"""

        



        
# 13. 文档
class Document(FileBase):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.pages = []          # List<Page>
        self.fonts = []         # List<Font>
        self.medias = []        # List<MultiMedia>
        self.signatures = []    # List<Signature>

