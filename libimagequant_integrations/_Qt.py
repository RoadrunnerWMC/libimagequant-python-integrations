# Shared function implementations for PyQt5 and PySide2


def to_liq(QtGui, image, attr, is_pyqt):
    """
    Convert QImage to liq.Image.
    """

    if image.format() != QtGui.QImage.Format_ARGB32:
        image = image.convertToFormat(QtGui.QImage.Format_ARGB32)

    argb_data = image.bits()
    if is_pyqt:
        argb_data = argb_data.asstring(image.byteCount())

    # BGRA -> RGBA
    def gen_rgba_indices():
        for i in range(0, len(argb_data), 4):
            yield i + 2 # r
            yield i + 1 # g
            yield i + 0 # b
            yield i + 3 # a
    rgba_data = bytes(argb_data[idx] for idx in gen_rgba_indices())

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
    out_img.setColorTable([QtGui.QColor(*color).rgb() for color in result.get_palette()])

    return out_img
