from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

authors = [Author('Zachary LaVere', 'zlavere@westga.edu')]
description = 'Systems Programming(CS3280) Project 1 - Regular Expressions with IP Addresses, Subnet Masks'
name = "zlavere_project1_regex"
default_task = ['clean', 'analyze', 'publish']


@init
def set_properties(project):
    pass
