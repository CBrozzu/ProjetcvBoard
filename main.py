import cv2

piano_cascade = cv2.CascadeClassifier('myhaar.xml')

cap = cv2.VideoCapture("AKAI MPK MINI MK2 TUTO N°1.mp4")

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pianos = piano_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in pianos:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    cv2.imshow('img', img)

    if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()