import attr
import abc

from typing import * 
from enum import *
from .path import * 

V = TypeVar('V', bound='Value')

class InvalidPathError(Exception): 
    """Path doesn't point to anything."""
    pass 

class InvalidPathMemberError(Exception): 
    """Intermediate element on path doesn't have members."""
    pass 

class InconsistentPathError(Exception): 
    """Path between wrapper and target doesn't point to self."""
    pass 

class IncompletePathError(Exception): 
    """The path references are broken somehow."""
    pass 

class NotParentWrapperError(Exception): 
    """The wrapper provided isn't a parent of this value."""
    pass


@attr.s
class Value():
    path : Optional[Path] = attr.ib(default=None) 
    """Path from container to this value"""

    wrapper : Optional[Wrapper] = attr.ib(kw_only=True)
    """Nearest parent wrapper""" 

    @abc.abstractmethod
    def _merge_(self: V, other: V) -> V: ...
    """How to combine two values being bound to the same ref.""" 

    def path_from(self, wrap: Wrapper) -> Path:
        """Get the path from the wrapper value to self."""
        out_path : Path = list() 
        cur_val  = self
        while cur_val.wrapper:
            if not cur_val.path:
                raise IncompletePathError() 
            else: 
                out_path = cur_val.path.copy() + out_path

            if cur_val.wrapper == wrap:
                if wrap.lookup_path(out_path) != self: 
                    raise InconsistentPathError()
                return out_path
            
        raise NotParentWrapperError() 

W = TypeVar('W', bound='Wrapper')

@attr.s 
class Wrapper(Value):
    members : dict[Step,Value] = attr.ib(factory=dict)

    def set_val(self, step: Step, val: Value):
        # Get new value for wrapper 
        curr = self.members.get(step,None)
        new = curr._merge_(val) if curr else val 
        # Enforce container invariants
        new.wrapper = self 
        new.path = [step]
        # Insert into map
        self.members[step] = new 

    def get_val(self, step: Step) -> Optional[Value]: 
        return self.members.get(step,None)
            
    def path_to(self, value: Value) -> Path: 
        return value.path_from(self)
        
    def lookup_path(self, path: Path) -> Value: 
        curr : Value = self 
        for step in path: 
            if not isinstance(curr, Wrapper): 
                raise InvalidPathMemberError()

            next = curr.get_val(step)

            if not next: 
                raise InvalidPathError()

            curr = next

        return curr 

    def _merge_(self: W, other: W) -> W: 
        for (s,v) in other.members.items(): 
            self.set_val(s,v)
        return self

        





