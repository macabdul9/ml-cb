import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# reading video stream
# acquire the camera object
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

face_data = []
cnt = 0


user_name = input("enter you name :")

while True:
	ret, frame = cam.read()

	if ret == False:
		print("Something went wrong ")
		continue

	key_pressed = cv2.waitKey(1)&0xFF # bitmasking to get last 8-bits

	if key_pressed == ord('q'):
		break


	faces = face_cascade.detectMultiScale(frame, 1.5, 5)

	if(len(faces) == 0):
		continue

	for face in faces:
		x, y, w, h = face


		face_section = frame[y - 10:y + h + 10, x - 10:x + w + 10]

		face_section = cv2.resize(face_section, (100, 100))

		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

		if cnt%10 == 0:
			print("taking picture ", int(cnt/10))
			face_data.append(face_section)
		cnt += 1




	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	#new_img = np.zeros(*gray.shape, 3) # *tuple brackets hata deta hai

	cv2.imshow("Video", frame)
	# cv2.imshow("Video", gray)
	cv2.imshow("face_frame", face_section)



print("total faces", len(face_data))
face_data = np.array(face_data)
face_data = face_data.reshape(face_data.shape[0], -1)

np.save("facedata/" + user_name + ".npy", face_data)

print("Saved at Facedata/" + user_name + ".npy")

print(face_data.shape)


# release the camera object
cam.release()
cv2.destroyAllWindows()
