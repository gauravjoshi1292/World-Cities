from cs1lib import *
from sort_cities import *


# The lower left corner of the window has a pixel value (0, 0) and the upper right corner has a pixel value (740, 380)
# The lower left corner of the map has a pixel value (10, 10) and the upper right corner has a pixel value (730, 370)
# I have added a padding of 10px either side for the map inside the window


WINDOW_WIDTH = 740  # Width of the graphics window in pixels
WINDOW_HEIGHT = 380  # Height of the graphics window in pixels
MAP_WIDTH = 720.0  # Map width in pixels
MAP_HEIGHT = 360.0  # Map height in pixels

# Factors used to translate longitude and latitude values to pixel values
# For e.g. a point with longitude -180 and latitude -90 translates to a pixel value (0, 0)
# Similarly (0, 0) translates to (360, 180)
COEFF_X = 2.0
COEFF_Y = 2.0
OFFSET_X = 360.0 + 10
OFFSET_Y = 180.0 + 10


def draw_map():
    """
    Draws the map on the graphics window and plots the
    :return: None
    """
    img = load_image("world.png")  # Load the image

    cities = get_cities_sorted_by_population()[:50]
    print cities

    enable_smoothing()
    draw_image(img, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, MAP_WIDTH/2, MAP_HEIGHT/2)

    i = 0
    while not window_closed():
        if i > 49:
            break
        city = cities[i]
        enable_fill()
        set_fill_color(255/255.0, 165/255.0, 0)  # Set color of the rectangle to red

        name = city.name

        x = (COEFF_X * city.longitude + OFFSET_X)  # Get the value of x coordinate in pixels
        y = (COEFF_Y * city.latitude + OFFSET_Y)  # Get the value of y coordinate in pixels

        draw_rectangle(x, y, 5, 5)  # Draw a rectangle on the map for the city
        sleep(0.2)
        draw_text(name, x, y, True)
        request_redraw()
        sleep(0.2)
        i += 1


def draw_window():
    """
    Draws the graphics window and calls the draw_map function that draws the world map with most populous cities marked
    as orange rectangles
    :return: None
    """
    start_graphics(draw_map, "World Map Showing Most Populated Cities", WINDOW_WIDTH, WINDOW_HEIGHT, True)


draw_window()