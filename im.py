from PIL import Image

def get_image_size(image_path):
    """
    Returns the width and height of the image at the specified path.
    
    :param image_path: Path to the image file
    :return: A tuple (width, height) representing the dimensions of the image
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Replace 'example.jpg' with the path to your JPG file
    image_path = "example.jpg"
    dimensions = get_image_size("Senate1.jpg")

    if dimensions:
        print(f"Image Size: {dimensions[0]}x{dimensions[1]} pixels")
    else:
        print("Failed to retrieve image size.")
