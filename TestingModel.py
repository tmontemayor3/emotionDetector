import tensorflow as tf
import cv2
import numpy as np
model = tf.keras.models.load_model('EmotionModel.h5')

cam = cv2.VideoCapture(0)
cam.set(3, 100)
cam.set(4, 100)

while True:
  _, frame = cam.read(0)
  cv2.imshow('say cheese', frame)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame = cv2.resize(frame, dsize=(100, 100))
  frame = np.reshape(frame, (1, 100, 100, 1))

  prediction = model.predict(frame)
  num = np.argmax(prediction)
  if num == 0:
    print('happy')
  elif num == 1:
    print('mad')
  elif num == 2:
    print('serious')
  else:
    print('ERROR')


  if cv2.waitKey(20) == ord('q'):
    # press q to break
    break
  
