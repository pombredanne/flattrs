# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flattrs_test

import flatbuffers

class JustOptionalBytes(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsJustOptionalBytes(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = JustOptionalBytes()
        x.Init(buf, n + offset)
        return x

    # JustOptionalBytes
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # JustOptionalBytes
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # JustOptionalBytes
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # JustOptionalBytes
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def JustOptionalBytesStart(builder): builder.StartObject(1)
def JustOptionalBytesAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def JustOptionalBytesStartValueVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def JustOptionalBytesEnd(builder): return builder.EndObject()