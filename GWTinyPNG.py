# -*- coding:UTF-8 -*-
import tinify
import os
import os.path
import shutil


tinify.key = "gYsZd2HqzSSRPy7QDGPbDcrXLPp5nn6V" # AppKey
fromFilePath = "/Users/admin/Desktop/origin" # 源路径
toFilePath = "/Users/admin/Desktop/new" # 输出路径

for root, dirs, files in os.walk(fromFilePath):
    for name in files:
        fileName, fileSuffix = os.path.splitext(name)
        toFullPath = toFilePath + root[len(fromFilePath):]
        toFullName = toFullPath + '/' + name
        if not os.path.exists(toFullPath):
            os.makedirs(toFullPath)
        if fileSuffix == '.png' or fileSuffix == '.jpg':
            
            source = tinify.from_file(root + '/' + name)
            source.to_file(toFullName)
            
            with open(toFullName, 'rb') as source:
                source_data = source.read()
                result_data = tinify.from_buffer(source_data).to_buffer()
        else:
            if fileSuffix == '.json':
                shutil.copy2(root + '/' + name, toFullName)
            else:
                print ("copied failed %s"%(root + '/' + name))
