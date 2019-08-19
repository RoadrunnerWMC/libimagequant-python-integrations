import libimagequant as liq
import PySide2.QtGui

from . import _Qt


def to_liq(image: PySide2.QtGui.QImage, attr: liq.Attr) -> liq.Image:
    """
    Convert PySide2.QtGui.QImage to liq.Image.
    """
    return _Qt.to_liq(PySide2.QtGui, image, attr, False)


def from_liq(result: liq.Result, image: liq.Image) -> PySide2.QtGui.QImage:
    """
    Convert liq.Image to PySide2.QtGui.QImage.
    """
    return _Qt.from_liq(PySide2.QtGui, result, image)
