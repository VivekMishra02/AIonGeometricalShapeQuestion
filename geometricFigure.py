import numpy as np
import cv2
import re

from GeometryFigure.Triangle import Triangle
from GeometryFigure.circle import Circle
from GeometryFigure.rectangle import Rectangle

# Drawing Shapes

def ParseText(text):
    #removing punctuation and wild charecter except space
    for word in text.split("\n"):
        text = " ".join(re.findall(r"[a-zA-Z0-9]+", word))
    shapes = ["circle", "line", "ellipse", "rectangle", "square", "triangle"]
    text_list = text.split()
    for shape in shapes:
        if shape in text_list:
            filterShape = shape
            ImageProcessing(filterShape, text)


def ImageProcessing(figure, text):
    image = np.zeros((512, 512, 3), np.uint8)

    if figure == "Shape not found":
        cv2.putText(image, "No shape detected!", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

    if figure.lower() == "line":
        cv2.line(image, (20, 200), (200, 20), (0, 0, 255), 3)

    if figure.lower() == "rectangle" or figure.lower() == "square":
        s = Rectangle()
        s.drawRectangle(image, text)

    if figure.lower() == "circle":
        c = Circle()
        c.drawCircle(image, text)

    if figure.lower() == "triangle":
        t = Triangle()
        t.drawTriangle(image, text)

    if figure.lower() == "ellipse":
        cv2.ellipse(image, (200, 50), (100, 30), 15, 0, 360, (0, 0, 255), 2)

    cv2.imshow('Black Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


sentence = "A triangle with height 30 and base 40 cm. find it's area?"

ParseText(sentence)
