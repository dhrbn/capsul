##########################################################################
# CAPSUL - Copyright (C) CEA, 2013
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

import os
from soma.undefined import undefined
from traits.api import Directory
from soma import config as soma_config

class BrainVISAConfig(object):
    def __init__(self, study_config):
        study_config.add_trait('shared_directory',Directory(
            undefined,
            output=False,
            desc='Study shared directory'))

        study_config.shared_directory = os.path.join(
            soma_config.BRAINVISA_SHARE, 'brainvisa-share-%s' \
                % soma_config.short_version)
