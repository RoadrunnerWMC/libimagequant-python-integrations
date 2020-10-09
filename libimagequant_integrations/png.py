import libimagequant as liq
import png

_LIQ_DEFAULT_GAMMA = 0.45455


def to_liq(image: png.Reader, attr: liq.Attr) -> liq.Image:
    """
    Convert png.Reader to liq.Image.
    """
    width, height, data, info = image.read_flat()
    return attr.create_rgba(data, width, height, info.get('gamma', 0))


def from_liq(result: liq.Result, image: liq.Image) -> (png.Writer, bytes):
    """
    Convert liq.Image to a (writer: png.Writer, data: bytes) tuple.
    You can save the image to file f using writer.write_array(f, data).
    """
    gamma = result.output_gamma
    if gamma == _LIQ_DEFAULT_GAMMA:
        gamma = None

    writer = png.Writer(image.width,
                        image.height,
                        palette=result.get_palette(),
                        gamma=gamma)
    data = result.remap_image(image)
    return writer, data
