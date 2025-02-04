---

# Mygip Image Processing Application

This project is an image processing application written in Python. It demonstrates a variety of image manipulation techniques using libraries such as **NumPy**, **Matplotlib**, **Pillow (PIL)**, and **Tkinter** for a graphical user interface (GUI). The application is structured into several parts, each focusing on different image operations.

## Features

- **Basic Image Operations**  
  - **Reading an Image:** Load images from file using Matplotlib.  
  - **Displaying an Image:** Show images without axes using Matplotlib.  
  - **Saving an Image:** Save processed images to a file.

- **Black & White Image Creation and Manipulation**  
  - Create a completely black image.  
  - Create a completely white image.  
  - Generate a chessboard (alternating black & white) pattern image.  
  - Generate the negative of an image.

- **Image Analysis**  
  - Calculate the **luminance** (average brightness) of an image.  
  - Compute the **contrast** (variance of pixel intensities) of an image.  
  - Determine the **maximum intensity (profondeur)** within an image.

- **Image Transformation**  
  - **Inversion:** Invert pixel values (255 - pixel value).  
  - **Flipping:** Perform horizontal and vertical flips.  
  - **Concatenation:** Stack images vertically or horizontally (requires same dimensions).

- **Color Image Manipulation**  
  - Generate a random RGB image.  
  - Convert an RGB image to grayscale using two different methods:
    - A faster NumPy-based approach.
    - A more traditional loop-based method.
  - Additional symmetry operations (flip up/down, left/right).

- **Graphical User Interface (GUI)**  
  - Built using Tkinter, the GUI provides interactive buttons to perform the above operations.  
  - Users can load an image, create new images (black, white, chessboard, RGB), and apply transformations such as flipping, inversion, and grayscale conversion.  
  - Options to display and save the manipulated image are also available.  
  - The interface also calculates image properties like luminance, contrast, and maximum intensity.

## Requirements

- **Python 3.x**
- **NumPy**
- **Matplotlib**
- **Pillow (PIL)**
- **Tkinter** (usually included with Python)

You can install the required libraries (if not already installed) using pip:

```bash
pip install numpy matplotlib pillow
```

## Installation and Usage

1. **Download the Source Code**  
   Save the file `Mygip_Pyhton_Source_Code.py` to your local machine.

2. **Run the Application**  
   Open a terminal or command prompt in the directory containing the source file and run:
   ```bash
   python Mygip_Pyhton_Source_Code.py
   ```
   This will launch the GUI.

3. **Using the GUI**  
   - **Loading an Image:** Click on **"Charger Image"** to open an image file.  
   - **Creating Images:**  
     - Use **"Creer Image Noir"** for a black image,  
     - **"Creer Image Blanc"** for a white image,  
     - **"Creer Imange Blanc et Noir"** for a chessboard-like image, or  
     - **"Creer Image RGB"** for a randomly generated RGB image.
   - **Image Transformations:**  
     - Apply horizontal/vertical flips, inversion, and grayscale conversion via the respective buttons.
   - **Image Analysis:**  
     - Calculate luminance, contrast, and maximum intensity using the provided buttons.
   - **Displaying and Saving:**  
     - **"Afficher Image"** shows the current image.  
     - **"Enregistrer L'Image"** saves the current image as `image1.png`.

## Code Structure

- **Part 1 & 2: Basic Image I/O**  
  Functions to read, display, and save images using Matplotlib and NumPy.

- **Part 3: Black & White Image Manipulations**  
  Functions to create black, white, and chessboard images as well as generate the negative of an image.

- **Part 4: Image Transformations**  
  Functions for image inversion, horizontal/vertical flipping, and concatenating images horizontally or vertically.

- **Part 5: Color Image Manipulations and Conversions**  
  Functions to generate a random RGB image, convert RGB images to grayscale (using both efficient and loop-based approaches), and perform symmetry operations.

- **Graphical User Interface (GUI)**  
  The `ImageApp` class creates an interactive GUI using Tkinter. Buttons are provided to perform the image operations described above. The footer credits the developers: *Daibbar, El Gueroua, Chigr, El Kouably, Bardoud*.

## Additional Notes

- **Performance Considerations:**  
  Some functions have two versions: an optimized NumPy version and a classic loop-based version for educational purposes. The optimized versions are used for better performance.
  
- **Educational Purpose:**  
  The project highlights the simplicity and power of Python in handling image processing tasks compared to traditional languages like C, especially when combined with a user-friendly GUI.

