from __future__ import annotations

from actions.CCAction import CCAction
from actions.CCActionInterval import CCActionInterval

class CCSpeed(CCAction):
    def getSpeed(self) -> float: pass
    def setSpeed(self, fSpeed: float) -> None: pass
    def initWithAction(self, pAction: CCActionInterval, fSpeed: float) -> bool: pass
    def setInnerAction(self, pAction: CCActionInterval) -> None: pass
    def getInnerAction(self) -> CCActionInterval: pass
    @staticmethod
    def create(pAction: CCActionInterval, fSpeed: float) -> CCSpeed: pass