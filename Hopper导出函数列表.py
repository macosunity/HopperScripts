# -*- coding: utf-8 -*-

import re
import gc
import os

document = Document.getCurrentDocument()
segment = document.getSegmentByName('__TEXT')

app_name = document.getExecutableFilePath().split('/')[-1]
path = os.path.expanduser('~/LabelsDecompiles/' + app_name)
if not os.path.exists(path):
    os.makedirs(path)


def get_file_path(class_name):
    return '%s/%s.txt'%(path, class_name)


file_path = get_file_path('identify')
file = open(file_path, 'w')
file.write('')
file.close()
file = open(file_path, 'a')

def start_decompile():
    classes = {}
    for i in range(segment.getProcedureCount()):
        procedure = segment.getProcedureAtIndex(i)
        address = procedure.getEntryPoint()

        label_name = segment.getNameAtAddress(address)
        file.write(label_name+'\n')

    del codes
    gc.collect()
    print 'Done!'

message = 'Please choose the decompile type:'
buttons = ['Decompile All Classes', 'Cancel']
button_index = document.message(message, buttons)
if button_index == 0:
    start_decompile()
elif button_index == 1:
    print 'Cancel decompile!'