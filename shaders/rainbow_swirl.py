from apps.shader.shaders.utils import vec2, vec3, mix
from math import sin, pow, atan2

def mainImage(fragCoord, iResolution, iTime):
    # input: pixel coordinates
    p = (-iResolution + fragCoord * 2.0) / iResolution.y

    # angle of each pixel to the center of the screen
    a = atan2(p.y, p.x)

    # Radius from centre
    r = pow(p.x*p.x + p.y*p.y, 0.5)

    # Scaled time
    t = iTime / 5.0

    col1 = vec3(
        1.0 * sin(4.0 * (r - t) + a),
        1.0 * sin(4.0 * (r - t) + a + 3.14 / 3.0),
        1.0 * sin(4.0 * (r - t * 2.0) + a + 3.14 * 2.0 / 3.0)
    )

    col2 = vec3(
        1.0 * sin(4.0 * (r * 0.5 + t * 0.2) + a + 3.14 / 3.0),
        1.0 * sin(4.0 * (r * 0.5 + t * 0.5) + a + 3.14 * 2.0 / 3.0),
        1.0 * sin(4.0 * (r * 0.5 + t * 0.5) + a)
    )

    col = mix(col1, col2, 0.5)

    # output: pixel color
    return col
