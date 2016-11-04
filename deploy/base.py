# -*- coding: utf-8 -*-

from __future__ import with_statement
from fabric.api import *
from fabric.utils import error
from abc import ABCMeta, abstractmethod

import os.path

class Base:
    __metaclass__ = ABCMeta
    node = dict()

    @abstractmethod
    def validate(self):
        """node varidation"""
        return

    @abstractmethod
    def start(self):
        """deploy script"""
        return
    
    @abstractmethod
    def test(self):
        """test script"""
        return

    def put_template(self, local, remote):
        """
        set template file
        """
        if os.path.exists(local) == False:
            error("File not found: %s" % local)
        put(local, remote)
