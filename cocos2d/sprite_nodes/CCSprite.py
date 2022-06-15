from __future__ import annotations

from ..base_nodes.CCNodeRGBA import CCNodeRGBA
from ..include.CCTextureProtocol import CCTextureProtocol
from ..cocoa.CCRect import CCRect
from ..textures.CCTexture2D import CCTexture2D
from ..sprite_nodes.CCSpriteFrame import CCSpriteFrame

class CCSprite(CCNodeRGBA, CCTextureProtocol):
    @staticmethod
    def create() -> CCSprite: pass
    @staticmethod
    def create_(pszFileName: str) -> CCSprite: pass
    @staticmethod
    def create__(pszFileName: str, rect: CCRect) -> CCSprite: pass
    @staticmethod
    def createWithTexture(pTexture: CCTexture2D) -> CCSprite: pass
    @staticmethod
    def createWithTexture_(pTexture: CCTexture2D, rect: CCRect) -> CCSprite: pass
    @staticmethod
    def createWithSpriteFrame(pSpriteFrame: CCSpriteFrame) -> CCSprite: pass
    @staticmethod
    def createWithSpriteFrameName(pszSpriteFrameName: str) -> CCSprite: pass
    def __init__(self) -> None: pass
    def __del__(self) -> None: pass
    def init(self) -> bool: pass
    def initWithTexture(self, pTexture: CCTexture2D) -> bool: pass
    def initWithTexture_(self, pTexture: CCTexture2D, rect: CCRect) -> bool: pass
    def initWithTexture__(self, pTexture: CCTexture2D, rect: CCRect, rotated: bool) -> bool: pass
    def initWithSpriteFrame(self, pSpriteFrame: CCSpriteFrame) -> bool: pass
    def initWithSpriteFrameName(self, pszSpriteFrameName: str) -> bool: pass
    def initWithFile(self, pszFilename: str) -> bool: pass
    def initWithFile_(self, pszFilename: str, rect: CCRect) -> bool: pass
    def setChildColor(self, color: ccColor3B) -> None: pass
    def setChildOpacity(self, opacity: GLubyte) -> None: pass