# coding: utf-8

import os
import yaml

from python.pycti.opencti import OpenCTI

# Load configuration
config = yaml.load(open(os.path.dirname(__file__) + '/config.yml'))

# File to import
file_to_import = config['mitre']['repository_path_cti'] + '/enterprise-attack/enterprise-attack.json'
#file_to_import = './exports/bundle.json'

# OpenCTI initialization
opencti = OpenCTI(config['opencti']['api_url'], config['opencti']['api_key'], config['opencti']['verbose'])

# Import the bundle
opencti.stix2_import_bundle(file_to_import)
