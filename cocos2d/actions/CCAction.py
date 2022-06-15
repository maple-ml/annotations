from __future__ import annotations

from ..cocoa.CCObject import CCObject
from ..actions.CCZone import CCZone

class CCAction(CCObject):
    def __init__(self) -> CCAction: pass
    def description(self) -> str: pass
    def copyWithZone(self, pZone: CCZone) -> CCObject: pass
    def isDone(self) -> bool: pass
    def startWithTarget(self, pTarget: "CCNode") -> None: pass
    def stop(self) -> None: pass
    def step(self, dt: float) -> None: pass
    def update(self, time: float) -> None: pass
    def getTarget(self) -> "CCNode": pass
    def setTarget(self, pTarget: "CCNode") -> None: pass
    def getOriginalTarget(self) -> "CCNode": pass
    def setOriginalTarget(self, pTarget: pOriginalTarget) -> None: pass
    def setSpeedMod(self, mod: float) -> None: pass
    @staticmethod
    def create() -> CCAction: pass