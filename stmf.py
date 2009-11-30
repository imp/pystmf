#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Copyright 2009 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
import ctypes as C

import libstmf

STMF_STATES = (
    "Logical Unit offline",
    "Logical Unit offlining",
    "Logical Unit online",
    "Logical Unit onlining",
    "Logical Unit unregistered",
    "Target Port offline",
    "Target Port offlining",
    "Target Port online",
    "Target Port onlining",
    "Service state online",
    "Service state offline",
    "Service state onlining",
    "Service state offlining",
    "Service state unknown",
    "Config state none",
    "Config state init",
    "Config state init done",
    "Config state unknown"
    )

def getstate():
    """
    Retrieves the current COMSTAR state
    """
    _st = libstmf.stmfState()
    _stp = C.pointer(_st)

    r = libstmf.stmfGetState(_stp)

    return _st.operationalState, _st.configState
