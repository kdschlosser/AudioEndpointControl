# -*- coding: mbcs -*-
#typelib_path = u'C:\\Program Files (x86)\\Util\\EventGhost\\plugins\\GameMenu\\AudioEndpointControl\\mmdeviceapi.tlb'
typelib_path = u'mmdeviceapi.tlb'
_lcid = 0 # change this if required
from ctypes import *
from ctypes.wintypes import _ULARGE_INTEGER
from comtypes.automation import IDispatch
from comtypes.typeinfo import tagSYSKIND
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import _FILETIME
#import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
import stdole
WSTRING = c_wchar_p
from ctypes.wintypes import _LARGE_INTEGER
from ctypes.wintypes import VARIANT_BOOL
from comtypes.automation import SCODE
from comtypes import BSTR
from comtypes import IUnknown
from comtypes import GUID
STRING = c_char_p
from comtypes.typeinfo import tagTLIBATTR
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from ctypes.wintypes import DWORD
from comtypes.typeinfo import tagARRAYDESC
from comtypes.typeinfo import IRecordInfo
from comtypes.typeinfo import tagVARDESC
from comtypes.typeinfo import tagFUNCDESC
from comtypes.typeinfo import tagTYPEDESC
from comtypes.typeinfo import tagIDLDESC
from comtypes.typeinfo import ITypeInfo
from comtypes.typeinfo import tagTYPEKIND
from comtypes.typeinfo import tagCALLCONV
from comtypes import CoClass
from comtypes.typeinfo import tagPARAMDESC
from comtypes.automation import VARIANT
from comtypes.typeinfo import tagTYPEDESC
from comtypes.typeinfo import ITypeLib
from comtypes.automation import tagINVOKEKIND
from comtypes.typeinfo import tagFUNCKIND
from comtypes.typeinfo import tagTYPEATTR
from comtypes.typeinfo import tagPARAMDESCEX
from comtypes.typeinfo import tagSAFEARRAYBOUND
from comtypes.typeinfo import tagSAFEARRAYBOUND
from comtypes.typeinfo import ITypeComp
from comtypes.typeinfo import tagELEMDESC
from comtypes.typeinfo import tagVARKIND
from comtypes.typeinfo import ULONG_PTR
from comtypes.typeinfo import tagDESCKIND
from comtypes.automation import VARIANT


class tagCAUH(Structure):
    pass
tagCAUH._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_ULARGE_INTEGER)),
]
assert sizeof(tagCAUH) == 8, sizeof(tagCAUH)
assert alignment(tagCAUH) == 4, alignment(tagCAUH)
class _wireSAFEARR_DISPATCH(Structure):
    pass
_wireSAFEARR_DISPATCH._fields_ = [
    ('Size', c_ulong),
    ('apDispatch', POINTER(POINTER(IDispatch))),
]
assert sizeof(_wireSAFEARR_DISPATCH) == 8, sizeof(_wireSAFEARR_DISPATCH)
assert alignment(_wireSAFEARR_DISPATCH) == 4, alignment(_wireSAFEARR_DISPATCH)
class tagCACY(Structure):
    pass
tagCACY._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_longlong)),
]
assert sizeof(tagCACY) == 8, sizeof(tagCACY)
assert alignment(tagCACY) == 4, alignment(tagCACY)
class tagSTATSTG(Structure):
    pass
tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', stdole.GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
assert sizeof(tagSTATSTG) == 72, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)
class __MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001(Union):
    pass
class tagCLIPDATA(Structure):
    pass
class tagBSTRBLOB(Structure):
    pass
tagBSTRBLOB._fields_ = [
    ('cbSize', c_ulong),
    ('pData', POINTER(c_ubyte)),
]
assert sizeof(tagBSTRBLOB) == 8, sizeof(tagBSTRBLOB)
assert alignment(tagBSTRBLOB) == 4, alignment(tagBSTRBLOB)
class tagBLOB(Structure):
    pass
tagBLOB._fields_ = [
    ('cbSize', c_ulong),
    ('pBlobData', POINTER(c_ubyte)),
]
assert sizeof(tagBLOB) == 8, sizeof(tagBLOB)
assert alignment(tagBLOB) == 4, alignment(tagBLOB)
class ISequentialStream(stdole.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IStorage(stdole.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000B-0000-0000-C000-000000000046}')
    _idlflags_ = []
class tagVersionedStream(Structure):
    pass
class _wireSAFEARRAY(Structure):
    pass
wirePSAFEARRAY = POINTER(POINTER(_wireSAFEARRAY))
class tagCAC(Structure):
    pass
tagCAC._fields_ = [
    ('cElems', c_ulong),
    ('pElems', STRING),
]
assert sizeof(tagCAC) == 8, sizeof(tagCAC)
assert alignment(tagCAC) == 4, alignment(tagCAC)
class tagCAUB(Structure):
    pass
tagCAUB._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ubyte)),
]
assert sizeof(tagCAUB) == 8, sizeof(tagCAUB)
assert alignment(tagCAUB) == 4, alignment(tagCAUB)
class tagCAI(Structure):
    pass
tagCAI._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_short)),
]
assert sizeof(tagCAI) == 8, sizeof(tagCAI)
assert alignment(tagCAI) == 4, alignment(tagCAI)
class tagCAUI(Structure):
    pass
tagCAUI._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ushort)),
]
assert sizeof(tagCAUI) == 8, sizeof(tagCAUI)
assert alignment(tagCAUI) == 4, alignment(tagCAUI)
class tagCAL(Structure):
    pass
tagCAL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_int)),
]
assert sizeof(tagCAL) == 8, sizeof(tagCAL)
assert alignment(tagCAL) == 4, alignment(tagCAL)
class tagCAUL(Structure):
    pass
tagCAUL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_ulong)),
]
assert sizeof(tagCAUL) == 8, sizeof(tagCAUL)
assert alignment(tagCAUL) == 4, alignment(tagCAUL)
class tagCAH(Structure):
    pass
tagCAH._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_LARGE_INTEGER)),
]
assert sizeof(tagCAH) == 8, sizeof(tagCAH)
assert alignment(tagCAH) == 4, alignment(tagCAH)
class tagCAFLT(Structure):
    pass
tagCAFLT._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_float)),
]
assert sizeof(tagCAFLT) == 8, sizeof(tagCAFLT)
assert alignment(tagCAFLT) == 4, alignment(tagCAFLT)
class tagCADBL(Structure):
    pass
tagCADBL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_double)),
]
assert sizeof(tagCADBL) == 8, sizeof(tagCADBL)
assert alignment(tagCADBL) == 4, alignment(tagCADBL)
class tagCABOOL(Structure):
    pass
tagCABOOL._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(VARIANT_BOOL)),
]
assert sizeof(tagCABOOL) == 8, sizeof(tagCABOOL)
assert alignment(tagCABOOL) == 4, alignment(tagCABOOL)
class tagCASCODE(Structure):
    pass
tagCASCODE._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(SCODE)),
]
assert sizeof(tagCASCODE) == 8, sizeof(tagCASCODE)
assert alignment(tagCASCODE) == 4, alignment(tagCASCODE)
class tagCADATE(Structure):
    pass
tagCADATE._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(c_double)),
]
assert sizeof(tagCADATE) == 8, sizeof(tagCADATE)
assert alignment(tagCADATE) == 4, alignment(tagCADATE)
class tagCAFILETIME(Structure):
    pass
tagCAFILETIME._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(_FILETIME)),
]
assert sizeof(tagCAFILETIME) == 8, sizeof(tagCAFILETIME)
assert alignment(tagCAFILETIME) == 4, alignment(tagCAFILETIME)
class tagCACLSID(Structure):
    pass
tagCACLSID._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(stdole.GUID)),
]
assert sizeof(tagCACLSID) == 8, sizeof(tagCACLSID)
assert alignment(tagCACLSID) == 4, alignment(tagCACLSID)
class tagCACLIPDATA(Structure):
    pass
tagCACLIPDATA._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tagCLIPDATA)),
]
assert sizeof(tagCACLIPDATA) == 8, sizeof(tagCACLIPDATA)
assert alignment(tagCACLIPDATA) == 4, alignment(tagCACLIPDATA)
class tagCABSTR(Structure):
    pass
tagCABSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(BSTR)),
]
assert sizeof(tagCABSTR) == 8, sizeof(tagCABSTR)
assert alignment(tagCABSTR) == 4, alignment(tagCABSTR)
class tagCABSTRBLOB(Structure):
    pass
tagCABSTRBLOB._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tagBSTRBLOB)),
]
assert sizeof(tagCABSTRBLOB) == 8, sizeof(tagCABSTRBLOB)
assert alignment(tagCABSTRBLOB) == 4, alignment(tagCABSTRBLOB)
class tagCALPSTR(Structure):
    pass
tagCALPSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(STRING)),
]
assert sizeof(tagCALPSTR) == 8, sizeof(tagCALPSTR)
assert alignment(tagCALPSTR) == 4, alignment(tagCALPSTR)
class tagCALPWSTR(Structure):
    pass
tagCALPWSTR._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(WSTRING)),
]
assert sizeof(tagCALPWSTR) == 8, sizeof(tagCALPWSTR)
assert alignment(tagCALPWSTR) == 4, alignment(tagCALPWSTR)
class tagCAPROPVARIANT(Structure):
    pass
class tag_inner_PROPVARIANT(Structure):
    pass
tagCAPROPVARIANT._fields_ = [
    ('cElems', c_ulong),
    ('pElems', POINTER(tag_inner_PROPVARIANT)),
]
assert sizeof(tagCAPROPVARIANT) == 8, sizeof(tagCAPROPVARIANT)
assert alignment(tagCAPROPVARIANT) == 4, alignment(tagCAPROPVARIANT)
class DECIMAL(Structure):
		_fields_ = [("wReserved", c_ushort),
								("scale", c_ubyte),
								("sign", c_ubyte),
								("Hi32", c_ulong),
								("Lo64", c_ulonglong)]
__MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001._fields_ = [
    ('cVal', c_char),
    ('bVal', c_ubyte),
    ('iVal', c_short),
    ('uiVal', c_ushort),
    ('lVal', c_int),
    ('ulVal', c_ulong),
    ('intVal', c_int),
    ('uintVal', c_uint),
    ('hVal', _LARGE_INTEGER),
    ('uhVal', _ULARGE_INTEGER),
    ('fltVal', c_float),
    ('dblVal', c_double),
    ('boolVal', VARIANT_BOOL),
    ('bool', VARIANT_BOOL),
    ('scode', SCODE),
    ('cyVal', c_longlong),
    ('date', c_double),
    ('filetime', _FILETIME),
    ('puuid', POINTER(stdole.GUID)),
    ('pClipData', POINTER(tagCLIPDATA)),
    ('bstrVal', BSTR),
    ('bstrblobVal', tagBSTRBLOB),
    ('blob', tagBLOB),
    ('pszVal', STRING),
    ('pwszVal', WSTRING),
    ('punkVal', POINTER(IUnknown)),
    ('pdispVal', POINTER(IDispatch)),
    ('pStream', POINTER(IStream)),
    ('pStorage', POINTER(IStorage)),
    ('pVersionedStream', POINTER(tagVersionedStream)),
    ('parray', wirePSAFEARRAY),
    ('cac', tagCAC),
    ('caub', tagCAUB),
    ('cai', tagCAI),
    ('caui', tagCAUI),
    ('cal', tagCAL),
    ('caul', tagCAUL),
    ('cah', tagCAH),
    ('cauh', tagCAUH),
    ('caflt', tagCAFLT),
    ('cadbl', tagCADBL),
    ('cabool', tagCABOOL),
    ('cascode', tagCASCODE),
    ('cacy', tagCACY),
    ('cadate', tagCADATE),
    ('cafiletime', tagCAFILETIME),
    ('cauuid', tagCACLSID),
    ('caclipdata', tagCACLIPDATA),
    ('cabstr', tagCABSTR),
    ('cabstrblob', tagCABSTRBLOB),
    ('calpstr', tagCALPSTR),
    ('calpwstr', tagCALPWSTR),
    ('capropvar', tagCAPROPVARIANT),
    ('pcVal', STRING),
    ('pbVal', POINTER(c_ubyte)),
    ('piVal', POINTER(c_short)),
    ('puiVal', POINTER(c_ushort)),
    ('plVal', POINTER(c_int)),
    ('pulVal', POINTER(c_ulong)),
    ('pintVal', POINTER(c_int)),
    ('puintVal', POINTER(c_uint)),
    ('pfltVal', POINTER(c_float)),
    ('pdblVal', POINTER(c_double)),
    ('pboolVal', POINTER(VARIANT_BOOL)),
    ('pdecVal', POINTER(DECIMAL)),
    ('pscode', POINTER(SCODE)),
    ('pcyVal', POINTER(c_longlong)),
    ('pdate', POINTER(c_double)),
    ('pbstrVal', POINTER(BSTR)),
    ('ppunkVal', POINTER(POINTER(IUnknown))),
    ('ppdispVal', POINTER(POINTER(IDispatch))),
    ('pparray', POINTER(wirePSAFEARRAY)),
    ('pvarVal', POINTER(tag_inner_PROPVARIANT)),
]
assert sizeof(__MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001) == 8, sizeof(__MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001)
assert alignment(__MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001) == 8, alignment(__MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001)
ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( ['out'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for ISequentialStream implementation
##class ISequentialStream_Impl(object):
##    def RemoteRead(self, cb):
##        '-no docstring-'
##        #return pv, pcbRead
##
##    def RemoteWrite(self, pv, cb):
##        '-no docstring-'
##        #return pcbWritten
##

IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
################################################################
## code template for IStream implementation
##class IStream_Impl(object):
##    def RemoteSeek(self, dlibMove, dwOrigin):
##        '-no docstring-'
##        #return plibNewPosition
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def UnlockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppstm
##
##    def Revert(self):
##        '-no docstring-'
##        #return
##
##    def RemoteCopyTo(self, pstm, cb):
##        '-no docstring-'
##        #return pcbRead, pcbWritten
##
##    def LockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return
##
##    def SetSize(self, libNewSize):
##        '-no docstring-'
##        #return
##

class _FLAGGED_WORD_BLOB(Structure):
    pass
_FLAGGED_WORD_BLOB._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('asData', POINTER(c_ushort)),
]
assert sizeof(_FLAGGED_WORD_BLOB) == 12, sizeof(_FLAGGED_WORD_BLOB)
assert alignment(_FLAGGED_WORD_BLOB) == 4, alignment(_FLAGGED_WORD_BLOB)
class IPropertyStore(stdole.IUnknown):
    _case_insensitive_ = True
    u'Simple Property Store Interface'
    _iid_ = GUID('{886D8EEB-8CF2-4446-8D02-CDBA1DBDCF99}')
    _idlflags_ = []
class _tagpropertykey(Structure):
    pass
IPropertyStore._methods_ = [
    COMMETHOD([], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_ulong), 'cProps' )),
    COMMETHOD([], HRESULT, 'GetAt',
              ( ['in'], c_ulong, 'iProp' ),
              ( ['out'], POINTER(_tagpropertykey), 'pkey' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['out'], POINTER(tag_inner_PROPVARIANT), 'pv' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(_tagpropertykey), 'key' ),
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'propvar' )),
    COMMETHOD([], HRESULT, 'Commit'),
]
################################################################
## code template for IPropertyStore implementation
##class IPropertyStore_Impl(object):
##    def Commit(self):
##        '-no docstring-'
##        #return
##
##    def GetCount(self):
##        '-no docstring-'
##        #return cProps
##
##    def SetValue(self, key, propvar):
##        '-no docstring-'
##        #return
##
##    def GetAt(self, iProp):
##        '-no docstring-'
##        #return pkey
##
##    def GetValue(self, key):
##        '-no docstring-'
##        #return pv
##

tagVersionedStream._fields_ = [
    ('guidVersion', stdole.GUID),
    ('pStream', POINTER(IStream)),
]
assert sizeof(tagVersionedStream) == 20, sizeof(tagVersionedStream)
assert alignment(tagVersionedStream) == 4, alignment(tagVersionedStream)
_tagpropertykey._fields_ = [
    ('fmtid', stdole.GUID),
    ('pid', c_ulong),
]
assert sizeof(_tagpropertykey) == 20, sizeof(_tagpropertykey)
assert alignment(_tagpropertykey) == 4, alignment(_tagpropertykey)
class __MIDL_IOleAutomationTypes_0005(Union):
    pass
__MIDL_IOleAutomationTypes_0005._fields_ = [
    ('lptdesc', POINTER(tagTYPEDESC)),
    ('lpadesc', POINTER(tagARRAYDESC)),
    ('hreftype', c_ulong),
]
assert sizeof(__MIDL_IOleAutomationTypes_0005) == 4, sizeof(__MIDL_IOleAutomationTypes_0005)
assert alignment(__MIDL_IOleAutomationTypes_0005) == 4, alignment(__MIDL_IOleAutomationTypes_0005)
class _BYTE_SIZEDARR(Structure):
    pass
_BYTE_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ubyte)),
]
assert sizeof(_BYTE_SIZEDARR) == 8, sizeof(_BYTE_SIZEDARR)
assert alignment(_BYTE_SIZEDARR) == 4, alignment(_BYTE_SIZEDARR)
class Library(object):
    u'MM Device API 1.0 Type Library'
    name = u'MMDeviceAPILib'
    _reg_typelib_ = ('{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}', 1, 0)

tagCLIPDATA._fields_ = [
    ('cbSize', c_ulong),
    ('ulClipFmt', c_int),
    ('pClipData', POINTER(c_ubyte)),
]
assert sizeof(tagCLIPDATA) == 12, sizeof(tagCLIPDATA)
assert alignment(tagCLIPDATA) == 4, alignment(tagCLIPDATA)

# values for enumeration '__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001'
eRender = 0
eCapture = 1
eAll = 2
EDataFlow_enum_count = 3
__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001 = c_int # enum
EDataFlow = __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001
class _wireSAFEARR_UNKNOWN(Structure):
    pass
_wireSAFEARR_UNKNOWN._fields_ = [
    ('Size', c_ulong),
    ('apUnknown', POINTER(POINTER(IUnknown))),
]
assert sizeof(_wireSAFEARR_UNKNOWN) == 8, sizeof(_wireSAFEARR_UNKNOWN)
assert alignment(_wireSAFEARR_UNKNOWN) == 4, alignment(_wireSAFEARR_UNKNOWN)
class MMDeviceEnumerator(CoClass):
    _reg_clsid_ = GUID('{BCDE0395-E52F-467C-8E3D-C4579291692E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}', 1, 0)
class IMMDeviceEnumerator(stdole.IUnknown):
    _case_insensitive_ = True
    u'MMDevice Enumerator Interface'
    _iid_ = GUID('{A95664D2-9614-4F35-A746-DE8DB63617E6}')
    _idlflags_ = ['nonextensible']
MMDeviceEnumerator._com_interfaces_ = [IMMDeviceEnumerator]

class _wireSAFEARR_VARIANT(Structure):
    pass
class _wireVARIANT(Structure):
    pass
_wireSAFEARR_VARIANT._fields_ = [
    ('Size', c_ulong),
    ('aVariant', POINTER(POINTER(_wireVARIANT))),
]
assert sizeof(_wireSAFEARR_VARIANT) == 8, sizeof(_wireSAFEARR_VARIANT)
assert alignment(_wireSAFEARR_VARIANT) == 4, alignment(_wireSAFEARR_VARIANT)
class __MIDL_IOleAutomationTypes_0006(Union):
    pass
__MIDL_IOleAutomationTypes_0006._fields_ = [
    ('oInst', c_ulong),
    ('lpvarValue', POINTER(VARIANT)),
]
assert sizeof(__MIDL_IOleAutomationTypes_0006) == 4, sizeof(__MIDL_IOleAutomationTypes_0006)
assert alignment(__MIDL_IOleAutomationTypes_0006) == 4, alignment(__MIDL_IOleAutomationTypes_0006)
class __MIDL_IOleAutomationTypes_0004(Union):
    pass
class _wireBRECORD(Structure):
    pass
# WARNING: PACKING FAILED: total alignment (8/64)
__MIDL_IOleAutomationTypes_0004._fields_ = [
    ('llVal', c_longlong),
    ('lVal', c_int),
    ('bVal', c_ubyte),
    ('iVal', c_short),
    ('fltVal', c_float),
    ('dblVal', c_double),
    ('boolVal', VARIANT_BOOL),
    ('scode', SCODE),
    ('cyVal', c_longlong),
    ('date', c_double),
    ('bstrVal', POINTER(_FLAGGED_WORD_BLOB)),
    ('punkVal', POINTER(IUnknown)),
    ('pdispVal', POINTER(IDispatch)),
    ('parray', POINTER(POINTER(_wireSAFEARRAY))),
    ('brecVal', POINTER(_wireBRECORD)),
    ('pbVal', POINTER(c_ubyte)),
    ('piVal', POINTER(c_short)),
    ('plVal', POINTER(c_int)),
    ('pllVal', POINTER(c_longlong)),
    ('pfltVal', POINTER(c_float)),
    ('pdblVal', POINTER(c_double)),
    ('pboolVal', POINTER(VARIANT_BOOL)),
    ('pscode', POINTER(SCODE)),
    ('pcyVal', POINTER(c_longlong)),
    ('pdate', POINTER(c_double)),
    ('pbstrVal', POINTER(POINTER(_FLAGGED_WORD_BLOB))),
    ('ppunkVal', POINTER(POINTER(IUnknown))),
    ('ppdispVal', POINTER(POINTER(IDispatch))),
    ('pparray', POINTER(POINTER(POINTER(_wireSAFEARRAY)))),
    ('pvarVal', POINTER(POINTER(_wireVARIANT))),
    ('cVal', c_char),
    ('uiVal', c_ushort),
    ('ulVal', c_ulong),
    ('ullVal', c_ulonglong),
    ('intVal', c_int),
    ('uintVal', c_uint),
    ('decVal', DECIMAL),
    ('pdecVal', POINTER(DECIMAL)),
    ('pcVal', STRING),
    ('puiVal', POINTER(c_ushort)),
    ('pulVal', POINTER(c_ulong)),
    ('pullVal', POINTER(c_ulonglong)),
    ('pintVal', POINTER(c_int)),
    ('puintVal', POINTER(c_uint)),
]
assert sizeof(__MIDL_IOleAutomationTypes_0004) == 16, sizeof(__MIDL_IOleAutomationTypes_0004)
assert alignment(__MIDL_IOleAutomationTypes_0004) == 8, alignment(__MIDL_IOleAutomationTypes_0004)
_wireVARIANT._fields_ = [
    ('clSize', c_ulong),
    ('rpcReserved', c_ulong),
    ('vt', c_ushort),
    ('wReserved1', c_ushort),
    ('wReserved2', c_ushort),
    ('wReserved3', c_ushort),
    ('DUMMYUNIONNAME', __MIDL_IOleAutomationTypes_0004),
]
assert sizeof(_wireVARIANT) == 32, sizeof(_wireVARIANT)
assert alignment(_wireVARIANT) == 8, alignment(_wireVARIANT)
class IMMDeviceCollection(stdole.IUnknown):
    _case_insensitive_ = True
    u'Interface for accessing a collection of IMMDevice objects'
    _iid_ = GUID('{0BD7A1BE-7A1A-44DB-8397-CC5392387B5E}')
    _idlflags_ = ['nonextensible']
class IMMDevice(stdole.IUnknown):
    _case_insensitive_ = True
    u'MMDevice Interface'
    _iid_ = GUID('{D666063F-1587-4E43-81F1-B948E807363F}')
    _idlflags_ = ['nonextensible']
IMMDeviceCollection._methods_ = [
    COMMETHOD([helpstring(u'method GetCount')], HRESULT, 'GetCount',
              ( ['out'], POINTER(c_uint), 'pcDevices' )),
    COMMETHOD([helpstring(u'method Item')], HRESULT, 'Item',
              ( ['in'], c_uint, 'nDevice' ),
              ( ['out'], POINTER(POINTER(IMMDevice)), 'ppDevice' )),
]
################################################################
## code template for IMMDeviceCollection implementation
##class IMMDeviceCollection_Impl(object):
##    def GetCount(self):
##        u'method GetCount'
##        #return pcDevices
##
##    def Item(self, nDevice):
##        u'method Item'
##        #return ppDevice
##

IMMDevice._methods_ = [
    COMMETHOD([helpstring(u'method Activate')], HRESULT, 'Activate',
              ( ['in'], POINTER(stdole.GUID), 'iid' ),
              ( ['in'], c_ulong, 'dwClsCtx' ),
              ( ['in'], POINTER(tag_inner_PROPVARIANT), 'pActivationParams' ),
              ( ['out'], POINTER(c_void_p), 'ppInterface' )),
    COMMETHOD([helpstring(u'method OpenPropertyStore')], HRESULT, 'OpenPropertyStore',
              ( ['in'], c_ulong, 'stgmAccess' ),
              ( ['out'], POINTER(POINTER(IPropertyStore)), 'ppProperties' )),
    COMMETHOD([helpstring(u'method GetId')], HRESULT, 'GetId',
              ( ['out'], POINTER(WSTRING), 'ppstrId' )),
    COMMETHOD([helpstring(u'method GetState')], HRESULT, 'GetState',
              ( ['out'], POINTER(c_ulong), 'pdwState' )),
]
################################################################
## code template for IMMDevice implementation
##class IMMDevice_Impl(object):
##    def GetState(self):
##        u'method GetState'
##        #return pdwState
##
##    def Activate(self, iid, dwClsCtx, pActivationParams):
##        u'method Activate'
##        #return ppInterface
##
##    def GetId(self):
##        u'method GetId'
##        #return ppstrId
##
##    def OpenPropertyStore(self, stgmAccess):
##        u'method OpenPropertyStore'
##        #return ppProperties
##

class __MIDL_IOleAutomationTypes_0001(Union):
    pass
class _wireSAFEARR_BSTR(Structure):
    pass
_wireSAFEARR_BSTR._fields_ = [
    ('Size', c_ulong),
    ('aBstr', POINTER(POINTER(_FLAGGED_WORD_BLOB))),
]
assert sizeof(_wireSAFEARR_BSTR) == 8, sizeof(_wireSAFEARR_BSTR)
assert alignment(_wireSAFEARR_BSTR) == 4, alignment(_wireSAFEARR_BSTR)
class _wireSAFEARR_BRECORD(Structure):
    pass
_wireSAFEARR_BRECORD._fields_ = [
    ('Size', c_ulong),
    ('aRecord', POINTER(POINTER(_wireBRECORD))),
]
assert sizeof(_wireSAFEARR_BRECORD) == 8, sizeof(_wireSAFEARR_BRECORD)
assert alignment(_wireSAFEARR_BRECORD) == 4, alignment(_wireSAFEARR_BRECORD)
class _wireSAFEARR_HAVEIID(Structure):
    pass
_wireSAFEARR_HAVEIID._fields_ = [
    ('Size', c_ulong),
    ('apUnknown', POINTER(POINTER(IUnknown))),
    ('iid', stdole.GUID),
]
assert sizeof(_wireSAFEARR_HAVEIID) == 24, sizeof(_wireSAFEARR_HAVEIID)
assert alignment(_wireSAFEARR_HAVEIID) == 4, alignment(_wireSAFEARR_HAVEIID)
class _SHORT_SIZEDARR(Structure):
    pass
_SHORT_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ushort)),
]
assert sizeof(_SHORT_SIZEDARR) == 8, sizeof(_SHORT_SIZEDARR)
assert alignment(_SHORT_SIZEDARR) == 4, alignment(_SHORT_SIZEDARR)
class _LONG_SIZEDARR(Structure):
    pass
_LONG_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_ulong)),
]
assert sizeof(_LONG_SIZEDARR) == 8, sizeof(_LONG_SIZEDARR)
assert alignment(_LONG_SIZEDARR) == 4, alignment(_LONG_SIZEDARR)
class _HYPER_SIZEDARR(Structure):
    pass
_HYPER_SIZEDARR._fields_ = [
    ('clSize', c_ulong),
    ('pData', POINTER(c_longlong)),
]
assert sizeof(_HYPER_SIZEDARR) == 8, sizeof(_HYPER_SIZEDARR)
assert alignment(_HYPER_SIZEDARR) == 4, alignment(_HYPER_SIZEDARR)
__MIDL_IOleAutomationTypes_0001._fields_ = [
    ('BstrStr', _wireSAFEARR_BSTR),
    ('UnknownStr', _wireSAFEARR_UNKNOWN),
    ('DispatchStr', _wireSAFEARR_DISPATCH),
    ('VariantStr', _wireSAFEARR_VARIANT),
    ('RecordStr', _wireSAFEARR_BRECORD),
    ('HaveIidStr', _wireSAFEARR_HAVEIID),
    ('ByteStr', _BYTE_SIZEDARR),
    ('WordStr', _SHORT_SIZEDARR),
    ('LongStr', _LONG_SIZEDARR),
    ('HyperStr', _HYPER_SIZEDARR),
]
assert sizeof(__MIDL_IOleAutomationTypes_0001) == 24, sizeof(__MIDL_IOleAutomationTypes_0001)
assert alignment(__MIDL_IOleAutomationTypes_0001) == 4, alignment(__MIDL_IOleAutomationTypes_0001)

# values for enumeration '__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002'
eConsole = 0
eMultimedia = 1
eCommunications = 2
ERole_enum_count = 3
__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002 = c_int # enum
ERole = __MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002
class IMMNotificationClient(stdole.IUnknown):
    _case_insensitive_ = True
    u'Interface implemented by objects that want to be notified of MMDevice events'
    _iid_ = GUID('{7991EEC9-7E89-4D85-8390-6C703CEC60C0}')
    _idlflags_ = ['nonextensible']
IMMDeviceEnumerator._methods_ = [
    COMMETHOD([helpstring(u'method EnumAudioEndpoints')], HRESULT, 'EnumAudioEndpoints',
              ( ['in'], EDataFlow, 'dataFlow' ),
              ( ['in'], c_ulong, 'dwStateMask' ),
              ( ['out'], POINTER(POINTER(IMMDeviceCollection)), 'ppDevices' )),
    COMMETHOD([helpstring(u'method GetDefaultAudioEndpoint')], HRESULT, 'GetDefaultAudioEndpoint',
              ( ['in'], EDataFlow, 'dataFlow' ),
              ( ['in'], ERole, 'role' ),
              ( ['out'], POINTER(POINTER(IMMDevice)), 'ppEndpoint' )),
    COMMETHOD([helpstring(u'method GetDevice')], HRESULT, 'GetDevice',
              ( ['in'], WSTRING, 'pwstrId' ),
              ( ['out'], POINTER(POINTER(IMMDevice)), 'ppDevice' )),
    COMMETHOD([helpstring(u'method RegisterEndpointNotificationCallback')], HRESULT, 'RegisterEndpointNotificationCallback',
              ( ['in'], POINTER(IMMNotificationClient), 'pClient' )),
    COMMETHOD([helpstring(u'method UnregisterEndpointNotificationCallback')], HRESULT, 'UnregisterEndpointNotificationCallback',
              ( ['in'], POINTER(IMMNotificationClient), 'pClient' )),
]
################################################################
## code template for IMMDeviceEnumerator implementation
##class IMMDeviceEnumerator_Impl(object):
##    def EnumAudioEndpoints(self, dataFlow, dwStateMask):
##        u'method EnumAudioEndpoints'
##        #return ppDevices
##
##    def UnregisterEndpointNotificationCallback(self, pClient):
##        u'method UnregisterEndpointNotificationCallback'
##        #return
##
##    def GetDefaultAudioEndpoint(self, dataFlow, role):
##        u'method GetDefaultAudioEndpoint'
##        #return ppEndpoint
##
##    def RegisterEndpointNotificationCallback(self, pClient):
##        u'method RegisterEndpointNotificationCallback'
##        #return
##
##    def GetDevice(self, pwstrId):
##        u'method GetDevice'
##        #return ppDevice
##

class tagRemSNB(Structure):
    pass
tagRemSNB._fields_ = [
    ('ulCntStr', c_ulong),
    ('ulCntChar', c_ulong),
    ('rgString', POINTER(c_ushort)),
]
assert sizeof(tagRemSNB) == 12, sizeof(tagRemSNB)
assert alignment(tagRemSNB) == 4, alignment(tagRemSNB)
class _wireSAFEARRAY_UNION(Structure):
    pass
_wireSAFEARRAY_UNION._fields_ = [
    ('sfType', c_ulong),
    ('u', __MIDL_IOleAutomationTypes_0001),
]
assert sizeof(_wireSAFEARRAY_UNION) == 28, sizeof(_wireSAFEARRAY_UNION)
assert alignment(_wireSAFEARRAY_UNION) == 4, alignment(_wireSAFEARRAY_UNION)
_wireSAFEARRAY._fields_ = [
    ('cDims', c_ushort),
    ('fFeatures', c_ushort),
    ('cbElements', c_ulong),
    ('cLocks', c_ulong),
    ('uArrayStructs', _wireSAFEARRAY_UNION),
    ('rgsabound', POINTER(tagSAFEARRAYBOUND)),
]
assert sizeof(_wireSAFEARRAY) == 44, sizeof(_wireSAFEARRAY)
assert alignment(_wireSAFEARRAY) == 4, alignment(_wireSAFEARRAY)
_wireBRECORD._fields_ = [
    ('fFlags', c_ulong),
    ('clSize', c_ulong),
    ('pRecInfo', POINTER(IRecordInfo)),
    ('pRecord', POINTER(c_ubyte)),
]
assert sizeof(_wireBRECORD) == 16, sizeof(_wireBRECORD)
assert alignment(_wireBRECORD) == 4, alignment(_wireBRECORD)
class IEnumSTATSTG(stdole.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000D-0000-0000-C000-000000000046}')
    _idlflags_ = []
IEnumSTATSTG._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(tagSTATSTG), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum' )),
]
################################################################
## code template for IEnumSTATSTG implementation
##class IEnumSTATSTG_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

tag_inner_PROPVARIANT._fields_ = [
    ('vt', c_ushort),
    ('wReserved1', c_ubyte),
    ('wReserved2', c_ubyte),
    ('wReserved3', c_ulong),
    ('__MIDL____MIDL_itf_mmdeviceapi_0003_00850001', __MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001),
]
assert sizeof(tag_inner_PROPVARIANT) == 16, sizeof(tag_inner_PROPVARIANT)
assert alignment(tag_inner_PROPVARIANT) == 8, alignment(tag_inner_PROPVARIANT)
wireSNB = POINTER(tagRemSNB)
IStorage._methods_ = [
    COMMETHOD([], HRESULT, 'CreateStream',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
    COMMETHOD([], HRESULT, 'RemoteOpenStream',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'cbReserved1' ),
              ( ['in'], POINTER(c_ubyte), 'reserved1' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
    COMMETHOD([], HRESULT, 'CreateStorage',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'reserved2' ),
              ( ['out'], POINTER(POINTER(IStorage)), 'ppstg' )),
    COMMETHOD([], HRESULT, 'OpenStorage',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(IStorage), 'pstgPriority' ),
              ( ['in'], c_ulong, 'grfMode' ),
              ( ['in'], wireSNB, 'snbExclude' ),
              ( ['in'], c_ulong, 'reserved' ),
              ( ['out'], POINTER(POINTER(IStorage)), 'ppstg' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], c_ulong, 'ciidExclude' ),
              ( ['in'], POINTER(stdole.GUID), 'rgiidExclude' ),
              ( ['in'], wireSNB, 'snbExclude' ),
              ( ['in'], POINTER(IStorage), 'pstgDest' )),
    COMMETHOD([], HRESULT, 'MoveElementTo',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(IStorage), 'pstgDest' ),
              ( ['in'], WSTRING, 'pwcsNewName' ),
              ( ['in'], c_ulong, 'grfFlags' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'RemoteEnumElements',
              ( ['in'], c_ulong, 'reserved1' ),
              ( ['in'], c_ulong, 'cbReserved2' ),
              ( ['in'], POINTER(c_ubyte), 'reserved2' ),
              ( ['in'], c_ulong, 'reserved3' ),
              ( ['out'], POINTER(POINTER(IEnumSTATSTG)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'DestroyElement',
              ( ['in'], WSTRING, 'pwcsName' )),
    COMMETHOD([], HRESULT, 'RenameElement',
              ( ['in'], WSTRING, 'pwcsOldName' ),
              ( ['in'], WSTRING, 'pwcsNewName' )),
    COMMETHOD([], HRESULT, 'SetElementTimes',
              ( ['in'], WSTRING, 'pwcsName' ),
              ( ['in'], POINTER(_FILETIME), 'pctime' ),
              ( ['in'], POINTER(_FILETIME), 'patime' ),
              ( ['in'], POINTER(_FILETIME), 'pmtime' )),
    COMMETHOD([], HRESULT, 'SetClass',
              ( ['in'], POINTER(stdole.GUID), 'clsid' )),
    COMMETHOD([], HRESULT, 'SetStateBits',
              ( ['in'], c_ulong, 'grfStateBits' ),
              ( ['in'], c_ulong, 'grfMask' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
]
################################################################
## code template for IStorage implementation
##class IStorage_Impl(object):
##    def RemoteOpenStream(self, pwcsName, cbReserved1, reserved1, grfMode, reserved2):
##        '-no docstring-'
##        #return ppstm
##
##    def MoveElementTo(self, pwcsName, pstgDest, pwcsNewName, grfFlags):
##        '-no docstring-'
##        #return
##
##    def DestroyElement(self, pwcsName):
##        '-no docstring-'
##        #return
##
##    def OpenStorage(self, pwcsName, pstgPriority, grfMode, snbExclude, reserved):
##        '-no docstring-'
##        #return ppstg
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def Revert(self):
##        '-no docstring-'
##        #return
##
##    def SetElementTimes(self, pwcsName, pctime, patime, pmtime):
##        '-no docstring-'
##        #return
##
##    def RemoteCopyTo(self, ciidExclude, rgiidExclude, snbExclude, pstgDest):
##        '-no docstring-'
##        #return
##
##    def SetClass(self, clsid):
##        '-no docstring-'
##        #return
##
##    def RemoteEnumElements(self, reserved1, cbReserved2, reserved2, reserved3):
##        '-no docstring-'
##        #return ppenum
##
##    def CreateStorage(self, pwcsName, grfMode, reserved1, reserved2):
##        '-no docstring-'
##        #return ppstg
##
##    def RenameElement(self, pwcsOldName, pwcsNewName):
##        '-no docstring-'
##        #return
##
##    def CreateStream(self, pwcsName, grfMode, reserved1, reserved2):
##        '-no docstring-'
##        #return ppstm
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return
##
##    def SetStateBits(self, grfStateBits, grfMask):
##        '-no docstring-'
##        #return
##

IMMNotificationClient._methods_ = [
    COMMETHOD([helpstring(u'method OnDeviceStateChanged')], HRESULT, 'OnDeviceStateChanged',
              ( ['in'], WSTRING, 'pwstrDeviceId' ),
              ( ['in'], c_ulong, 'dwNewState' )),
    COMMETHOD([helpstring(u'method OnDeviceAdded')], HRESULT, 'OnDeviceAdded',
              ( ['in'], WSTRING, 'pwstrDeviceId' )),
    COMMETHOD([helpstring(u'method OnDeviceRemoved')], HRESULT, 'OnDeviceRemoved',
              ( ['in'], WSTRING, 'pwstrDeviceId' )),
    COMMETHOD([helpstring(u'method OnDefaultDeviceChanged')], HRESULT, 'OnDefaultDeviceChanged',
              ( ['in'], EDataFlow, 'flow' ),
              ( ['in'], ERole, 'role' ),
              ( ['in'], WSTRING, 'pwstrDefaultDeviceId' )),
    COMMETHOD([helpstring(u'method OnPropertyValueChanged')], HRESULT, 'OnPropertyValueChanged',
              ( ['in'], WSTRING, 'pwstrDeviceId' ),
              ( ['in'], _tagpropertykey, 'key' )),
]
################################################################
## code template for IMMNotificationClient implementation
##class IMMNotificationClient_Impl(object):
##    def OnDeviceStateChanged(self, pwstrDeviceId, dwNewState):
##        u'method OnDeviceStateChanged'
##        #return
##
##    def OnDeviceRemoved(self, pwstrDeviceId):
##        u'method OnDeviceRemoved'
##        #return
##
##    def OnDeviceAdded(self, pwstrDeviceId):
##        u'method OnDeviceAdded'
##        #return
##
##    def OnDefaultDeviceChanged(self, flow, role, pwstrDefaultDeviceId):
##        u'method OnDefaultDeviceChanged'
##        #return
##
##    def OnPropertyValueChanged(self, pwstrDeviceId, key):
##        u'method OnPropertyValueChanged'
##        #return
##

__all__ = ['__MIDL_IOleAutomationTypes_0006', 'IMMDevice',
           'tagCABSTR', '__MIDL_IOleAutomationTypes_0005',
           '_wireSAFEARRAY', '_wireSAFEARR_HAVEIID', 'tagBLOB',
           '__MIDL_IOleAutomationTypes_0001', 'EDataFlow',
           '_wireSAFEARR_BSTR', '__MIDL_IOleAutomationTypes_0004',
           'tagCALPWSTR', 'tagCASCODE', 'tagBSTRBLOB', 'tagCAUB',
           'ERole_enum_count', 'eConsole', 'wirePSAFEARRAY',
           'tagSTATSTG', 'tagCLIPDATA', 'tagCAUH', 'tagCALPSTR',
           'tagCAUL', 'EDataFlow_enum_count', '_wireSAFEARR_UNKNOWN',
           '_LONG_SIZEDARR', 'tag_inner_PROPVARIANT',
           'IMMDeviceEnumerator', 'ERole', '_wireBRECORD', 'tagCAFLT',
           'tagCABSTRBLOB', 'tagCAFILETIME', 'wireSNB',
           'IMMDeviceCollection', '_wireSAFEARR_DISPATCH',
           'tagRemSNB', 'tagCADBL', 'tagCACLIPDATA', 'tagCAUI',
           'IStorage', 'tagVersionedStream', '_FLAGGED_WORD_BLOB',
           '__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0001', 'tagCAL',
           '__MIDL___MIDL_itf_mmdeviceapi_0000_0000_0002', 'tagCAH',
           'tagCAI', 'DECIMAL', '_BYTE_SIZEDARR', 'tagCAC',
           'IPropertyStore', '_HYPER_SIZEDARR', '_SHORT_SIZEDARR',
           'eRender', 'eAll', 'eMultimedia', '_wireSAFEARRAY_UNION',
           'ISequentialStream',
           '__MIDL___MIDL_itf_mmdeviceapi_0003_0085_0001', 'eCapture',
           'tagCACLSID', 'IMMNotificationClient', '_wireVARIANT',
           'MMDeviceEnumerator', 'eCommunications',
           'tagCAPROPVARIANT', 'tagCABOOL', 'IStream',
           '_wireSAFEARR_BRECORD', 'IEnumSTATSTG', '_tagpropertykey',
           'tagCADATE', '_wireSAFEARR_VARIANT', 'tagCACY']
from comtypes import _check_version; _check_version('501')