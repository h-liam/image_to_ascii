import cv2

def brightness_to_ascii(brightness):
  """
  Maps brightness value to an ASCII character representing light level.

  Args:
      brightness: Integer representing pixel brightness (0-255).

  Returns:
      A single character representing the light level.
  """
  char_map = "@@@@@@@@@@@@%%%%%%%%#########********+++++++++====" 
  index = int(brightness * len(char_map) / 256)
  return char_map[-index]

def webcam_to_ascii():

  cap = cv2.VideoCapture(0)

  while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # (256)

    resized_frame = cv2.resize(gray, (100, 100))  #smaller fits better in terminal. Larger = more resolution obviously

    ascii_frame = []
    for row in resized_frame:
      ascii_row = [brightness_to_ascii(pixel) for pixel in row]
      ascii_frame.append(ascii_row)

    for row in ascii_frame:
      print("".join(row))

    print("\033c", end="")  # This clears the terminal screen

    if cv2.waitKey(1) == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  webcam_to_ascii()