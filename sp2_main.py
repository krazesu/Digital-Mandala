from sp2_mandala import *

if __name__ == '__main__':
    #initialize the shuriken like christmas star
    shuriken = Mandala((5000,5000), ((250,250,250)))

    #colors:
    color_g = (0,127,0)
    color_r = (153,0,0)

    #draw rotating diamonds with with increasing sizes and different colors
    size = 0
    color_ctr = 0
    while size < 5:
        angle_pivot = 0
        angle = 0
        while angle_pivot < 360:
            if color_ctr % 2 == 0: color = color_g
            else: color = color_r

            center_pivot = shuriken.rotate_point((2500,2000), (2500,2500), angle_pivot)
            shuriken.draw_diamond(center_pivot, size, angle, color)
            angle += 15
            angle_pivot += 15
        color_ctr += 1
        size += 0.25

    #draw rotating triangles inside the rotating diamonds to create the hole of the shuriken
    angle = 0
    gradient_g = 255
    gradient_r = 0
    while angle < 360:
        shuriken.draw_triangle((2500, 2500), 860, angle, (gradient_r, gradient_g, 0))
        angle += 5
        gradient_g -= 1
        gradient_r += 2

    #draw additional elements at the tip of the diamonds 

    #draw diamonds in increasing size at tip of the rotating diamonds
    angle = 0
    angle_pivot = 0
    color_ctr = 0
    while angle < 360:
        size = 3
        center = shuriken.rotate_point((2500, 1050), (2500,2500), angle_pivot)

        while size > 0:
            if color_ctr % 3 == 0: color = color_r
            elif color_ctr % 2 == 0: color = color_g
            else: color = (255, 255, 0)
            shuriken.draw_diamond(center, size, angle, color)
            size -= 0.3
            color_ctr += 1

        angle += 60
        angle_pivot += 60

    #draw a diamond and triangles in increasing size at tip of the rotating diamonds
    angle = 30
    angle_pivot = 30
    while angle < 360:
        triangle_size = 600
        center = shuriken.rotate_point((2500, 1050), (2500,2500), angle_pivot)
        shuriken.draw_diamond(center, 4.5, angle, (70, 0, 0))

        while triangle_size > 0:
            shuriken.draw_triangle(center, triangle_size, angle, (255, 255, 0))
            triangle_size -= 100

        angle += 60
        angle_pivot += 60

    # show created shuriken-like mandala and save
    shuriken.show()
    shuriken.save("sp2_output.png")