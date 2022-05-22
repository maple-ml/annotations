from __future__ import annotations

from sprite_nodes.CCSprite import CCSprite
from include.CCLabelProtocol import CCLabelProtocol
from include.CCSize import CCSize
from unknown.CCTextAlignment import CCTextAlignment
from unknown.CCVerticalTextAlignment import CCVerticalTextAlignment

class CCLabelTTF(CCSprite, CCLabelProtocol):
    def __init__(self) -> None: pass
    def __del__(self) -> None: pass
    def description(self) -> str: pass
    @staticmethod
    def create(string: str, fontName: str, fontSize: float) -> CCLabelTTF: pass
    @staticmethod
    def create(string: str, fontName: str, fontSize: float, dimensions: CCSize, hAlignment: CCTextAlignment) -> CCLabelTTF: pass
    @staticmethod
    def create(string: str, fontName: str, fontSize: float, dimensions: CCSize, hAlignment: CCTextAlignment, vAlignment: CCVerticalTextAlignment) -> CCLabelTTF: pass
    def createWithFontDefinition(self, string: str, textDefinion: )