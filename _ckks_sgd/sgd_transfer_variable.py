#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2020 BE-GAIA. All Rights Reserved.
#


################################################################################
#
# AUTO GENERATED TRANSFER VARIABLE CLASS. DO NOT MODIFY
#
################################################################################

from lego.transfer_variable.base_transfer_variable import BaseTransferVariables


# noinspection PyAttributeOutsideInit
class VerticalSGDTransferVariable(BaseTransferVariables):
    def __init__(self, flowid=0):
        super().__init__(flowid)
        self.public_key = self._create_variable(name='public_key', src=['guest'], dst=['host'])
        self.y_host = self._create_variable(name='y_host', src=['host'], dst=['guest'])
        self.cipher_delta_y = self._create_variable(name='cipher_delta_y', src=['guest'], dst=['host'])
        