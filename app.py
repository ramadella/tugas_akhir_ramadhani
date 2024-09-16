from flask import Flask, render_template, Response, jsonify, request
import cv2
import mysql.connector
import time
from datetime import datetime

app = Flask(__name__)

faceDetect = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(1)
recognizer = cv2.face.LBPHFaceRecognizer.create()
recognizer.read(r"data_yml/trainingData.yml")
profiles = {
    0: {"name": "Ramadhani", "nim": "2010951036", "gender": "Male"},
    1: {"name": "Arif", "nim": "2010952053", "gender": "Male"},
    2: {"name": "Ridho", "nim": "2110951006", "gender": "Male"},
    3: {"name": "Rahdian", "nim": "2010951001", "gender": "Male"},
    4: {"name": "Taufik", "nim": "2010952009", "gender": "Male"},
    5: {"name": "Sukry", "nim": "2010951045", "gender": "Male"},
    # Add more profiles as needed
}

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="face_recognition_db"
)
mycursor = mydb.cursor()
# Variables to control time delay
last_insert_time = time.time()
insert_delay = 20  # Time delay in seconds
def gen_frames():
    global last_insert_time
    while True:
        success, frame = video.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceDetect.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Predict ID and confidence
                id, conf = recognizer.predict(gray[y:y+h, x:x+w])                
                # Print debug information
                print(f"Detected ID: {id} with confidence: {conf}")                
                # Fetch the profile
                profile = profiles.get(id, {"name": "Unknown", "nim": "Unknown", "gender": "Unknown"})               
                # Only display the name if confidence is below a certain threshold
                if conf < 70:
                    cv2.putText(frame, f"{profile['name']}", (x, y + h + 30), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
                    cv2.putText(frame, f"{profile['nim']}", (x, y + h + 60), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
                    cv2.putText(frame, f"{profile['gender']}", (x, y + h + 90), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), 2)
                    # Insert data into database if the profile is known and enough time has passed
                    current_time = datetime.now()
                    if time.time() - last_insert_time >= insert_delay and profile['name'] != "Unknown":
                        sql = "INSERT INTO face_scan_results (name, nim, gender, scan_time) VALUES (%s, %s, %s, %s)"
                        val = (profile['name'], profile['nim'], profile['gender'], current_time)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        last_insert_time = time.time()
                else:
                    print(f"Unknown face with confidence: {conf}")
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/script')
def script():
    return render_template('script.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/get_records')
def get_records():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        offset = (page - 1) * limit
        mycursor.execute("SELECT name, nim, gender, DATE_FORMAT(scan_time, '%W %H:%i') as scan_time FROM face_scan_results ORDER BY scan_time DESC LIMIT %s OFFSET %s", (limit, offset))
        records = mycursor.fetchall()
        # Check if there are more records available
        mycursor.execute("SELECT COUNT(*) FROM face_scan_results")
        total_records = mycursor.fetchone()[0]
        has_more_records = (page * limit) < total_records
        return jsonify({
            "records": records,
            "hasMoreRecords": has_more_records
        })
    except Exception as e:
        print("Error fetching records:", e)  # Debug print
        return jsonify({"error": str(e)})
if __name__ == "__main__":
    app.run(debug=True)