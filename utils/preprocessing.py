from PIL import Image, ImageFilter
import numpy as np
from skimage import exposure, filters

def preprocess_image(img, target_size=(224, 224)):
    # Convert to PIL Image if needed
    if not isinstance(img, Image.Image):
        img = Image.fromarray(img)
    # Resize
    img = img.resize(target_size)
    # Convert to grayscale
    img = img.convert("L")
    # Convert to numpy array
    img_np = np.array(img)
    # Histogram equalization
    img_np = exposure.equalize_hist(img_np)
    # Median blur (skimage)
    img_np = filters.median(img_np)
    # Sharpening (Pillow filter)
    img_sharp = Image.fromarray((img_np * 255).astype(np.uint8))
    img_sharp = img_sharp.filter(ImageFilter.SHARPEN)
    # Convert back to numpy
    img_np = np.array(img_sharp).astype("float32")
    # Normalize
    img_np = img_np / 255.0
    return img_np