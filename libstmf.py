#
# Copyright 2009 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
import ctypes as C

STMF_LOGICAL_UNIT_OFFLINE	= 0
STMF_LOGICAL_UNIT_OFFLINING	= 1
STMF_LOGICAL_UNIT_ONLINE	= 2
STMF_LOGICAL_UNIT_ONLINING	= 3
STMF_LOGICAL_UNIT_UNREGISTERED	= 4
STMF_TARGET_PORT_OFFLINE	= 5
STMF_TARGET_PORT_OFFLINING	= 6
STMF_TARGET_PORT_ONLINE		= 7
STMF_TARGET_PORT_ONLINING	= 8
STMF_SERVICE_STATE_ONLINE	= 9
STMF_SERVICE_STATE_OFFLINE	= 10
STMF_SERVICE_STATE_ONLINING	= 11
STMF_SERVICE_STATE_OFFLINING	= 12
STMF_SERVICE_STATE_UNKNOWN	= 13
STMF_CONFIG_STATE_NONE		= 14
STMF_CONFIG_STATE_INIT		= 15
STMF_CONFIG_STATE_INIT_DONE	= 16
STMF_CONFIG_STATE_UNKNOWN	= 17

STMF_IDENT_LENGTH		= 255

# API status return values
STMF_STATUS_SUCCESS		= 0x0000
STMF_STATUS_ERROR		= 0x8000
STMF_ERROR_BUSY			= (STMF_STATUS_ERROR | 0x01)
STMF_ERROR_NOT_FOUND		= (STMF_STATUS_ERROR | 0x02)
STMF_ERROR_MEMBER_NOT_FOUND	= (STMF_STATUS_ERROR | 0x03)
STMF_ERROR_GROUP_NOT_FOUND	= (STMF_STATUS_ERROR | 0x04)
STMF_ERROR_PERM			= (STMF_STATUS_ERROR | 0x05)
STMF_ERROR_NOMEM		= (STMF_STATUS_ERROR | 0x06)
STMF_ERROR_INVALID_ARG		= (STMF_STATUS_ERROR | 0x07)
STMF_ERROR_EXISTS		= (STMF_STATUS_ERROR | 0x08)
STMF_ERROR_SERVICE_NOT_FOUND	= (STMF_STATUS_ERROR | 0x09)
STMF_ERROR_SERVICE_ONLINE	= (STMF_STATUS_ERROR | 0x0a)
STMF_ERROR_SERVICE_OFFLINE	= (STMF_STATUS_ERROR | 0x0b)
STMF_ERROR_GROUP_IN_USE		= (STMF_STATUS_ERROR | 0x0c)
STMF_ERROR_LUN_IN_USE		= (STMF_STATUS_ERROR | 0x0d)
STMF_ERROR_VE_CONFLICT		= (STMF_STATUS_ERROR | 0x0e)
STMF_ERROR_CONFIG_NONE		= (STMF_STATUS_ERROR | 0x0f)
STMF_ERROR_SERVICE_DATA_VERSION = (STMF_STATUS_ERROR | 0x10)
STMF_ERROR_INVALID_HG		= (STMF_STATUS_ERROR | 0x11)
STMF_ERROR_INVALID_TG		= (STMF_STATUS_ERROR | 0x12)
STMF_ERROR_PROV_DATA_STALE	= (STMF_STATUS_ERROR | 0x13)
STMF_ERROR_NO_PROP		= (STMF_STATUS_ERROR | 0x14)
STMF_ERROR_NO_PROP_VAL		= (STMF_STATUS_ERROR | 0x15)
STMF_ERROR_MISSING_PROP_VAL	= (STMF_STATUS_ERROR | 0x16)
STMF_ERROR_INVALID_BLOCKSIZE	= (STMF_STATUS_ERROR | 0x17)
STMF_ERROR_FILE_ALREADY		= (STMF_STATUS_ERROR | 0x18)
STMF_ERROR_INVALID_PROPSIZE	= (STMF_STATUS_ERROR | 0x19)
STMF_ERROR_INVALID_PROP		= (STMF_STATUS_ERROR | 0x20)
STMF_ERROR_PERSIST_TYPE		= (STMF_STATUS_ERROR | 0x21)
STMF_ERROR_TG_ONLINE		= (STMF_STATUS_ERROR | 0x22)
STMF_ERROR_ACCESS_STATE_SET	= (STMF_STATUS_ERROR | 0x23)
STMF_ERROR_NO_PROP_STANDBY	= (STMF_STATUS_ERROR | 0x24)
STMF_ERROR_POST_MSG_FAILED	= (STMF_STATUS_ERROR | 0x25)
STMF_ERROR_DOOR_INSTALLED	= (STMF_STATUS_ERROR | 0x26)

# Failures for stmfCreateLu
STMF_ERROR_FILE_IN_USE		= (STMF_STATUS_ERROR | 0x100)
STMF_ERROR_INVALID_BLKSIZE	= (STMF_STATUS_ERROR | 0x101)
STMF_ERROR_GUID_IN_USE		= (STMF_STATUS_ERROR | 0x102)
STMF_ERROR_META_FILE_NAME	= (STMF_STATUS_ERROR | 0x103)
STMF_ERROR_DATA_FILE_NAME	= (STMF_STATUS_ERROR | 0x104)
STMF_ERROR_SIZE_OUT_OF_RANGE	= (STMF_STATUS_ERROR | 0x105)
STMF_ERROR_LU_BUSY		= (STMF_STATUS_ERROR | 0x106)
STMF_ERROR_META_CREATION	= (STMF_STATUS_ERROR | 0x107)
STMF_ERROR_FILE_SIZE_INVALID	= (STMF_STATUS_ERROR | 0x108)
STMF_ERROR_WRITE_CACHE_SET	= (STMF_STATUS_ERROR | 0x109)

# libstmf datastructure definitions

class stmfState(C.Structure):
    _fields_ = [("operationalState", C.c_int),
                ("configState", C.c_int)]

_libstmf = C.CDLL("libstmf.so.1")

# API callable functions

# int stmfGetState(stmfState *);
stmfGetState = _libstmf.stmfGetState
stmfGetState.argtypes = [C.POINTER(stmfState)]


# int stmfAddToHostGroup(stmfGroupName *hostGroupName, stmfDevid *name);
stmfAddToHostGroup = _libstmf.stmfAddToHostGroup

# int stmfAddToTargetGroup(stmfGroupName *targetGroupName,
#     stmfDevid *targetName);
stmfAddToTargetGroup = _libstmf.stmfAddToTargetGroup

# int stmfAddViewEntry(stmfGuid *lu, stmfViewEntry *viewEntry);
stmfAddViewEntry = _libstmf.stmfAddViewEntry

# int stmfClearProviderData(char *providerName, int providerType);
stmfClearProviderData = _libstmf.stmfClearProviderData

# int stmfCreateHostGroup(stmfGroupName *hostGroupName);
stmfCreateHostGroup = _libstmf.stmfCreateHostGroup

# int stmfCreateLu(luResource hdl, stmfGuid *luGuid);
stmfCreateLu = _libstmf.stmfCreateLu

# int stmfCreateLuResource(uint16_t dType, luResource *hdl);
stmfCreateLuResource = _libstmf.stmfCreateLuResource

# int stmfCreateTargetGroup(stmfGroupName *targetGroupName);
stmfCreateTargetGroup = _libstmf.stmfCreateTargetGroup

# int stmfDeleteHostGroup(stmfGroupName *hostGroupName);
stmfDeleteHostGroup = _libstmf.stmfDeleteHostGroup

# int stmfDeleteLu(stmfGuid *luGuid);
stmfDeleteLu = _libstmf.stmfDeleteLu

# int stmfDeleteTargetGroup(stmfGroupName *targetGroupName);
stmfDeleteTargetGroup = _libstmf.stmfDeleteTargetGroup

# void stmfDestroyProxyDoor(int hdl);
stmfDestroyProxyDoor = _libstmf.stmfDestroyProxyDoor

# int stmfDevidFromIscsiName(char *iscsiName, stmfDevid *devid);
stmfDevidFromIscsiName = _libstmf.stmfDevidFromIscsiName

# int stmfDevidFromWwn(uchar_t wwn[8], stmfDevid *devid);
stmfDevidFromWwn = _libstmf.stmfDevidFromWwn

# int stmfFreeLuResource(luResource hdl);
stmfFreeLuResource = _libstmf.stmfFreeLuResource

# void stmfFreeMemory(void *);
stmfFreeMemory = _libstmf.stmfFreeMemory

# int stmfGetAluaState(boolean_t *enabled, uint32_t *node);
stmfGetAluaState = _libstmf.stmfGetAluaState

# int stmfGetHostGroupList(stmfGroupList **initiatorGroupList);
stmfGetHostGroupList = _libstmf.stmfGetHostGroupList

# int stmfGetHostGroupMembers(stmfGroupName *hostGroupName,
#     stmfGroupProperties **groupProperties);
stmfGetHostGroupMembers = _libstmf.stmfGetHostGroupMembers

# int stmfGetLocalPortProviderList(stmfProviderList **localPortProviderList);
# XXX stmfGetLocalPortProviderList = _libstmf.stmfGetLocalPortProviderList

# int stmfGetLocalPortProviderProperties(stmfProviderName *providerName,
#     stmfLocalPortProviderProperties *providerProperties);
# XXX stmfGetLocalPortProviderProperties = _libstmf.stmfGetLocalPortProviderProperties

# int stmfGetLogicalUnitList(stmfGuidList **logicalUnitList);
stmfGetLogicalUnitList = _libstmf.stmfGetLogicalUnitList

# int stmfGetLogicalUnitProperties(stmfGuid *logicalUnit,
#     stmfLogicalUnitProperties *logicalUnitProps);
stmfGetLogicalUnitProperties = _libstmf.stmfGetLogicalUnitProperties

# int stmfGetLogicalUnitProviderList(stmfProviderList **logicalUnitProviderList);
# XXX stmfGetLogicalUnitProviderList = _libstmf.stmfGetLogicalUnitProviderList

# int stmfGetLogicalUnitProviderProperties(stmfProviderName *providerName,
#     stmfLogicalUnitProviderProperties *providerProperties);
# XXX stmfGetLogicalUnitProviderProperties = _libstmf.stmfGetLogicalUnitProviderProperties

# int stmfGetLuProp(luResource hdl, uint32_t propType, char *prop,
#     size_t *propLen);
stmfGetLuProp = _libstmf.stmfGetLuProp

# int stmfGetLuResource(stmfGuid *luGuid, luResource *hdl);
stmfGetLuResource = _libstmf.stmfGetLuResource

# int stmfGetPersistMethod(uint8_t *persistType, boolean_t serviceState);
stmfGetPersistMethod = _libstmf.stmfGetPersistMethod

# int stmfGetProviderData(char *providerName, nvlist_t **nvl, int providerType);
stmfGetProviderData = _libstmf.stmfGetProviderData

# int stmfGetProviderDataProt(char *providerName, nvlist_t **nvl,
#     int providerType, uint64_t *setToken);
stmfGetProviderDataProt = _libstmf.stmfGetProviderDataProt

# int stmfGetSessionList(stmfDevid *target, stmfSessionList **sessionList);
stmfGetSessionList = _libstmf.stmfGetSessionList

# int stmfGetTargetGroupList(stmfGroupList **targetGroupList);
stmfGetTargetGroupList = _libstmf.stmfGetTargetGroupList

# int stmfGetTargetGroupMembers(stmfGroupName *targetGroupName,
#     stmfGroupProperties **groupProperties);
stmfGetTargetGroupList = _libstmf.stmfGetTargetGroupList

# int stmfGetTargetList(stmfDevidList **targetList);
stmfGetTargetList = _libstmf.stmfGetTargetList

# int stmfGetTargetProperties(stmfDevid *target,
#     stmfTargetProperties *targetProps);
stmfGetTargetProperties = _libstmf.stmfGetTargetProperties

# int stmfGetViewEntryList(stmfGuid *lu, stmfViewEntryList **viewEntryList);
stmfGetViewEntryList = _libstmf.stmfGetViewEntryList

# int stmfImportLu(uint16_t dType, char *fname, stmfGuid *luGuid);
stmfImportLu = _libstmf.stmfImportLu

# int stmfInitProxyDoor(int *hdl, int fd);
stmfInitProxyDoor = _libstmf.stmfInitProxyDoor

# int stmfLoadConfig(void);
stmfLoadConfig = _libstmf.stmfLoadConfig

# int stmfLuStandby(stmfGuid *luGuid);
stmfLuStandby = _libstmf.stmfLuStandby

# int stmfModifyLu(stmfGuid *luGuid, uint32_t prop, const char *propVal);
stmfModifyLu = _libstmf.stmfModifyLu

# int stmfModifyLuByFname(uint16_t dType, const char *fname, uint32_t prop,
#     const char *propVal);
stmfModifyLuByFname = _libstmf.stmfModifyLuByFname

# int stmfOffline(void);
stmfOffline = _libstmf.stmfOffline

# int stmfOfflineTarget(stmfDevid *devid);
stmfOfflineTarget = _libstmf.stmfOfflineTarget

# int stmfOfflineLogicalUnit(stmfGuid *logicalUnit);
stmfOfflineLogicalUnit = _libstmf.stmfOfflineLogicalUnit

# int stmfOnline(void);
stmfOnline = _libstmf.stmfOnline

# int stmfOnlineTarget(stmfDevid *devid);
stmfOnlineTarget = _libstmf.stmfOnlineTarget

# int stmfOnlineLogicalUnit(stmfGuid *logicalUnit);
stmfOnlineLogicalUnit = _libstmf.stmfOnlineLogicalUnit

# int stmfPostProxyMsg(int hdl, void *buf, uint32_t buflen);
stmfPostProxyMsg = _libstmf.stmfPostProxyMsg

# int stmfRemoveFromHostGroup(stmfGroupName *hostGroupName,
#     stmfDevid *initiatorName);
stmfRemoveFromHostGroup = _libstmf.stmfRemoveFromHostGroup

# int stmfRemoveFromTargetGroup(stmfGroupName *targetGroupName,
#     stmfDevid *targetName);
stmfRemoveFromTargetGroup = _libstmf.stmfRemoveFromTargetGroup

# int stmfRemoveViewEntry(stmfGuid *lu, uint32_t viewEntryIndex);
stmfRemoveViewEntry = _libstmf.stmfRemoveViewEntry

# int stmfSetAluaState(boolean_t enabled, uint32_t node);
stmfSetAluaState = _libstmf.stmfSetAluaState

# int stmfSetLuProp(luResource hdl, uint32_t propType, const char *propVal);
stmfSetLuProp = _libstmf.stmfSetLuProp

# int stmfSetPersistMethod(uint8_t persistType, boolean_t serviceSet);
stmfSetPersistMethod = _libstmf.stmfSetPersistMethod

# int stmfSetProviderData(char *providerName, nvlist_t *nvl, int providerType);
stmfSetProviderData = _libstmf.stmfSetProviderData

# int stmfSetProviderDataProt(char *providerName, nvlist_t *nvl,
#     int providerType, uint64_t *setToken);
stmfSetProviderDataProt = _libstmf.stmfSetProviderDataProt

# int stmfValidateView(stmfViewEntry *viewEntry);
stmfValidateView = _libstmf.stmfValidateView


