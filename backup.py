# -*- coding: utf-8 -*-
idir = u'C:\Users\Public\Pictures\デジカメ\iPad'
odir = u'Z:\photo'

import os, shutil

def copy(ipath,odir):
    fname = os.path.basename(ipath)
    opath = os.path.join(odir,fname)
    if not os.path.exists(opath):
        shutil.copy2(ipath,opath)

def copytree(src,odir):
    if os.path.isdir(src):
        for sub in os.listdir(src):
            path = os.path.join(src,sub)
            copytree(path,odir)
    elif os.path.isfile(src):
        copy(src,odir)

copytree(idir,odir)
