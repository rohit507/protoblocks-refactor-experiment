from typing import * 
import attr 
from ops import * 

class IntVal(): pass 
class FloatVal(): pass
class BoolVal(): pass 

F = TypeVar('F')

class RangeVal(Generic[F]): pass
class ArrayVal(Generic[F]): pass 

ScalarVal = TypeVar('ScalarVal', bound=Union[
    IntVal,
    FloatVal])

NumericVal = TypeVar('NumericVal', bound=Union[ 
    IntVal,
    FloatVal,
    RangeVal[IntVal],
    RangeVal[FloatVal]])