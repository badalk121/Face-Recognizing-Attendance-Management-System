# Face Recognizing Attendance Management System (F.R.A.M.S)

## Description
F.R.A.M.S is an AI-powered attendance management system that automates attendance tracking using face recognition. Built with Python, OpenCV, and Tkinter, it efficiently captures, trains, and recognizes faces to mark attendance in real time. This system reduces manual errors, saves time, and enhances security in educational and professional settings.

## Features
- Face capture and dataset generation
- Model training for face recognition
- Real-time attendance tracking
- Simple GUI with Tkinter
- CSV-based attendance storage

## Prerequisites
Ensure you have the following installed:
- Python 3.12.1+
- OpenCV
- NumPy
- Pandas
- Tkinter

## Installation
Clone the repository:
```bash
git clone https://github.com/badalk121/Face-Recognizing-Attendance-Management-System.git
cd Face-Recognizing-Attendance-Management-System
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. **Run the application**:
   ```bash
   python app.py
   ```
2. **Capture face images**:
   - Enter the user ID and name.
   - Capture 100 images using the webcam.
3. **Train the model**:
   - Click on the "Train Model" button to train the face recognizer.
4. **Recognize & mark attendance**:
   - Start the recognition process.
   - Recognized faces will be marked in the attendance CSV.

## File Structure
- `app.py`: Main application file
- `dataset/`: Stores captured images
- `trainer/`: Contains trained models
- `attendance.csv`: Stores recorded attendance
- `requirements.txt`: Lists dependencies

## Potential Use Cases
- Schools & universities for automated student attendance
- Offices & organizations for employee tracking
- Secure access control at events and restricted areas

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository, make changes, and submit a pull request.

## Contact
For queries or contributions, contact me at badal.k.1908@gmail.com
