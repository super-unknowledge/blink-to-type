# blink_detect.py
from pathlib import Path
import cv2
import dlib
import imutils
from scipy.spatial import distance as dist
from imutils import face_utils

from typer import typingPrint


f = open(Path('assets/copypasta.txt'))

# Calculate EyeAspect Ratio
def calculate_EAR(eye):

	# vertical distances
	y1 = dist.euclidean(eye[1], eye[5])
	y2 = dist.euclidean(eye[2], eye[4])

	# horizontal distance
	x1 = dist.euclidean(eye[0], eye[3])

	# calculate the EAR
	ear = (y1+y2) / x1
	return ear


# Constants
BLINK_THRESH = 0.45
SUCC_FRAME = 1
count_frame = 0

# Eye landmarks
(L_start, L_end) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(R_start, R_end) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

# Initialize the models for landmark and face detection
detector = dlib.get_frontal_face_detector()
landmark_predict = dlib.shape_predictor(
	'Models/shape_predictor_68_face_landmarks.dat'
)

# Capture webcam video
cam = cv2.VideoCapture(0) 
while True: 
	_, frame = cam.read() 
	# can we set size with cam.read() instead of resizing
	frame = imutils.resize(frame, width=640)

	# Convert frame to gray scale
	# and pass to detector
	img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect face
	faces = detector(img_gray)
	for face in faces:
		# detect landmarks
		shape = landmark_predict(img_gray, face)

		# convert shape class to (x,y) coords
		shape = face_utils.shape_to_np(shape)

		# extract left and right eye landmarks
		lefteye = shape[L_start: L_end]
		righteye = shape[R_start: R_end]

		# calculate EAR
		left_EAR = calculate_EAR(lefteye)
		right_EAR = calculate_EAR(righteye)

		# get average of left and right eye EAR
		avg = (left_EAR+right_EAR)/2
		if avg < BLINK_THRESH:
			count_frame += 1  # increment frame count
		else:
			if count_frame >= SUCC_FRAME:
				# Perform logic when blink is detected
				typingPrint(f.read(5))
				# must set flush=True to avoid problems with
				# buffering, but might not be necessary when
				# typer function is used for animation
#				cv2.putText(
#					frame, 'Blink Detected', (30, 30),
#					cv2.FONT_HERSHEY_DUPLEX, 1,
#					(0, 200, 0), 1
#				)
				# must reset to zero or else it 
				# will fire nonstop
				count_frame = 0 
			else:
				count_frame = 0

	cv2.imshow('Camera Feed', frame) 
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

f.close()
cam.release() 
cv2.destroyAllWindows()
