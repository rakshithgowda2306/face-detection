import cv2

def detect_faces(image_path):
    # Load the Haarcascade face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the input image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save the output image
    output_path = 'output.jpg'
    cv2.imwrite(output_path, image)

    return output_path

if __name__ == "__main__":
    image_path = 'input.jpg'  # Replace with the path to your input image
    output_path = detect_faces(image_path)
    print(f"Output saved to {output_path}")