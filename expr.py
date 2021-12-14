from typing import * 
import attr 
if TYPE_CHECKING:
    from ops import *

ExprLike = TypeVar('ExprLike')
T = TypeVar('T')
E = TypeVar('E',bound='Expr')

class Expr(Generic[ExprLike]):
    def bind(self: E, ExprLike) -> E: ... 

    def dump(self) -> str: ...


BoolLike = Union[bool, 'BoolExpr', Op['BoolExpr']]
class BoolExpr(Expr[BoolLike]): pass 


ConstraintLike = Union[BoolLike,'ConstraintExpr']
class ConstraintExpr(Expr[ConstraintLike]): pass

IntLike = Union[int,'IntExpr', Op['IntExpr']]
class IntExpr(Expr[IntLike]): pass

FloatLike = Union[float,IntLike,'FloatExpr',Op['FloatExpr']] 
class FloatExpr(Expr[IntLike]): pass 

ScalarLike = Union[IntLike,FloatLike]
ScalarExpr = Union[IntExpr,FloatExpr]

SVL = TypeVar('SVL',bound='ScalarLike')
SV  = TypeVar('SV',bound='ScalarExpr')
RangeLike = Union[SVL,Tuple[SVL,SVL],'RangeExpr[SVL]',Op['RangeExpr[SVL]']] 
class RangeExpr(Expr[RangeLike[SV]],Generic[SV]): pass

NumericLike = Union[IntLike,FloatLike,RangeLike[ScalarLike]]
NumericExpr = Union[IntExpr,FloatExpr,RangeExpr[ScalarExpr]]

ArrayLike = Union[Sequence[T],'ArrayExpr[T]',Op['ArrayExpr[T]']]
class ArrayExpr(Expr,Generic[T]): pass 
