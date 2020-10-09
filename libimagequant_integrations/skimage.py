import libimagequant as liq
import numpy as np
import skimage


def to_liq(image: np.ndarray, attr: liq.Attr) -> liq.Image:
    """
    Convert numpy.ndarray to liq.Image.
    """
    if image.shape[2] != 4:
        raise ValueError('scikit-image array must be in RGBA format')

    return attr.create_rgba(skimage.img_as_ubyte(image), image.shape[1], image.shape[0], 0)


def from_liq(result: liq.Result, image: liq.Image) -> np.ndarray:
    """
    Convert liq.Image to two numpy.ndarray's (for pixel and palette data).
    """

    arr = np.frombuffer(result.remap_image(image), dtype=np.uint8)
    out_img = np.reshape(arr,
                         (image.height, image.width, 1))
    out_pal = np.array(result.get_palette())

    return out_img, out_pal
