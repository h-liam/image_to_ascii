import cv2

def brightness_to_ascii(brightness):
  """
  Maps brightness value to an ASCII character representing light level.

  Args:
      brightness: Integer representing pixel brightness (0-255).

  Returns:
      A single character representing the light level.
  """
  char_map = "@@@@@@@@@@@@%%%%%%%%#########********+++++++++===="  # You can adjust the character map for different effects
  index = int(brightness * len(char_map) / 256)
  return char_map[-index]

def webcam_to_ascii():
  """
  Captures live webcam feed and converts it to ASCII art.
  """
  # Initialize video capture object
  cap = cv2.VideoCapture(0)

  while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # (256)

    # Resize frame (optional) for better performance
    resized_frame = cv2.resize(gray, (100, 100))  # Adjust width and height as desired

    # Get ASCII representation for each pixel
    ascii_frame = []
    for row in resized_frame:
      ascii_row = [brightness_to_ascii(pixel) for pixel in row]
      ascii_frame.append(ascii_row)

    # Print the ASCII art to console
    for row in ascii_frame:
      print("".join(row))

    # Clear the console (optional)
    print("\033c", end="")  # This clears the terminal screen on some systems

    # Exit on 'q' press
    if cv2.waitKey(1) == ord('q'):
      break

  # Release capture object
  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  webcam_to_ascii()