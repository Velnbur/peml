"""
This is a module for all types in the language.
"""
import enum


@enum.unique
class Types(enum.Enum):
    u8 = enum.auto()
    u16 = enum.auto()
    u32 = enum.auto()
    u64 = enum.auto()
    u128 = enum.auto()
    u256 = enum.auto()

    i8 = enum.auto()
    i16 = enum.auto()
    i32 = enum.auto()
    i64 = enum.auto()
    i128 = enum.auto()
    i256 = enum.auto()

    bool = enum.auto()
    str = enum.auto()

    address = enum.auto()
