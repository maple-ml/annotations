from __future__ import annotations

from ..actions.CCAction import CCAction

class CCFiniteTimeAction(CCAction):
    def getDuration(self) -> float: pass
    def setDuration(self, duration: float) -> None: pass
    def reverse(self) -> CCFiniteTimeAction: pass