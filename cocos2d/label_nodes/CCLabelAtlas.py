from __future__ import annotations

from ..textures.CCTexture2D import CCTexture2D
from ..include.CCLabelProtocol import CCLabelProtocol
from ..base_nodes.CCAtlasNode import CCAtlasNode

class CCLabelAtlas(CCAtlasNode, CCLabelProtocol):
    def __init__(self) -> CCLabelAtlas: pass
    def __del__(self) -> None: pass
    @staticmethod
    def create(string: str, charMapFile: str, itemWidth: int, itemHeight: int, startCharMap: int) -> CCLabelAtlas: pass
    @staticmethod
    def create_(string: str, fntFile: str) -> CCLabelAtlas: pass
    def initWithString(self, string: str, charMapFile: str, itemWidth: int, itemHeight: int, startCharMap: int) -> bool: pass
    def initWithString_(self, string: str, fntFile: str) -> bool: pass
    def initWithString__(self, string: str, texture: CCTexture2D, itemWidth: int, itemHeight: int, startCharMap: int) -> bool: pass