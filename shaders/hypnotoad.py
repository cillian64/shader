from apps.shader.shaders.utils import vec2, vec3, mix
from math import sin, pow, atan2

def mainImage(fragCoord, iResolution, iTime):
    # input: pixel coordinates
    p = (-iResolution + fragCoord * 2.0) / iResolution.y

    # angle of each pixel to the center of the screen
    a = atan2(p.y,p.x)

    # Radius from centre
    r = pow(p.x*p.x + p.y*p.y, 0.5)

    # Scaled time
    t = iTime * 10.0

    colour = vec3(
        sin(r * 40.0 + a - t) + 0.5,
        sin(r * 40.0 + a - t) + 0.5,
        sin(r * 40.0 + a - t) + 0.5
    )

    # output: pixel color
    return colour