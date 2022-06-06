from __future__ import annotations

from cocoa.CCPoint import CCPoint
from cocoa.CCArray import CCArray
from cocoa.CCSize import CCSize
from cocoa.CCObject import CCObject
from cocoa.CCRect import CCRect
from shaders.CCGLProgram import CCGLProgram
from shaders.ccGLServerState import ccGLServerState
from actions.CCActionManager import CCActionManager
from actions.CCAction import CCAction
from touch_dispatcher.CCTouch import CCTouch

class CCNode(CCObject):
    def __init__(self) -> CCNode: pass
    def __del__(self) -> None: pass
    @staticmethod
    def create() -> CCNode: pass
    def init(self) -> bool: pass
    def description(self) -> str: pass
    def setZOrder(self, zOrder: int) -> None: pass
    def _setZOrder(self, zOrder: int) -> None: pass
    def getZOrder(self) -> int: pass
    def setVertexZ(self, vertexZ: int) -> None: pass
    def getVertexZ(self) -> int: pass
    def setScaleX(self, fScaleX: float) -> None: pass
    def getScaleX(self) -> float: pass
    def setScaleY(self, fScaleY: float) -> None: pass
    def getScaleY(self) -> float: pass
    def setScale(self, scale: float) -> None: pass
    def getScale(self) -> float: pass
    def setPosition(self, position: CCPoint) -> None: pass
    def getPosition(self) -> CCPoint: pass
    def setPosition_(self, x: float, y: float) -> None: pass
    def setPositionX(self, x: float) -> None: pass
    def getPositionX(self) -> float: pass
    def setPositionY(self, y: float) -> None: pass
    def getPositionY(self) -> float: pass
    def setSkewX(self, fSkewX: float) -> None: pass
    def getSkewX(self) -> float: pass
    def setSkewY(self, fSkewY: float) -> None: pass
    def getSkewY(self) -> float: pass
    def setAnchorPoint(self, anchorPoint: CCPoint) -> None: pass
    def getAnchorPoint(self) -> CCPoint: pass
    def getAnchorPointInPoints(self) -> CCPoint: pass
    def setContentSize(self, contentSize: CCSize) -> None: pass
    def getContentSize(self) -> CCSize: pass
    def getScaledContentSize(self) -> CCSize: pass
    def setVisible(self, visible: bool) -> None: pass
    def isVisible(self) -> bool: pass
    def setRotation(self, fRotation: float) -> None: pass
    def getRotation(self) -> float: pass
    def setRotationX(self, x: float) -> None: pass
    def getRotationX(self) -> float: pass
    def setRotationY(self, y: float) -> None: pass
    def getRotationY(self) -> float: pass
    def setOrderOfArrival(self, uOrderOfArrival: int) -> None: pass
    def getOrderOfArrival(self) -> int: pass
    def setGLServerState(self, glServerState: ccGLServerState) -> None: pass
    def getGLServerState(self) -> ccGLServerState: pass
    def ignoreAnchorPointForPosition(self, ignore: bool) -> bool: pass
    def isIgnoreAnchorPointForPosition(self) -> bool: pass
    def addChild(self, child: CCNode) -> None: pass
    def addChild_(self, child: CCNode, zOrder: int) -> None: pass
    def addChild__(self, child: CCNode, zOrder: int, tag: int) -> None: pass
    def getChildByTag(self, tag: int) -> CCNode: pass
    def getChildren(self) -> CCArray: pass
    def getChildrenCount(self) -> int: pass
    def setParent(self, parent: CCNode) -> None: pass
    def getParent(self) -> CCNode: pass
    def removeFromParent(self) -> None: pass
    def removeFromParentAndCleanup(self, cleanup: bool) -> None: pass
    def removeChild(self, child: CCNode) -> None: pass
    def removeChild_(self, child: CCNode, cleanup: bool) -> None: pass
    def removeChildByTag(self, tag: int) -> None: pass
    def removeChildByTag_(self, tag: int, cleanup: bool) -> None: pass
    def removeChildren(self) -> None: pass
    def removeChildrenWithCleanup(self, cleanup: bool) -> None: pass
    def reorderChild(self, child: CCNode, zOrder: int) -> None: pass
    def sortAllChildren(self) -> None: pass
    def getGrid(self) -> CCGridBase: pass
    def setGrid(self, pGrid: CCGridBase) -> None: pass
    def getTag(self) -> int: pass
    def setTag(self, nTag: int) -> None: pass
    def getUserData(self): pass
    def setUserData(self, pUserData) -> None: pass
    def getUserObject(self) -> CCObject: pass
    def setUserObject(self, pUserObject: CCObject) -> None: pass
    def getShaderProgram(self) -> CCGLProgram: pass
    def setShaderProgram(self, pShaderProgram: CCGLProgram) -> None: pass
    def getCamera(self) -> CCCamera: pass
    def isRunning(self) -> bool: pass
    def registerScriptHandler(self, handler: int) -> None: pass
    def unregisterScriptHandler(self) -> None: pass
    def onEnter(self) -> None: pass
    def onEnterTransitionDidFinish(self) -> None: pass
    def onExit(self) -> None: pass
    def onExitTransitionDidStart(self) -> None: pass
    def cleanup(self) -> None: pass
    def draw(self) -> None: pass
    def visit(self) -> None: pass
    def boundingBox(self) -> CCRect: pass
    def setActionManager(self, actionManager: CCActionManager) -> None: pass
    def getActionManager(self) -> CCActionManager: pass
    def runAction(self, action: CCAction) -> CCAction: pass
    def stopAllActions(self) -> None: pass
    def stopAction(self, action: CCAction) -> None: pass
    def stopActionByTag(self, tag: int) -> CCAction: pass
    def getActionByTag(self, tag: int) -> CCAction: pass
    def numberOfRunningActions(self) -> int: pass
    def setScheduler(self, scheduler: CCScheduler) -> None: pass
    def getScheduler(self) -> CCScheduler: pass
    def isScheduler(self, scheduler) -> bool: pass
    def scheduleUpdate(self) -> None: pass
    def scheduleUpdateWithPriority(self, priority: int) -> None: pass
    def unscheduleUpdate(self) -> None: pass
    def schedule(self, selector, interval: float, repeat: int, delay: float) -> None: pass
    def schedule_(self, selector, interval: float) -> None: pass
    def scheduleOnce(self, selector, delay: float) -> None: pass
    def schedule__(self, selector) -> None: pass
    def unschedule(self, selector) -> None: pass
    def unscheduleAllSelectors(self) -> None: pass
    def resumeSchedulerAndActions(self) -> None: pass
    def pauseSchedulerAndActions(self) -> None: pass
    def update(self, delta: float) -> None: pass
    def transform(self) -> None: pass
    def transformAncestors(self) -> None: pass
    def updateTransform(self) -> None: pass
    def convertToNodeSpace(self, worldPoint: CCPoint) -> CCPoint: pass
    def convertToWorldSpace(self, nodePoint: CCPoint) -> CCPoint: pass
    def convertToNodeSpaceAR(self, worldPoint: CCPoint) -> CCPoint: pass
    def convertToWorldSpaceAR(self, nodePoint: CCPoint) -> CCPoint: pass
    def convertTouchToNodeSpace(self, touch: CCTouch) -> CCPoint: pass
    def convertTouchToNodeSpaceAR(self, touch: CCTouch) -> CCPoint: pass