# -*- coding: utf-8 -*-

from __future__ import with_statement
from fabric.api import *
from fabric.utils import error
from fabric.contrib.console import confirm
from deploy.base import Base

class Default(Base):
    def validate(self):
        conf = self.node["project_a"]
        if "owner" not in conf: error("project_a.conf.owner is required.")
        if "group" not in conf: error("project_a.conf.group is required.")
        if "templates" not in conf: conf["templates"] = []

    def start(self):
        conf = self.node["project_a"]
        for file_path in conf["templates"]:
            base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
            local_path = "%s/templates%s" % (base_path, file_path)
            self.put_template(local_path, file_path)
            sudo("chown %s:%s %s" %(conf["owner"], conf["group"], file_path))

    def test(self):
        return
