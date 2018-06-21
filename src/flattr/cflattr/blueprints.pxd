from libc.stdint cimport uint8_t


cpdef enum FieldType:
    bool,
    uint8,
    uint16,
    uint32,
    uint64,
    int8,
    int16,
    int32,
    int64,
    float32,
    float64,
    string,
    optional_string,
    vector_of_strings,


cdef class Field:
    cdef uint8_t slot_num
    cdef object name
    cdef FieldType type
    cdef object default
    cdef uint8_t alignment  // For vectors.


cdef class Blueprint:
    cdef uint8_t num_slots
    cdef list fields, string_fields, optional_string_fields, vectors_of_strings
