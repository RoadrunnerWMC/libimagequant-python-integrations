import warnings

# NOTE: importing PySide2 before anything else fixes some weird linking
# errors I'm experiencing, for some reason
try:
    import PySide2.QtGui
    import libimagequant_integrations.PySide2 as liq_PySide2
except ImportError:
    PySide2 = None

try:
    # PIL internally raises some DeprecationWarnings upon import --
    # block those so they don't affect our actual tests
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        import PIL.Image
        import libimagequant_integrations.PIL as liq_PIL
except ImportError:
    PIL = None

try:
    import PyQt5.QtGui
    import libimagequant_integrations.PyQt5 as liq_PyQt5
except ImportError:
    PyQt5 = None

try:
    import skimage.io
    import numpy as np
    import libimagequant_integrations.skimage as liq_skimage
except ImportError:
    skimage = None

import libimagequant as liq
import pytest


TEST_IMAGE_1 = 'test_res/gradient.png'
TEST_POINTS_1 = [
    # ((x,   y), (  r,   g,   b,   a))
    ((  0,   0), (  0,   0, 128, 255)),
    ((511,   0), (255,   0, 139, 255)),
    ((  0, 511), (  0, 255, 117, 255)),
    ((511, 511), (255, 255, 126, 255))]
TEST_IMAGE_2 = 'test_res/gradient_alpha.png'
TEST_POINTS_2 = [
    # ((x,   y), (  r,   g,   b,   a))
    ((  0,   0), (  0,   0, 128, 254)),
    ((511,   0), (255,   0, 139, 127)),
    ((  0, 511), (  0, 255, 117, 127)),
    ((511, 511), (255, 255, 126, 0))]


def near(a, b):
    """
    Helper function for checking if a is "near" b.
    Feel free to adjust the tolerance as necessary. The goal here is to
    ensure that the color channels aren't getting accidentally swapped,
    not to rate libimagequant on how good of a job it's doing.
    """
    return abs(a - b) < 30


@pytest.mark.skipif(PIL is None, reason='Pillow is not available')
def test_PIL():
    """
    Test libimagequant_integrations.PIL
    """
    def test_against(image_filename, points):
        pil_in = PIL.Image.open(image_filename)

        for pos, expected in points:
            assert pil_in.getpixel(pos) == expected

        attr = liq.Attr()
        img = liq_PIL.to_liq(pil_in, attr)

        result = img.quantize(attr)
        pil_out = liq_PIL.from_liq(result, img)

        assert pil_out.mode == 'P'

        pil_out_rgba = pil_out.convert('RGBA')

        for pos, expected in points:
            r, g, b, a = pil_out_rgba.getpixel(pos)
            print(pos, expected, (r, g, b, a))
            assert near(r, expected[0])
            assert near(g, expected[1])
            assert near(b, expected[2])
            assert near(a, expected[3])

    test_against(TEST_IMAGE_1, TEST_POINTS_1)
    # PIL doesn't support paletted images with transparency (the "PA"
    # image mode actually uses separate index and alpha channels for
    # each pixel), so we don't test against image 2


def run_qt_test(liq_Qt, QtGui):
    """
    Test PyQt5 or PySide2
    """
    app = QtGui.QGuiApplication([])

    def test_against(image_filename, points):
        q_in = QtGui.QImage(image_filename)

        for pos, expected in points:
            qcolor = q_in.pixelColor(*pos)
            assert (qcolor.red(), qcolor.green(), qcolor.blue(), qcolor.alpha()) == expected

        attr = liq.Attr()
        img = liq_Qt.to_liq(q_in, attr)

        result = img.quantize(attr)
        q_out = liq_Qt.from_liq(result, img)

        assert q_out.format() == QtGui.QImage.Format_Indexed8

        q_out_rgba = q_out.convertToFormat(QtGui.QImage.Format_ARGB32)

        for pos, expected in points:
            qcolor = q_out_rgba.pixelColor(*pos)
            r, g, b, a = qcolor.red(), qcolor.green(), qcolor.blue(), qcolor.alpha()
            print(pos, expected, (r, g, b, a))
            assert near(r, expected[0])
            assert near(g, expected[1])
            assert near(b, expected[2])
            assert near(a, expected[3])

    test_against(TEST_IMAGE_1, TEST_POINTS_1)
    test_against(TEST_IMAGE_2, TEST_POINTS_2)


@pytest.mark.skipif(PyQt5 is None, reason='PyQt5 is not available')
def test_PyQt5():
    """
    Test libimagequant_integrations.PyQt
    """
    run_qt_test(liq_PyQt5, PyQt5.QtGui)


@pytest.mark.skipif(PySide2 is None, reason='PySide2 is not available')
@pytest.mark.xfail(reason='QImage has been almost completely broken in PySide2 for years')
def test_PySide2():
    """
    Test libimagequant_integrations.PySide2
    """
    run_qt_test(liq_PySide2, PySide2.QtGui)


@pytest.mark.skipif(skimage is None, reason='scikit-image is not available')
def test_skimage():
    """
    Test libimagequant_integrations.skimage
    """
    def test_against(image_filename, points):
        sk_in = skimage.io.imread(image_filename)
        assert sk_in.shape[2] == 4

        for (x, y), expected in points:
            assert np.array_equal(sk_in[y, x], np.array(expected))

        attr = liq.Attr()
        img = liq_skimage.to_liq(sk_in, attr)

        result = img.quantize(attr)
        sk_out_px, sk_out_pal = liq_skimage.from_liq(result, img)

        assert sk_out_px.shape[2] == 1
        assert sk_out_pal.shape[1] == 4

        for (x, y), expected in points:
            r, g, b, a = sk_out_pal[sk_out_px[y, x][0]]
            print((x, y), expected, (r, g, b, a))
            assert near(r, expected[0])
            assert near(g, expected[1])
            assert near(b, expected[2])
            assert near(a, expected[3])

    test_against(TEST_IMAGE_1, TEST_POINTS_1)
    test_against(TEST_IMAGE_2, TEST_POINTS_2)
