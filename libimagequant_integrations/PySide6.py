import libimagequant as liq
import PySide6.QtGui

from . import _Qt


def to_liq(image: PySide6.QtGui.QImage, attr: liq.Attr) -> liq.Image:
    """
    Convert PySide6.QtGui.QImage to liq.Image.
    """
    return _Qt.to_liq(PySide6.QtGui, image, attr, False)


def from_liq(result: liq.Result, image: liq.Image) -> PySide6.QtGui.QImage:
    """
    Convert liq.Image to PySide6.QtGui.QImage.
    """
    return _Qt.from_liq(PySide6.QtGui, result, image)
