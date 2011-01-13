#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Copyright 2009-2011 Grigale Ltd. All rights reserved.
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

class STMFMemberNotFound(STMFError):
    status = libstmf.STMF_ERROR_MEMBER_NOT_FOUND

class STMFGroupNotFound(STMFError):
    status = libstmf.STMF_ERROR_GROUP_NOT_FOUND

class STMFPerm(STMFError):
    status = libstmf.STMF_ERROR_PERM

class STMFNoMem(STMFError):
    status = libstmf.STMF_ERROR_NOMEM

class STMFInvalidArg(STMFError):
    status = libstmf.STMF_ERROR_INVALID_ARG

class STMFExists(STMFError):
    status = libstmf.STMF_ERROR_EXISTS

class STMFServiceNotFound(STMFError):
    status = libstmf.STMF_ERROR_SERVICE_NOT_FOUND

class STMFServiceOnline(STMFError):
    status = libstmf.STMF_ERROR_SERVICE_ONLINE

class STMFServiceOffline(STMFError):
    status = libstmf.STMF_ERROR_SERVICE_OFFLINE

class STMFGroupInUse(STMFError):
    status = libstmf.STMF_ERROR_GROUP_IN_USE

class STMFLunInUse(STMFError):
    status = libstmf.STMF_ERROR_LUN_IN_USE

