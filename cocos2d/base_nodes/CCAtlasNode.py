from __future__ import annotations

from base_nodes.CCNode import CCNode
from base_nodes.CCNodeRGBA import CCNodeRGBA
from include.CCTextureProtocol import CCTextureProtocol
from textures.CCTexture2D import CCTexture2D
from shaders.OpenGL import GLubyte
from include.ccColor3B import ccColor3B

class CCAtlasNode(CCNodeRGBA, CCTextureProtocol):
    def __init__(self) -> CCNode: pass
    def __del__(self) -> CCNode: pass
    @staticmethod
    def create(title: str, tileWidth: int, tileHeight: int, itemsToRender: int) -> CCAtlasNode: pass
    def initWithTileFile(self, title: str, tileWidth: int, tileHeight: int, itemsToRender: int) -> bool: pass
    def initWithTexture(self, texture: CCTexture2D, tileWidth: int, tileHeight: int, itemsToRender: int) -> bool: pass
    def updateAtlasValues(self) -> None: pass
    def draw(self) -> None: pass
    def getTexture(self) -> CCTexture2D: pass
    def setTexture(self, texture: CCTexture2D) -> None: pass
    def isOpacityModifyRGB(self) -> bool: pass
    def setOpacityModifyRGB(self, isOpacityModifyRGB: bool) -> None: pass
    def getColor(self) -> ccColor3B: pass
    def setColor(self, color: ccColor3B) -> None: pass
    def setOpacity(self, opacity: GLubyte) -> None: pass
