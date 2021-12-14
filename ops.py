from abc import abstractclassmethod
from typing import * 
import attr 
from expr import *

R  = TypeVar('R')

@attr.s 
class Op(Generic[R]):

    @classmethod
    def build(cls) -> Op[R]: ... # Sig will be overloaded in children. 

    def members(self) -> Iterable[Expr]: ... 

    def dump(self) -> str: ... # Should always have this sig. 



# Numeric

@attr.s
class Neg(Op[R]):

    val : Expr = attr.ib()

    @overload 
    def build(cls, val : IntExpr) -> Op[IntExpr]: ... 
    @overload
    def build(cls, val : FloatExpr) -> Op[FloatExpr]: ...
    @overload
    def build(cls, val : RangeExpr[ScalarExpr]) -> Op[RangeExpr[ScalarExpr]]: ... 
    @overload
    def build(cls, val : ArrayExpr[NumericExpr]) -> Op[RangeExpr[NumericExpr]]: ...
    @classmethod
    def build(cls, val): 
        return Neg(val)

    def members(self): yield self.val

    def dump(self): return f'(-{self.val.dump()})'


@attr.s
class Add(Op[R]): 

    lhs : Expr = attr.ib() 
    rhs : Optional[Expr] = attr.ib() 

    @overload
    def build(cls, lhs: IntExpr, rhs: IntExpr) -> Op[IntExpr]: ...
    @overload
    def build(cls, lhs: FloatExpr, rhs: ScalarExpr) -> Op[FloatExpr]: ...
    @overload
    def build(cls, lhs: SV, rhs: SV) -> Op[SV]: ...
    @overload
    def build(cls, lhs: RangeExpr[SV], rhs: SV) -> Op[RangeExpr[SV]]: ...    @overload
    def build(cls, lhs: SV, rhs: RangeExpr[SV]) -> Op[RangeExpr[SV]]: ...
    @overload
    def build(cls, lhs: RangeExpr[SV], 
                   rhs: RangeExpr[SV]) -> Op[RangeExpr[SV]]: ...

"""
class Add(Op[Args],Generic[Args]):
    types = {
        Tuple[IntVal, IntVal] : IntVal,
        Tuple[FloatVal, ScalarVal] : FloatVal,
        Tuple[ScalarVal,FloatVal] : FloatVal,
    }
    pass

class Mul(Op[Args],Generic[Args]): pass

class Sum(Op[Args],Generic[Args]): pass

# Divisible
class Inv(Op[Args],Generic[Args]): pass

# Boolean
class Not(Op[Args],Generic[Args]): pass
class And(Op[Args],Generic[Args]): pass
class Or(Op[Args],Generic[Args]): pass
class Xor(Op[Args],Generic[Args]): pass
class Implies(Op[Args],Generic[Args]): pass

# Equality
class Eq(Op[Args],Generic[Args]): pass
class Neq(Op[Args],Generic[Args]): pass

# Equality + Set 
class AllEq(Op[Args],Generic[Args]): pass
class AllUnique(Op[Args],Generic[Args]): pass

# Ord 
class Gt(Op[Args],Generic[Args]): pass
class Gte(Op[Args],Generic[Args]): pass
class Lt(Op[Args],Generic[Args]): pass
class Lte(Op[Args],Generic[Args]): pass

# Min/Max 
class Min(Op[Args],Generic[Args]): pass
class Max(Op[Args],Generic[Args]): pass

# Range
class Hull(Op[Args],Generic[Args]): pass
class Intersection(Op[Args],Generic[Args]): pass

class Center(Op[Args],Generic[Args]): pass
class Width(Op[Args],Generic[Args]): pass

# Set 
class Extract(Op[Args],Generic[Args]): pass
 """