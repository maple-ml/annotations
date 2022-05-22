from __future__ import annotations

from shaders.OpenGL import GLuint

class CCGLBufferedNode:
    def __init__(self) -> CCGLBufferedNode: pass
    def setGLBufferData(self, buf, bufSize: GLuint, slot: int) -> None: pass
    def setGLIndexData(self, buf, bufSize: GLuint, slot: int) -> None: pass