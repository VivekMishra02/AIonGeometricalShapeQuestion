import cv2

class Circle:
    def drawCircle(self,image, text):
        rad_dia = ["radius", "diameter", "area"]
        center = (225, 200)
        unit = ""
        dimensions = {}
        text_list = text.split()
        units = ["mm", "cm", "km", "miles", "hm", "Hm"]

        for num in text_list:
            if num in units:
                unit = num

        for x in rad_dia:
            if x in text_list:
                ind = text_list.index(x)
                for char in range(ind, len(text_list)):
                    if text_list[char].isdigit():
                        dimensions[x] = text_list[char]
                        break
        print(dimensions)

        cv2.circle(image, center, 100, (0, 0, 255), 3)

        try:
            cv2.putText(image, "r = "+dimensions["radius"] + " " + unit, (center[0]+110 ,center[1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            cv2.putText(image, "Area = " + str(3.14*(int(dimensions["radius"]))**2) + " " + unit, (center[0]- 80, center[1]+130), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
        except:
            pass