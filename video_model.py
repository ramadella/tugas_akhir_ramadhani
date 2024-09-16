import cv2
import numpy as np

# Initialize face detector and video capture
faceDetect = cv2.CascadeClassifier('classifier\haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(1)

# Load the recognizer and the trained model
recognizer = cv2.face.LBPHFaceRecognizer.create()
recognizer.read(r"data_yml\trainingData.yml")

# Directly storing the profiles within the program
profiles = {
    0: {"name": "Ramadhani", "nim": "2010951036", "gender": "Male"},
    1: {"name": "Septi Rahma Della", "nim": "2010432033", "gender": "Female"},
    # Add more profiles as needed
}

while True:
    # Capture frame-by-frame
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Predict the ID and confidence of the face
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])
        
        # Retrieve the profile directly from the program
        profile = profiles.get(id, {"name": "Unknown", "nim": "Unknown", "gender": "Unknown"})
        
        # Display the profile information if available
        cv2.putText(frame, f"{profile['name']}", (x, y + h + 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0),2)
        cv2.putText(frame, f"{profile['nim']}", (x, y + h + 60), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
        cv2.putText(frame, f"{profile['gender']}", (x, y + h + 90), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)

    # Display the resulting frame
    cv2.imshow("Wajah", frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close windows
video.release()
cv2.destroyAllWindows()
