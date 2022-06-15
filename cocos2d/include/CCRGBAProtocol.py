from __future__ import annotations

from ..include.ccColor3B import ccColor3B
from ..shaders.OpenGL import GLubyte

class CCRGBAProtocol:
    def setColor(self, color: ccColor3B) -> None: pass
    def getColor(self) -> ccColor3B: pass
    def getDisplayedColor(self) -> ccColor3B: pass
    def getDisplayedOpacity(self) -> GLubyte: pass
    def getOpacity(self) -> GLubyte: pass
    def setOpacity(self, opacity: GLubyte) -> None: pass
    def setOpacityModifyRGB(self, bValue: bool) -> None: pass
    def isOpacityModifyRGB(self) -> bool: pass
    def isCascadeColorEnabled(self) -> bool: pass
    def setCascadeColorEnabled(self, cascadeColorEnabled: bool) -> None: pass
    def updateDisplayedColor(self, color: ccColor3B) -> None: pass
    def isCascadeOpacityEnabled(self) -> bool: pass
    def setCascadeOpacityEnabled(self, cascadeOpacityEnabled: bool) -> None: pass
    def updateDisplayedOpacity(self, opacity: GLubyte) -> None: pass