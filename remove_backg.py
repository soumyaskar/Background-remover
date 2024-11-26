from rembg import remove
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

input_path = 'Your_picture'.jpg'
output_path = 'output.png'

input_image = Image.open(input_path)

output_image = remove(input_image)
output_image.save(output_path)
