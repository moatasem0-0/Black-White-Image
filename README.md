# Image Conversion Steps

This README describes the steps followed to convert a colored image to black and white using thresholding.

## Steps

1. **Load the Original Image**
   - The original colored image was loaded into the program.

2. **Convert to Black and White**
   - The image was converted to black and white using a thresholding technique.
   - A threshold value of **128** was applied:
     - Any pixel intensity above 128 was set to **white**.
     - Any pixel intensity below 128 was set to **black**.

3. **Calculate Pixel Count**
   - The total number of pixels in the image was calculated before and after conversion.

4. **Save the Resulting Image**
   - The black and white image was saved as **`image_bw.png`**.

## Output

- **Original Image**: Colored image loaded into the program.
- **Black and White Image**: Saved as `image_bw.png`.
