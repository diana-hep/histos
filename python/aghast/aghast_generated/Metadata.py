# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers

class Metadata(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMetadata(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Metadata()
        x.Init(buf, n + offset)
        return x

    # Metadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Metadata
    def Data(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Metadata
    def Language(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def MetadataStart(builder): builder.StartObject(2)
def MetadataAddData(builder, data): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def MetadataAddLanguage(builder, language): builder.PrependUint32Slot(1, language, 0)
def MetadataEnd(builder): return builder.EndObject()