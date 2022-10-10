from turtle import window_height
import cv2
import cv2.aruco as aruco

device = 0  # Front camera

cap = cv2.VideoCapture(device)
while cap.isOpened():

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is not empty
    if not ret:
        continue

    # # Convert from BGR to RGB
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    frame = aruco.drawDetectedMarkers(frame, corners)
    if corners != (): 
        for i in range(0, len(corners), 2):
            array_or_corners = corners[i]
            x1, y1 = array_or_corners[0][0][0], array_or_corners[0][0][1]
            x2, y2 = array_or_corners[0][1][0], array_or_corners[0][1][1]
            x3, y3 = array_or_corners[0][2][0], array_or_corners[0][2][1]
            x4, y4 = array_or_corners[0][3][0], array_or_corners[0][3][1]
            xc, yc = (x1 + x2) / 2, (y1 + y2) / 2
            xc2, yc2 = (x3 + x4) / 2, (y3 + y4) / 2
            cv2.circle(frame, (int((xc + xc2) / 2), int((yc + yc2) / 2)), 10, (255, 255, 0))
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    height, width, channels = frame.shape
    
    if cv2.waitKey(30) & 0xFF == ord('q'): # press q to exit
        break