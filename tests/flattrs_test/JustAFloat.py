# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flattrs_test

import flatbuffers

class JustAFloat(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsJustAFloat(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = JustAFloat()
        x.Init(buf, n + offset)
        return x

    # JustAFloat
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # JustAFloat
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def JustAFloatStart(builder): builder.StartObject(1)
def JustAFloatAddValue(builder, value): builder.PrependFloat32Slot(0, value, 0.0)
def JustAFloatEnd(builder): return builder.EndObject()