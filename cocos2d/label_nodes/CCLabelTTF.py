from __future__ import annotations

from ..sprite_nodes.CCSprite import CCSprite
from ..include.CCLabelProtocol import CCLabelProtocol
from ..include.CCSize import CCSize
from ..include.ccFontDefinition import ccFontDefinition
from ..include.textAlignment import CCTextAlignment
from ..include.textAlignment import CCVerticalTextAlignment
from ..include.ccColor3B import ccColor3B

class CCLabelTTF(CCSprite, CCLabelProtocol):
    def __init__(self) -> None: pass
    def __del__(self) -> None: pass
    def description(self) -> str: pass
    @staticmethod
    def create(string: str, fontName: str, fontSize: float) -> CCLabelTTF: pass
    @staticmethod
    def create_(string: str, fontName: str, fontSize: float, dimensions: CCSize, hAlignment: CCTextAlignment) -> CCLabelTTF: pass
    @staticmethod
    def create__(string: str, fontName: str, fontSize: float, dimensions: CCSize, hAlignment: CCTextAlignment, vAlignment: CCVerticalTextAlignment) -> CCLabelTTF: pass
    @staticmethod
    def createWithFontDefinition(string: str, textDefinion: ccFontDefinition) -> CCLabelTTF: pass
    def initWithString(self, string: str, fontName: str, fontSize: float) -> bool: pass
    def initWithString_(self, string: str, fontName: str, fontSize: float, dimensions: CCSize, hAlignment: CCTextAlignment) -> bool: pass
    def initWithString__(self, string: str, fontName: str, fontSize: float, dimensions: CCSize, hAlignment: CCTextAlignment, vAlignment: CCVerticalTextAlignment) -> bool: pass
    def initWithStringAndTextDefinition(self, string: str, textDefinition: ccFontDefinition) -> bool: pass
    def setTextDefinition(self, theDefinition: ccFontDefinition) -> None: pass
    def getTextDefinition(self) -> ccFontDefinition: pass
    def enableShadow(self, shadowOffset: CCSize, shadowOpacity: float, shadowBlur: float, mustUpdateTexture: bool=True) -> None: pass
    def disableShadow(self, mustUpdateTexture: bool=True) -> None: pass
    def enableStroke(self, strokeColor: ccColor3B, strokeSize: float, mustUpdateTexture: bool=True) -> None: pass
    def disableStroke(self, mustUpdateTexture: bool=True) -> None: pass
    def setFontFillColor(tintColor: ccColor3B, mustUpdateTexture: bool=True) -> None: pass
    def init(self) -> bool: pass
    @staticmethod
    def create___() -> None: pass
    def setString(self, label: str) -> None: pass
    def getString(self) -> str: pass