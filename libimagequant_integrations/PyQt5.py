import libimagequant as liq
import PyQt5.QtGui

from . import _Qt


def to_liq(image: PyQt5.QtGui.QImage, attr: liq.Attr) -> liq.Image:
    """
    Convert PyQt5.QtGui.QImage to liq.Image.
    """
    return _Qt.to_liq(PyQt5.QtGui, image, attr, True)


def from_liq(result: liq.Result, image: liq.Image) -> PyQt5.QtGui.QImage:
    """
    Convert liq.Image to PyQt5.QtGui.QImage.
    """
    return _Qt.from_liq(PyQt5.QtGui, result, image)
