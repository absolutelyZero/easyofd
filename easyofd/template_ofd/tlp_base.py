"""
#!/usr/bin/env python
-*- coding: utf-8 -*-
PROJECT_NAME: F:\opensource\easyofd\easyofd\template_ofd
CREATE_TIME: 2026-04-30 
E_MAIL: renoyuan@foxmail.com
AUTHOR: reno 
note:  
"""
class FileBase: 
    def __init__(self,*args,**kwargs):
        self.path = ""
        self.children = []
    
    def save(self,*args,**kwargs):
        # 1. 定义命名空间
        ns = {"ofd": "http://www.ofdspec.org/2016"}
        ET.register_namespace("ofd", ns["ofd"])

        # 2. 构建根节点
        root = ET.Element("ofd:OFD", {
            "DocType": "OFD",
            "Version": "1.0",
            "xmlns:ofd": ns["ofd"]
        })

        # 3. 添加DocBody节点
        doc_body = ET.SubElement(root, "ofd:DocBody")
        doc_info = ET.SubElement(doc_body, "ofd:DocInfo")

        # 4. 添加基础信息
        ET.SubElement(doc_info, "ofd:DocID").text = str(uuid4()).replace("-", "")
        ET.SubElement(doc_info, "ofd:CreationDate").text = "2025-04-01"
        ET.SubElement(doc_info, "ofd:Creator").text = "nuonuo"
        ET.SubElement(doc_info, "ofd:CreatorVersion").text = "1.0.0"
        ET.SubElement(doc_info, "ofd:ModDate").text = "2025-02-21"

        # 5. 添加CustomDatas（核心）
        custom_datas = ET.SubElement(doc_info, "ofd:CustomDatas")
        for name, value in custom_data_dict.items():
            ET.SubElement(custom_datas, "ofd:CustomData", {"Name": name}).text = str(value)

        # 6. 添加DocRoot（主文档路径）
        ET.SubElement(doc_body, "ofd:DocRoot").text = "Doc_0/Document.xml"

        # 7. 写入文件（带XML声明）
        tree = ET.ElementTree(root)
        with open(output_path, "wb") as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            tree.write(f, encoding="utf-8", xml_declaration=False)
        
class NodeBase :
    def __init__(self,*args,**kwargs):
        self.tag = ""
        self.id = ""
        self.text = ""
        self.children = []
        self.attrs = {}
        
    def add_child(self,child):
        self.children.append(child)
    
    def add_text(self,value):
        self.text = value
        
    def add_attribute(self,attr,value):
        self.attrs[attr] = value


class OFDReferenceManager:
    def __init__(self):
        # 所有带 ID 的节点都存在这里
        self.id_map: dict[str, OFDNode] = {}

    # 注册带ID的节点（自动提取ID）
    def register(self, node: OFDNode):
        if "ID" in node.attrs:
            node_id = node.attrs["ID"]
            self.id_map[node_id] = node

    # 通过ID查找节点
    def get(self, node_id: str) -> OFDNode | None:
        return self.id_map.get(node_id)
    

class OFDContext:
    def __init__(self):
        # 🔥 所有文件都在这里！统一维护！
        self.file_map: dict[str, OFFile] = {}

        # 所有带 ID 的节点
        self.id_map: dict[str, OFDNode] = {}

    # 注册文件
    def add_file(self, file: OFFile):
        self.file_map[file.file_path] = file

    # 通过路径找文件（你未来最常用的方法）
    def get_file(self, path: str) -> OFFile | None:
        return self.file_map.get(path)