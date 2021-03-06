from hypothesis import given
from hypothesis.strategies import (
    binary,
    booleans,
    composite,
    lists,
    none,
    sampled_from,
)

from flattr import model_from_bytes, model_to_bytes

from .models_enums import ASimpleUByteEnum
from .models_vectors import (
    ByteArrayTable,
    OptionalByteArrayTable,
    VectorOfCommon1,
    VectorOfEnums,
    VectorsOfScalars,
)
from .strats import (
    float32s,
    float64s,
    int8s,
    int16s,
    int32s,
    int64s,
    uint8s,
    uint16s,
    uint32s,
    uint64s,
)
from .test_common import common1s


@composite
def vectors_of_scalars(draw):
    return VectorsOfScalars(
        draw(lists(booleans())),
        draw(lists(uint8s)),
        draw(lists(uint16s)),
        draw(lists(uint32s)),
        draw(lists(uint64s)),
        draw(lists(int8s)),
        draw(lists(int16s)),
        draw(lists(int32s)),
        draw(lists(int64s)),
        draw(lists(float32s)),
        draw(lists(float64s)),
    )


@composite
def vectors_of_common1s(draw):
    return VectorOfCommon1(draw(lists(common1s())))


@composite
def bytearray_tables(draw):
    return ByteArrayTable(draw(binary()))


@composite
def vectors_of_enums(draw):
    return VectorOfEnums(draw(lists(sampled_from(ASimpleUByteEnum))))


@composite
def optional_bytearray_tables(draw):
    return OptionalByteArrayTable(draw(binary() | none()))


@given(vectors_of_scalars())
def test_vectors_of_scalars_rt(inst):
    assert inst == model_from_bytes(inst.__class__, model_to_bytes(inst))


@given(vectors_of_common1s())
def test_vectors_of_common1s_rt(inst):
    assert inst == model_from_bytes(inst.__class__, model_to_bytes(inst))


@given(bytearray_tables())
def test_bytearray_tables(inst):
    assert inst == model_from_bytes(inst.__class__, model_to_bytes(inst))


@given(optional_bytearray_tables())
def test_optional_bytearray_tables(inst):
    assert inst == model_from_bytes(inst.__class__, model_to_bytes(inst))


@given(vectors_of_enums())
def test_vectors_of_enums(inst):
    assert inst == model_from_bytes(inst.__class__, model_to_bytes(inst))
