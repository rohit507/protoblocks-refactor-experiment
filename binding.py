from typing import * 
from enum import *
import attr 

if TYPE_CHECKING:
    from expr import Expr

class Operator(Enum): 
    NEGATE = auto() 
    ADD = auto()

    INVERT = auto() 
    MUL = auto() 

@attr.s 
class Binding():
    __match_container__ : int = 0
    __match_class__ : int = 0
    __match_args__ : Sequence[str] = ()

    def members(self) -> Iterator[Expr]: 

        from expr import Expr

        for val in self.__match_args__:
            if isinstance(val, Expr): 
                yield getattr(self, val)

@attr.s 
class Lit(Binding):
    __match_args__ : Sequence[str] = ("val")

    val : Any = attr.ib()

@attr.s 
class Op(Binding):
    __match_args__ : Sequence[str] = ("op")

    op : Operator = attr.ib()

@attr.s 
class UnOp(Op):
    __match_args__ : Sequence[str] = ("op","val")

    val : Expr = attr.ib()

@attr.s 
class BinOp(Op):
    __match_args__ : Sequence[str] = ("op", "lhs", "rhs")
    
    lhs : Any = attr.ib()
    rhs : Optional[Any] = attr.ib(default=None)