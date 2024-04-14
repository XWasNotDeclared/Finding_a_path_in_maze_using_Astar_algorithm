import pygame

# Initialize Pygame
pygame.init()

# Constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create a display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Zoom In and Zoom Out with Mouse Scroll")

# Load an image (you can replace 'image.png' with your own image file)
image = pygame.image.load('image.jpg')

# Initial zoom level
zoom_level = 1.0

# Define the running state
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            # Adjust zoom level based on mouse wheel
            if event.y > 0:
                # Mouse wheel scrolled up (zoom in)
                zoom_level += 0.1
            elif event.y < 0:
                # Mouse wheel scrolled down (zoom out)
                zoom_level -= 0.1
                # Ensure zoom level doesn't go below a certain limit
                zoom_level = max(0.1, zoom_level)
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Calculate the new size of the image based on the zoom level
    new_width = int(image.get_width() * zoom_level)
    new_height = int(image.get_height() * zoom_level)
    
    # Resize the image using the scale function
    scaled_image = pygame.transform.scale(image, (new_width, new_height))
    
    # Calculate the position to center the scaled image on the screen
    x = (SCREEN_WIDTH - new_width) // 2
    y = (SCREEN_HEIGHT - new_height) // 2
    
    # Blit the scaled image to the screen at the calculated position
    screen.blit(scaled_image, (x, y))
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
