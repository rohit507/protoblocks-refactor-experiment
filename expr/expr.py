from typing import * 
from elem import *
from abc import *

import attr

EL = TypeVar('EL') # Expr-Like

@attr.s
class Expr(Value, Generic[EL]):
    __match_containter__ = 0 
    __match_class__ = 8 # MATCH_SELF

    EV = TypeVar('EV',bound='Expr[EL]') # Expr-Value

    @classmethod
    def free(cls: Type[EV]) -> EV:
        """Creates a new unbound/free.undefined value expr."""
        ...
    
    def bind(self: EV, expr_like : Union[EV,EL]) -> EV:
        """Assign a particular expression like value to this expression."""
        ...

    @classmethod
    def new(cls: Type[EV], expr_like : Union[EV,EL]) -> EV:
        """Create a new free expr and simultaneously bind to it.""" 
        return cls.free().bind(expr_like)

