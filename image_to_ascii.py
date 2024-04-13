from PIL import Image

def image_to_ASCII(image_path:str, char_map="@@@@@@@@@@@@%%%%%%%%#########********+++++++++====", save:bool=False, invert:bool=False, intermediate:str="") -> str:
  """
  Converts an image to ASCII art using a character map.

  Args:
      image_path: Path to the image file.
      char_map: A string containing characters representing different light levels.
      save: to save or not to save to a text file default = False
      invert: will invert the charmap default = False
      intermediate: which character(s) should be between each character from the charmap default = ""

  Returns:
      A string containing the ASCII art representation of the image.
  """
  img = Image.open(image_path).convert('L')  # Convert to grayscale

  width, height = img.size
  new_width = 500  # too low means image is unrecognizable
  aspect_ratio = height / width
  new_height = int(aspect_ratio * new_width)
  img = img.resize((new_width, new_height))

  # Define a list of ASCII characters based on brightness levels
  ascii_chars = list(char_map)

  # Get pixel data
  pixels = img.getdata()

  ascii_image = []
  for pixel in pixels:
    index = int(pixel * len(ascii_chars) / 256)
    if invert:
        index = -index
    ascii_image.append(ascii_chars[index])

 
  final_image = "\n".join([f"{intermediate}".join(row) for row in zip(*[iter(ascii_image)] * new_width)]) # having the l between each character makes the width more natural
  if save:
    with open("ascii_art.txt", "w", encoding="utf-8") as f:
        f.write(final_image)
    
  return final_image



  
  
if __name__ == "__main__":
    
    ascii_art = image_to_ASCII("images/image.jpg", save=True)