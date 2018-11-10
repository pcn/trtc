import logging
import math
from collections import namedtuple
from functools import reduce

import util
import tuples

_c = namedtuple('Canvas', ['width', 'height', 'pixels'])


def Canvas(width, height, fill=tuples.Color(0.0, 0.0, 0.0)):
    """Canvas appears to be a 2-dimensional structure.

    For the pixels, we're going to refer to them by width (x), height (y)
    because it seems natural.  However when storing and accessing them,
    it makes sense to have them be height, width (y, x) in the pixels tuple
    """
    pixels = [[fill] * int(width) for count in range(int(height))]
    return _c(width, height, pixels)

def write_pixel(canvas, width, height, value):
    """The book has this implemented as
    height, width for accesses"""
    canvas.pixels[height][width] = value
    return pixel_at(canvas, width, height)

def pixel_at(canvas, width, height):
    return canvas.pixels[height][width]


def _yield_row(row, least, most, ppm_max_line_len):
    """Yield a row as 1+ text lines in ppm pixel format, each line 
    limited to the ppm_max_line_len"""
    
    def _normalize_clamp_colors(input_generator):
        """for each value, clamp values between 0 and 1, and 
        then normalize that floating point number from 0 to 255"""
        for i in input_generator:
            if i <= 0.0:
                yield least
            elif i >= 1.0:
                yield most
            else:
                yield int(math.ceil(i * (most - least)))
                
    def _yield_colors():
        "provide each pixel as a series of red, green, and blue strings"
        for pix in row:
            yield pix.red
            yield pix.green
            yield pix.blue

    colors_stream = _yield_colors()
    line_pos = 0
    for this_pix_color in _normalize_clamp_colors(colors_stream):
        # print(f"line_pos is {line_pos}")
        speculative_len = (1 + line_pos + len(str(this_pix_color)))
        if speculative_len > ppm_max_line_len:
            # print(f"speculative_len is {speculative_len}, and it'll overrun")
            line_pos = 0
            yield "\n"
        if line_pos != 0:
            line_pos += (1 + len(str(this_pix_color)))
            yield " {}".format(this_pix_color)
        else:
            line_pos += len(str(this_pix_color))
            yield "{}".format(this_pix_color)
            

def canvas_to_ppm(c):
    """Canvas gets written out, 70 characters per line.  Each pixel is
    somewhere between 6 and 12 characters (r,g,b and spaces), so
    we have a generator that splits up each line.
    
    This doesn't provide newlines, those should be handled by the caller when e.g. writing to disk.
    """
    min_color = 0
    max_color = 255
    line_len = 70
    
    yield "P3"
    yield f"{len(c.pixels[0])} {len(c.pixels)}"
    yield f"{max_color}"
    # yield "\n"  # This is a separate yield to end up as the 4th element yielded
                # so the test for the header contents pass without the newline

    # for idx in range(len(c.pixels[0])):
    for line in c.pixels:
        # line = [ pix[idx] for pix in c.pixels ]
        print(f"Line is {line}")
        print(f"Len of line id {len(line)}")
        yield f'{"".join(_yield_row(line, min_color, max_color, line_len))}\n'
