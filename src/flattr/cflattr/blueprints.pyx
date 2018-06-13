from libc.stdint cimport uint8_t


cdef class Field:
    def __init__(self, uint8_t slot_num, str name, FieldType type, default):
        self.slot_num = slot_num
        self.name = name
        self.type = type
        self.default = default


cdef class Blueprint:
    def __init__(self, num_slots, fields, string_fields, opt_string_fields):
        self.num_slots = num_slots
        self.fields = fields
        self.string_fields = string_fields
        self.optional_string_fields = opt_string_fields