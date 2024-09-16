import numpy as np
import cv2
import os
import face_recognition as fr
# Load and process the image
test_img = cv2.imread(r'dataset\0\image0016.jpg')  # Provide path to the image you want to test
test_img = cv2.imread(r'dataset\1\image0015.jpg')  # Provide path to the image you want to test
test_img = cv2.imread(r'dataset\2\image0034.jpg')  # Provide path to the image you want to test
test_img = cv2.imread(r'dataset\3\image0012.jpg')  # Provide path to the image you want to test
test_img = cv2.imread(r'dataset\4\image0037.jpg')  # Provide path to the image you want to test
test_img = cv2.imread(r'dataset\1\image0294.jpg')  # Provide path to the image you want to test
if test_img is None:
    raise ValueError("Image not loaded correctly")
# Perform face detection
faces_detected, gray_img = fr.faceDetection(test_img)
print("Faces Detected: ", faces_detected)
# Train the classifier
faces, faceID = fr.labels_for_training_data(r'dataset')  # Provide the path to the training images
face_recognizer = fr.train_classifier(faces, faceID)
face_recognizer.save(r'data_yml\trainingData.yml')  # Save the trained model
# Define profiles for each label
profiles = {
    0: {"name": "Ramadhani", "nim": "2010951036", "gender": "Male"},
    1: {"name": "Arif", "nim": "2010952053", "gender": "Male"},
    2: {"name": "Ridho", "nim": "2110951006", "gender": "Male"},
    3: {"name": "Rahdian", "nim": "2010951001", "gender": "Male"},
    4: {"name": "Taufik", "nim": "2010952009", "gender": "Male"},
    5: {"name": "Sukry", "nim": "2010951045", "gender": "Male"},
}
# Process detected faces
for face in faces_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(roi_gray)
    print("Confidence:", confidence)
    print("Label:", label)

    fr.draw_rect(test_img, face)  # Draw rectangle on color image
    person = profiles.get(label, {"name": "Unknown", "nim": "Unknown", "gender": "Unknown"})
    predicted_name = person['name']
    predicted_nim = person['nim']
    predicted_gender = person['gender']
    # Draw text on the color image
    fr.put_text((test_img, f"Name: {predicted_name}", x, y + h + 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
    fr.put_text((test_img, f"NIM: {predicted_nim}", x, y + h + 60), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
    fr.put_text((test_img, f"Gender: {predicted_gender}", x, y + h + 90), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
# Resize image for display
resized_img = cv2.resize(test_img, (1000, 700))
# Display the image
cv2.imshow("Face Detection", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()