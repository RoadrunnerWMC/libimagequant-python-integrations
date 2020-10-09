# Shared function implementations for PyQt5 and PySide2


def to_liq(QtGui, image, attr, is_pyqt):
    """
    Convert QImage to liq.Image.
    """

    if image.format() != QtGui.QImage.Format_ARGB32:
        image = image.convertToFormat(QtGui.QImage.Format_ARGB32)

    image = image.rgbSwapped()

    rgba_data = image.bits()
    if is_pyqt:
        rgba_data = rgba_data.asstring(image.byteCount())

    return attr.create_rgba(rgba_data, image.width(), image.height(), 0)


def from_liq(QtGui, result, image):
    """
    Convert liq.Image to QImage.
    """

    out_img = QtGui.QImage(result.remap_image(image),
                           image.width,
                           image.height,
                           image.width,
                           QtGui.QImage.Format_Indexed8)
    out_img.setColorTable([QtGui.QColor(*color).rgba() for color in result.get_palette()])

    return out_img
