import numpy as np
from PIL import Image

image_path = "pic.jpg"
output_path = "picgray.jpg"
orginal_image = Image.open(image_path)
image_data = np.asarray(orginal_image)

red_channel = image_data[: , : , 0]
print(f"image shape :{red_channel},mean:{red_channel.mean()},min{red_channel.min()}")

# فرمول y=0.2126R + 0.7152G + 0.0722B

weights = [0.2126 , 0.7152 , 0.0722]

image_data_float = image_data.astype(np.float32)
grayscale_image_data = np.dot(image_data_float, weights)

# Normalize to the range [0, 255] and convert to uint8
grayscale_image_data = np.clip(grayscale_image_data, 0, 255).astype(np.uint8)

# grayscale_image_data = image_data @ weights

grayscale_image = Image.fromarray(grayscale_image_data)
grayscale_image.save(output_path)