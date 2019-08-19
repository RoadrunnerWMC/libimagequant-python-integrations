Python libimagequant Integrations
=================================

This library provides helper functions for converting between objects in the
[unofficial Python libimagequant bindings library](http://libimagequant-python.readthedocs.io/)
and "image" objects in various popular Python libraries.

If you'd like to add support for integration with more libraries, pull requests
are welcome!

Install with pip:

    python3 -m pip install libimagequant_integrations
    

API Documentation
-----------------

This package contains the following submodules, for converting to/from the
indicated classes:

* `libimagequant_integrations.PIL` (for Pillow's `PIL.Image.Image`)
* `libimagequant_integrations.PySide2` (for `PySide2.QtGui.QImage`)
* `libimagequant_integrations.PyQt5` (for `PyQt5.QtGui.QImage`)
* `libimagequant_integrations.skimage` (for scikit-image numpy arrays<sup>[†](#skimage)</sup>)

I suggest you import using (for example)
`import libimagequant_integrations.PyQt5 as liq_PyQt5`, to avoid typing an
excessive amount. :)

Each submodule contains two functions, used to convert to and from the
`libimagequant.Image` class:

    to_liq(image: OtherImageClass, attr: libimagequant.Attr) -> libimagequant.Image

    from_liq(result: libimagequant.Result, image: libimagequant.Image) -> OtherImageClass

(Replace `OtherImageClass` with the appropriate other image class.)

<sup><a name="skimage">†</a></sup>
Give `to_liq()` an RGBA image (numpy array of shape `(y, x, 4)`, with
uint8-type elements) as its "image" argument. `from_liq()` returns two numpy
arrays: one with pixel data (shape `(y, x, 1)`, uint8-type elements), and one
with the RGBA color palette (shape `(n, 4)`, uint8-type elements).


License
-------

Licensed under the GNU GPL v3. See the `LICENSE` file for the full license
text.
