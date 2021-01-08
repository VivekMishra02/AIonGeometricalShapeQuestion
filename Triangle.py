import cv2

class Triangle:
    def drawTriangle(self,image,text):

        #declaring variables
        flag = 0
        unit = "units"
        type = ""
        dimension = {"height" : "", "base" : ""}
        text_list = text.split()
        units = ["mm","cm","km","miles","hm","Hm"]

        types = ["right", "acute", "obtuse", "equilateral"]
        dim = ["base", "height", "hypotenuse"]
        sides = []

        # Extracting measuring unit i.e. cm, mm, etc and the dimesnsions given
        for num in text_list:
            if num in units:
                unit = num
            if num.isdigit():
                sides.append(int(num))

        sides.sort()

        #Extracting dimesnsions for a righnt angle triangle.
        for x in dim:
            if x in text_list:
                ind = text_list.index(x)
                for char in range(ind, len(text_list)):
                    if text_list[char].isdigit():
                        dimension[x] = text_list[char]
                        break

        #Checking types of triangle i.e. acute, right, etc.
        for x in text_list:
            if x in types:
                type = x
                flag = 1

        # Drawing right triangle with its dimension
        if type.lower() == "right":
            p1 = (100, 200)
            p2 = (100, 50)
            p3 = (300, 200)
            cv2.line(image, p1, p2, (0, 0, 255), 3)
            cv2.line(image, p2, p3, (0, 0, 255), 3)
            cv2.line(image, p1, p3, (0, 0, 255), 3)

            try:
                cv2.putText(image, str(dimension["height"])+" "+unit, (p1[0]-p1[0]//3- 20, (p1[1]+p2[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(dimension["base"])+" "+unit, ((p1[0] + p3[0]) // 2, p1[1]+p1[1]//10), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(dimension["hypotenuse"])+" "+unit, ((p3[0]+p1[0])//2, (p1[1]+p2[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                pass
            try:
                cv2.putText(image, "Area = "+str(self.area(type, dimension, sides)) + " square " + unit,
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                cv2.putText(image, "Some dimensions may be missing",
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

        # Drawing obtuse triangle with its dimension
        elif type.lower() == "obtuse":
            p1 = (100, 200)
            p2 = (50, 50)
            p3 = (450, 200)
            cv2.line(image, p1, p2, (0, 0, 255), 3)
            cv2.line(image, p2, p3, (0, 0, 255), 3)
            cv2.line(image, p1, p3, (0, 0, 255), 3)
            try:
                cv2.putText(image, str(sides[0])+" "+unit, (p1[0] - p1[0] // 2 - 20, (p1[1] + p2[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[1])+" "+unit, ((p1[0] + p3[0]) // 2, (p1[1] + p3[1]) // 2 + 15), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[2])+" "+unit, ((p3[0] + p1[0]) // 2, (p3[1] + p2[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                pass

            try:
                cv2.putText(image, "Area = "+str(self.area(type, dimension, sides)) + " square " + unit,
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                cv2.putText(image, "Some dimensions may be missing",
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

        # Drawing acute triangle with its dimension
        elif type.lower() == "acute":
            p1 = (100, 200)
            p2 = (150, 50)
            p3 = (450, 200)
            cv2.line(image, p1, p2, (0, 0, 255), 3)
            cv2.line(image, p2, p3, (0, 0, 255), 3)
            cv2.line(image, p1, p3, (0, 0, 255), 3)
            try:
                cv2.putText(image, str(sides[0])+" "+unit, (p1[0] + p1[0] // 10 - 30, (p1[1] + p2[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[1])+" "+unit, ((p1[0] + p3[0]) // 2, (p1[1] + p3[1]) // 2 + 15), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[2])+" "+unit, ((p3[0] + p1[0]) // 2 + 25, (p3[1] + p2[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                pass

            try:
                cv2.putText(image, "Area = "+str(self.area(type, dimension, sides)) + " square " + unit,
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                cv2.putText(image, "Some dimensions may be missing",
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

        # Drawing equilateral triangle with its dimension
        elif type.lower() == "equilateral":
            p1 = (100, 200)
            p2 = (200, 50)
            p3 = (300, 200)
            cv2.line(image, p1, p2, (0, 0, 255), 3)
            cv2.line(image, p2, p3, (0, 0, 255), 3)
            cv2.line(image, p1, p3, (0, 0, 255), 3)
            try:
                cv2.putText(image, str(sides[0])+" "+unit, ((p1[0] + p2[0]) // 2- 45, (p1[1] + p2[1]) // 2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[0])+" "+unit, ((p1[0] + p3[0]) // 2, (p1[1] + p3[1]) // 2 + 15), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[0])+" "+unit, ((p3[0] + p2[0]) // 2 + 5, (p3[1] + p2[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                pass

            try:
                cv2.putText(image, "Area = "+str(self.area(type, dimension, sides)) + " square " + unit,
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                cv2.putText(image, "Some dimensions may be missing",
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

        # Drawing scalene triangle with its dimension
        if flag == 0:
            p1 = (100, 200)
            p2 = (50, 70)
            p3 = (400, 100)
            cv2.line(image, p1, p2, (0, 0, 255), 3)
            cv2.line(image, p2, p3, (0, 0, 255), 3)
            cv2.line(image, p1, p3, (0, 0, 255), 3)
            try:
                cv2.putText(image, str(sides[0])+" "+unit, (p1[0]-p1[0]//2 - 20, (p1[1]+p2[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[1])+" "+unit, ((p1[0] + p3[0]) // 2, (p1[1]+p3[1])//2+15), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[2])+" "+unit, ((p3[0]+p1[0])//2, p2[1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

            except:
                pass

            try:
                cv2.putText(image, "Area = "+str(self.area(type, dimension, sides)) + " square " + unit,
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                cv2.putText(image, "Some dimensions may be missing",
                            (p1[0], p1[1] + 50), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))

    #function to calculate the  area
    def area(self,type, dimesnsion, sides):
        if type == "equilateral":
            return round(3**(1/2)/4*(sides[0]**2),3)
        if type == "" and (dimesnsion["height"] != "") and (dimesnsion["base"] != ""):
            return round(1 / 2 * (int(dimesnsion["base"]) * int(dimesnsion["height"])), 3)
        if type == "" and len(sides) >= 3:
            s = (int(sides[0])+int(sides[1])+int(sides[2]))/2
            return round(s*(s-sides[0])*(s-(sides[1]))*(s-sides[2]))**(1/2)
        if type == "right":
            return round(1/2*(int(dimesnsion["base"])*int(dimesnsion["height"])),3)
