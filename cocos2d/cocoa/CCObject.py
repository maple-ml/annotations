from __future__ import annotations

from ..cocoa.CCDataVisitor import CCDataVisitor
from ..cocoa.CCObjectType import CCObjectType
from ..cocoa.CCCopying import CCCopying

class CCObject(CCCopying):
    def release(self) -> None: pass
    def retain(self) -> None: pass
    def autorelease(self) -> CCObject: pass
    def copy(self) -> CCObjet: pass
    def isSingleReference(self) -> bool: pass
    def retainCount(self) -> int: pass
    def isEqual(self, pObject: CCObject) -> bool: pass
    # python == operator
    def __eq__(self, other) -> bool: return self.isEqual(pObject)
    def update(self, dt: float) -> None: pass
    def getTag(self) -> int: pass
    def setTag(self, nTag: int) -> None: pass
    def setObjType(self, type: CCObjectType) -> None: pass