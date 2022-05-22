from __future__ import annotations

from include.CCLabelProtocol import CCLabelProtocol
from include.CCRGBAProtocol import CCRGBAProtocol
from sprite_nodes.CCSpriteBatchNode import CCSpriteBatchNode
from include.textAlignment import CCTextAlignment
from cocoa.CCPoint import CCPoint

class CCLabelBMFont(CCSpriteBatchNode, CCLabelProtocol, CCRGBAProtocol):
    def __init__(self) -> None: pass
    def __del__(self) -> None: pass
    @staticmethod
    def purgeCachedData() -> None: pass
    @staticmethod
    def create(string: str, fntFile: str, width: float, alignment: CCTextAlignment, imageOffset: CCPoint) -> CCLabelBMFont: pass
    @staticmethod
    def create_(string: str, fntFile: str, width: float, alignment: CCTextAlignment) -> CCLabelBMFont: pass
    @staticmethod
    def create__(string: str, fntFile: str, width: float) -> CCLabelBMFont: pass
    @staticmethod
    def create___(string: str, fntFile: str) -> CCLabelBMFont: pass
    @staticmethod
    def create____() -> CCLabelBMFont: pass
    def init(self) -> bool: pass
    def initWithString(self, string: str, fntFile: str, width: float=None, alignment: CCTextAlignment=None, imageOffset: CCPoint=CCPoint(0, 0)) -> bool: pass
    def createFontChars(self) -> None: pass