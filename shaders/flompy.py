from apps.shader.shaders.utils import vec2, vec3, mix
from math import sin, atan2, pow

def mainImage(fragCoord, iResolution, iTime):
    # input: pixel coordinates
    p = (-iResolution + fragCoord * 2.0) / iResolution.y

    # angle of each pixel to the center of the screen
    a = atan2(p.y,p.x)

    # Radius from centre
    r = pow(p.x*p.x + p.y*p.y, 0.5)

    # Scaled time
    t = iTime / 5.0

    scale = sin(t * 1.0)

    circles = vec3(
        sin(r * scale * 40.0),
        sin(r * scale * 40.0),
        sin(r * scale * 40.0)
    )

    radii = vec3 (
        sin(a * 60.0 + t * 60.0),
        sin(a * 60.0 + t * 60.0),
        sin(a * 60.0 + t * 60.0)
    )

    colour = mix(circles, radii, 0.5) + vec3(0.0, 0.0, 1.0)

    # output: pixel color
    return colour