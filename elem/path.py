import attr

from typing import * 
from enum import *

class Reserved(Enum):
    CONNECTED_LINK = auto()
    IS_CONNECTED = auto() 
    LENGTH = auto() 

Local = NewType('Local', str)

Index = NewType('Index', int)

Step = Union[Reserved, Local, Index]

Path = List[Step]