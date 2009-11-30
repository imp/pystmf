#!/bin/python2.6
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Copyright 2009 Grigale, Ltd. All rights reserved.
# Use is subject to license terms.
#

import stmf

print "Testing Python-STMF API"

print "Excersizing stmfGetState()"

operationalState, configState = stmf.getstate()

print " STMF service : %s" % stmf.STMF_STATES[operationalState]
print " STMF config  : %s" % stmf.STMF_STATES[configState]
