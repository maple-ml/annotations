from __future__ import annotations

from actions.CCAction import CCAction
from base_nodes.CCNode import CCNode
from cocoa.CCRect import CCRect
from cocoa.CCObject import CCObject
from actions.CCZone import CCZone

class CCFollow(CCAction):
    def isBoundarySet(self) -> bool: pass
    def setBoudarySet(self, bValue: bool) -> None: pass
    def initWithTarget(self, pFollowedNode: CCNode, rect: CCRect) -> CCNode: pass
    def copyWithZone(self, pZone: CCZone) -> CCObject: pass
    def step(self, dt: float) -> None: pass
    def isDone(self) -> bool: pass
    def stop(self) -> None: pass
    @staticmethod
    def create(pFollowedNode: CCNode, rect: CCRect) -> CCNode: pass