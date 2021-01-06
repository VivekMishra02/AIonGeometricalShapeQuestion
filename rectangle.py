import cv2

class Rectangle:
    def drawRectangle(self,image, text):
        types = ["square","rectangle"]
        s_startPoint, s_endPoint = (125, 100), (325, 300)
        r_startPoint, r_endPoint = (100, 100), (400, 250)
        text_list = text.split()

        units = ["mm", "cm", "km", "miles", "hm", "Hm"]
        sides = []

        for num in text_list:
            if num in units:
                unit = num
            if num.isdigit():
                sides.append(int(num))

        sides.sort()

        for x in text_list:
            if x.lower() in types:
                type = x
                break

        if type.lower() == "square":
            cv2.rectangle(image, s_startPoint, s_endPoint, (0,0,255), 3)
            try:
                cv2.putText(image, str(sides[0])+" "+unit, (s_startPoint[0] - 60, (s_startPoint[1]+ s_endPoint[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[0])+" "+unit, (s_endPoint[0] + 5, (s_startPoint[1]+ s_endPoint[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[0]) + " " + unit, ((s_startPoint[0] + s_endPoint[1])//2, s_startPoint[1]-5), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[0]) + " " + unit, ((s_startPoint[0] + s_endPoint[1])//2,s_endPoint[1]+20), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, "Area = "+str(sides[0]*sides[0]) + " square " + unit, ((s_startPoint[0] ), s_endPoint[1] + 80), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                pass

        if type.lower() == "rectangle":
            cv2.rectangle(image, (100,100), (400,250), (0,0,255), 3)
            try:
                cv2.putText(image, str(sides[0])+" "+unit, (r_startPoint[0] - 60, (r_startPoint[1]+ r_endPoint[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[0])+" "+unit, (r_endPoint[0] + 5, (r_startPoint[1]+ r_endPoint[1])//2), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[1]) + " " + unit, ((r_startPoint[0] + r_endPoint[1])//2, r_startPoint[1]-5), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, str(sides[1]) + " " + unit, ((r_startPoint[0] + r_endPoint[1])//2,r_endPoint[1]+20), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
                cv2.putText(image, "Area = "+str(sides[0]*sides[1]) + " square " + unit, ((r_startPoint[0] ), r_endPoint[1] + 80), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255))
            except:
                pass