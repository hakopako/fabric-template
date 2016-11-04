# -*- coding:utf-8 -*-

from fabric.api import *
import os
import sys
import json

fabfile_path = os.path.realpath(__file__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(fabfile_path))))

def deploy(filepath, skip_test=False):
    puts("deploy_json=%s" % (filepath))
    tasks = __taskFactory(filepath, env)
    for t in tasks:
        t.start()

    if skip_test:
        puts("Skipped Test.")
        return

    for t in tasks:
        t.test()


def test(filepath=''):
    puts("test_json=%s" % (filepath))
    tasks = __taskFactory(filepath, env)
    for t in tasks:
        t.test()


def __taskFactory(fp, e):
    f = open(fp)
    data = json.load(f)
    f.close()

    hostname = e.host
    hostgroup = re.sub(r'[0-9]{4}$', "", hostname)
    runenv = __get_env(hostgroup)
    task_stack = []

    for recipe in data["deploy"]:
        m = recipe.replace("./", "").replace("/", ".")
        module_name = os.path.basename(recipe)
        components = module_name.split('_')
        klassname = "".join(x.title() for x in components[0:])
        mod = __import__(m, fromlist=[klassname])
        klass = getattr(mod, klassname)
        a = klass()
        a.node.update({"hostname": hostname})
        a.node.update(data)
        a.validate()
        task_stack.append(a)
    return task_stack

