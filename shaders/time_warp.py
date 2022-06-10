from apps.shader.shaders.utils import vec2, vec3, mix, clamp
from math import sin, pow, atan2, sqrt


def annulus(p, centre, radius, thiccness):
    p = p - centre
    r = sqrt(p.x * p.x + p.y * p.y)
    if r > radius - thiccness / 2.0 and r < radius + thiccness / 2.0:
        return 1.0
    else:
        return 0.0


def hsv2rgb(c):
    K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0)
    p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www)
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y)

float float_mod(float a, float b) {
    return fract(a / b) * b
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    # input: pixel coordinates
    vec2 p = (-iResolution.xy + 2.0*fragCoord)/iResolution.y

    # angle of each pixel to the center of the screen
    float a = atan(p.y,p.x)

    # Radius from centre
    float r = pow(p.x*p.x + p.y*p.y, 0.5)

    # Scaled time
    float t = iTime * 2.0

    vec3 result = vec3(0.0, 0.0, 0.0)
    for (int i = 0 i < 8 i++) {
        float annulus_r = float_mod(t * 0.5 + float(i) * 0.5, 3.0)
        float circle = annulus(p, vec2(0.0, 0.0), annulus_r, 0.1)
        vec3 colour = hsv2rgb(vec3(float(i) / 7.0, 1.0, 1.0))
        result += circle * colour
    }

    # output: pixel color
    fragColor = vec4( result, 1.0 )
}


