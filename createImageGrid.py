#Library
from PIL import Image


# Function to create a grid of images with customizable dimensions and size.
"""Parameters:
        - image_paths (list of str): List of file paths to the images to be included in the grid.
        - grid_cols_rows (tuple): A tuple (rows, cols) defining the number of rows and columns in the grid.
        - image_size (tuple): A tuple (width, height) specifying the size to which each image will be resized.
        - output_path (str): File path to save the final grid image. """

def create_image_grid(image_paths, grid_cols_rows, image_size, output_path):
    rows, cols = grid_cols_rows
    grid_width = cols * image_size[0]
    grid_height = rows * image_size[1]


    # Create a blank white image
    grid = Image.new('RGB', size=(grid_width, grid_height), color="white")

    #Loop through each image and place it in the appropriate position in the grid
    for idx, img_path in enumerate(image_paths):
        row_image = idx // cols
        col_image = idx % rows

        img = Image.open(img_path)
        img = img.resize(image_size)

        # Calculate the top-left corner where the image will be placed
        x = col_image * image_size[0]
        y = row_image  * image_size[1]

        grid.paste(img, (x, y))

    grid.save(output_path)


# Example usage
image_files = [
    "image_1.png", "image_2.png", "image_3.png",
    "image_4.png", "image_5.png", "image_6.png",
    "image_7.png", "image_8.png", "image_9.png"
]

# Call to the function
create_image_grid(image_files, grid_cols_rows=(3, 3), image_size=(80, 80), output_path="grid_result.png")