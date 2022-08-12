#!/usr/bin/env python
import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig



class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')



from setuptools import setup, find_packages
import pkg_resources
setup(
    name='python-sample-vscode-flask-tutorial',
    packages=find_packages('src', exclude=['test']),
    description='teste',
    version=pkg_resources.require("MyProject")[0].version,
    url='https://mmatapereira@dev.azure.com/mmatapereira/mmatapereira/_git/mmatapereira',
    author='Pereira, Miguel Pereira',
    author_email='m.mata.pereira@ctt.pt',
    keywords=['repirar','fundo','calma']
)