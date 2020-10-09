import libimagequant as liq
import PIL.Image


def to_liq(image: PIL.Image.Image, attr: liq.Attr) -> liq.Image:
    """
    Convert PIL.Image.Image to liq.Image.
    """

    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    return attr.create_rgba(image.tobytes(), image.width, image.height, image.info.get('gamma', 0))


def from_liq(result: liq.Result, image: liq.Image) -> PIL.Image.Image:
    """
    Convert liq.Image to PIL.Image.Image.
    """

    out_img = PIL.Image.frombytes('P',
                                  (image.width, image.height),
                                  result.remap_image(image))

    palette_data = []
    for color in result.get_palette():
        palette_data.extend(color[:3])
    out_img.putpalette(palette_data)

    return out_img
