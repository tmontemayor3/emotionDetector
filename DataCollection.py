import cv2

cam = cv2.VideoCapture(0)

cam.set(3, 100)
cam.set(4, 100)

number_of_images = 150
current_images = 0
while current_images < number_of_images:
  _, frame = cam.read(0)
  cv2.imshow('say cheese', frame)
  cv2.imwrite(f'SeriousImages/IMG_{current_images}.png', frame)

  if cv2.waitKey(20) == ord('q'):
    # press q to break
    break

  current_images += 1
