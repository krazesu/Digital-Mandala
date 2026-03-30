import PIL.Image, PIL.ImageDraw
from math import sin, cos, pi

class Mandala:
    #initialize instance attributes
    def __init__(self, size, bgcolor):
        self.size = size
        self.bgcolor = bgcolor
        self.canvas = PIL.Image.new("RGB", self.size, self.bgcolor)
        self.draw = PIL.ImageDraw.Draw(self.canvas)
    
    #Image.show function
    def show(self):
        self.canvas.show()

    #Image.save function
    def save(self ,filename):
        self.canvas.save(filename)

    #rotate a point
    def rotate_point(self, point, pivot, angle):
        x_1 = point[0]
        y_1 = point[1]

        x_2 = pivot[0]
        y_2 = pivot[1]

        #convert angle from degrees to radians
        radians = angle * (pi/180)
        
        #temporarily translate point and pivot so pivot is at origin
        temp_x_1 = x_1 + (0-x_2)
        temp_y_1 = y_1 + (0-y_2)

        #rotate point about the origin
        x_new = temp_x_1 * cos(radians) - temp_y_1 * sin(radians)
        y_new = temp_x_1 * sin(radians) + temp_y_1 * cos(radians)

        #retranslate rotated point anf pivot so pivot is at original place
        x_new = x_new - (0-x_2)
        y_new = y_new - (0-y_2)

        return (x_new, y_new)

    def draw_triangle(self, center, side_length, rotation, color):
        #define vertices of the triangle
        vertex_1 = (center[0], center[1] - ((side_length/2) / sin(60*pi/180)))
        vertex_2 = (center[0] + side_length/2, center[1] + ((side_length/2) / (sin(60*pi/180)/cos(60*pi/180))))
        vertex_3 = (center[0] - side_length/2, center[1] + ((side_length/2) / (sin(60*pi/180)/cos(60*pi/180))))

        #rotate every vertex to rotate the whole triangle
        vertex_1 = self.rotate_point(vertex_1, center, rotation)
        vertex_2 = self.rotate_point(vertex_2, center, rotation)
        vertex_3 = self.rotate_point(vertex_3, center, rotation)
        
        #draw the triangle by connecting the vertices
        self.draw.line([vertex_1, vertex_2], fill=color, width=10)
        self.draw.line([vertex_2, vertex_3], fill=color, width=10)
        self.draw.line([vertex_3, vertex_1], fill=color, width=10)

    def draw_diamond(self, pivot, size, rotation, color):
        #define vertices of the diamond
        vertex_1 = (pivot[0], pivot[1] - size*200)
        vertex_2 = (pivot[0] + size*75, pivot[1] - size*50)
        vertex_3 = (pivot[0], pivot[1])
        vertex_4 = (pivot[0] - size*75, pivot[1] - size*50)

        #rotate every vertex to rotate the whole diamond
        vertex_1 = self.rotate_point(vertex_1, pivot, rotation)
        vertex_2 = self.rotate_point(vertex_2, pivot, rotation)
        vertex_3 = self.rotate_point(vertex_3, pivot, rotation)
        vertex_4 = self.rotate_point(vertex_4, pivot, rotation)

        #draw the diamond by connecting the vertices
        self.draw.line([vertex_1, vertex_2], fill=color, width=10)
        self.draw.line([vertex_2, vertex_3], fill=color, width=10)
        self.draw.line([vertex_3, vertex_4], fill=color, width=10)
        self.draw.line([vertex_4, vertex_1], fill=color, width=10)