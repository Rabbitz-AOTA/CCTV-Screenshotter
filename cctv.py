import requests
import os
from PIL import Image, ImageDraw, ImageFont

# Set the URL of the CCTV camera
cctv_url = "http://192.168.1.100/video.mjpg"

# Set the folder to save the screenshots
save_folder = "screenshots"

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Set the ASCII banner text
ascii_banner = "ANONYMOUS"

while True:
    # Get the latest screenshot from the CCTV camera
    response = requests.get(cctv_url, stream=True)
    
    # Save the screenshot to a temporary file
    temp_file = "temp.jpg"
    with open(temp_file, "wb") as f:
        f.write(response.content)
    
    # Open the screenshot image
    img = Image.open(temp_file)
    
    # Create a new image with the same size as the original
    new_img = Image.new("RGB", img.size, color="white")
    
    # Draw the ASCII banner on the new image
    draw = ImageDraw.Draw(new_img)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((10, 10), ascii_banner, font=font, fill="black")
    
    # Paste the original image onto the new image
    new_img.paste(img, (0, 50))
    
    # Save the new image with the ASCII banner to a file
    filename = os.path.join(save_folder, f"screenshot_{int(time.time())}.jpg")
    new_img.save(filename)
    
    # Close the images
    img.close()
    new_img.close()
    
    # Remove the temporary file
    os.remove(temp_file)
    
    # Wait for a short interval before taking the next screenshot
    time.sleep(5)
