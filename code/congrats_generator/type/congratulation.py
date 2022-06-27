import enum


@enum.unique
class CongratulationType(enum.Enum):
    DEFAULT_CONGRATS = enum.auto()
    BIRTHDAY_CONGRATS = enum.auto()
