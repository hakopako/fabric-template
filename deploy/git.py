# -*- coding: utf-8 -*-

from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, sudo
from fabric.contrib.console import confirm
from fabric.utils import error
from deploy.base import Base


class Git(Base):
    def validate(self):
        conf = self.node["git"]
        if "repo_url" not in conf: error("Git.repo_url is required.")
        if "dir_path" not in conf: error("Git.dir_path is required.")
        if "barnch" not in conf: error("Git.barnch is required.")
        if "proxy_host" not in conf: conf["proxy_host"] = ""
        if "proxy_port" not in conf: conf["proxy_port"] = ""
        self.node["git"] = conf

    def start(self):
        if self.node["git"]["proxy_host"] != "": 
            host = self.node["git"]["proxy_host"]
            port =  self.node["git"]["proxy_port"]
        with settings(warn_only=True):
            run("git config --global --unset-all http.proxy")
            run("git config --global --unset-all https.proxy")
            sudo("git config --global --add http.proxy http://%s:%s" % (host, port))
            sudo("git config --global --add https.proxy http://%s:%s" % (host, port))
        with settings(warn_only=True):
            if run("test -d %s" % self.node["git"]["dir_path"]).failed:
                run("git clone %s %s" % (self.node["git"]["repo_url"], self.node["git"]["dir_path"]))
        with cd(self.node["git"]["dir_path"]):
            sudo("git checkout master")
            sudo("git pull --prune")
            sudo("git checkout %s" % self.node["git"]["barnch"])

    def test(self):
        return
