import libimagequant as liq
import PyQt6.QtGui

from . import _Qt


def to_liq(image: PyQt6.QtGui.QImage, attr: liq.Attr) -> liq.Image:
    """
    Convert PyQt6.QtGui.QImage to liq.Image.
    """
    return _Qt.to_liq(PyQt6.QtGui, image, attr, True)


def from_liq(result: liq.Result, image: liq.Image) -> PyQt6.QtGui.QImage:
    """
    Convert liq.Image to PyQt6.QtGui.QImage.
    """
    return _Qt.from_liq(PyQt6.QtGui, result, image)
