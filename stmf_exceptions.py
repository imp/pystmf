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

class STMFError(Exception):
    status = libstmf.STMF_STATUS_ERROR

class STMFBusy(STMFError):
    status = libstmf.STMF_ERROR_BUSY

class STMFNotFound(STMFError):
    status = libstmf.STMF_ERROR_NOT_FOUND
