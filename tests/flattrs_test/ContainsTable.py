# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flattrs_test

import flatbuffers

class ContainsTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsContainsTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ContainsTable()
        x.Init(buf, n + offset)
        return x

    # ContainsTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ContainsTable
    def Inner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Common1 import Common1
            obj = Common1()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ContainsTableStart(builder): builder.StartObject(1)
def ContainsTableAddInner(builder, inner): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(inner), 0)
def ContainsTableEnd(builder): return builder.EndObject()
