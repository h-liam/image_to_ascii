from PIL import Image

def image_to_ASCII(image_path, char_map="@@@@@@@@@@@@%%%%%%%%#########********+++++++++===="):
  """
  Converts an image to ASCII art using a character map.

  Args:
      image_path: Path to the image file.
      char_map: A string containing characters representing different light levels.

  Returns:
      A string containing the ASCII art representation of the image.
  """
  # Open the image with Pillow
  img = Image.open(image_path).convert('L')  # Convert to grayscale

  # Resize the image (optional)
  width, height = img.size
  new_width = 500  # Adjust width as desired
  aspect_ratio = height / width
  new_height = int(aspect_ratio * new_width)
  img = img.resize((new_width, new_height))

  # Define a list of ASCII characters based on brightness levels
  ascii_chars = list(char_map)

  # Get pixel data
  pixels = img.getdata()

    
  invert = False # change to true to invert the image
  
  # Create a list to store ASCII characters for each pixel
  ascii_image = []
  for pixel in pixels:
    # Map pixel brightness to a character in the char_map
    index = int(pixel * len(ascii_chars) / 256)
    if invert:
        index = -index
    ascii_image.append(ascii_chars[index])

  # Split the ASCII characters into lines based on image width
  final_image = "\n".join(["l".join(row) for row in zip(*[iter(ascii_image)] * new_width)])

  return final_image



  
  
if __name__ == "__main__":
    
    ascii_art = image_to_ASCII("kevin.jpg")
    
    # You can also save it to a text file
    with open("ascii_art.txt", "w", encoding="utf-8") as f:
        f.write(ascii_art)