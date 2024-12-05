import cv2

def preprocess_image(image_path):
    """
    Praproses gambar: konversi ke grayscale dan thresholding.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    processed_image_path = "processed_image.jpg"
    cv2.imwrite(processed_image_path, thresh)
    return processed_image_path
