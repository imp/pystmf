#
# Copyright 2009 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
import ctypes as C

import libstmf

def getstate():
    _st = libstmf.stmfState()
    _stp = C.pointer(_st)

    r = libstmf.stmfGetState(_stp)

    return _st.operationalState, _st.configState
