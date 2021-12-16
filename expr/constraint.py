from typing import *
from .expr import *
import attr 

ConstraintLike = Union[bool]
class ConstraintExpr(Expr[ConstraintLike]): 
    pass
