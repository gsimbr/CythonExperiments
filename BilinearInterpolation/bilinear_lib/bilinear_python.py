def bilinear_interpolation_pure_python(
        q11, q12, q21, q22,  x1,  x2,
        y1, y2, x, y):
    x2x1 = x2 - x1
    y2y1 = y2 - y1
    x2x = x2 - x
    y2y = y2 - y
    yy1 = y - y1
    xx1 = x - x1
    return 1.0 / (x2x1 * y2y1) * (
        q11 * x2x * y2y +
        q21 * xx1 * y2y +
        q12 * x2x * yy1 +
        q22 * xx1 * yy1
    )
