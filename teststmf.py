#!/bin/python2.6
# Copyright 2009 Grigale, Ltd. All rights reserved.
# Use is subject to license terms.
#

import stmf

print "Testing Python-STMF API"

print "Excersizing stmfGetState()"

operationalState, configState = stmf.getstate()

print operationalState, configState
