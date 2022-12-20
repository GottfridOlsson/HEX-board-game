##=======================================================##
##     Project: HEX BOARD GAME
##        File: plot_hexagons.py
##      Author: GOTTFRID OLSSON 
##     Created: 2022-12-20
##     Updated: 2022-12-20
##       About: Plot hexagons for the board, to lasercut.
##=======================================================##

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


## TODO: kolla hur man graverar hela hexagonerna i laserskäraren (måste jag fylla alla hexagoner i SVG?)

########3 hmmm: kanske lära mig att generera SVG-kod istället. Känns mer allmänt, inte mycket svårare, och blir nog bättre/enklare så med laserskärning,
# speciellt om jag behöver gravera g.a. ha fill i varje hexagon!

## TODO: plot rows of hexagonals, e.g. define function that draws n rows with m columns of hexagonals
## TODO: plot the rows, but now with some equal spacing between all hexagonals (walls IRL)
## TODO: include some scale in the PDF s.t. I can make sure it has the correct size before lasercutting
## TODO: 


export_figure = True
PDF_filepath = "C:\HEX Board game\HEX_board_game.pdf"



def get_hexagonal_corner_coordinates(x_coordinate_base, y_coordinate_base, sidelength):
    # Cartesian coordinates for the corners of a hexagon, going around in mathematical positive direction
    # with the last extra coordinate the same as the first, for easier code below 
    corner_coordinates_x = [x_coordinate_base,
                            x_coordinate_base + sidelength * np.sqrt(3)/2, 
                            x_coordinate_base + sidelength * np.sqrt(3)/2, 
                            x_coordinate_base + sidelength * 0, 
                            x_coordinate_base - sidelength * np.sqrt(3)/2, 
                            x_coordinate_base - sidelength * np.sqrt(3)/2, 
                            x_coordinate_base
                            ]
                                
    corner_coordinates_y = [y_coordinate_base,
                            y_coordinate_base + sidelength * 1/2, 
                            y_coordinate_base + sidelength * 3/2, 
                            y_coordinate_base + sidelength * 2,
                            y_coordinate_base + sidelength * 3/2, 
                            y_coordinate_base + sidelength * 1/2, 
                            y_coordinate_base
                            ]

    return (corner_coordinates_x, corner_coordinates_y)



# Given base coordinates, lowest points, ('x', 'y') in Cartesian coordinates
# draw hexagon with sidelength 'sidelength' with plt
def draw_hexagon(x_coordinate_base, y_coordinate_base, sidelength, linestyle='-', linecolor='k'):


    (corner_coordinates_x, corner_coordinates_y) = get_hexagonal_corner_coordinates(x_coordinate_base, y_coordinate_base, sidelength)

    for corner in range(6):
        x_start = corner_coordinates_x[corner]
        x_end   = corner_coordinates_x[corner+1]
        y_start = corner_coordinates_y[corner]
        y_end   = corner_coordinates_y[corner+1]

        plt.plot([x_start, x_end], [y_start, y_end], linestyle=linestyle, color=linecolor)
    print(f"Successfully drew hexagon at position ({x_coordinate_base},{y_coordinate_base}) with sidelength {sidelength}")

def get_hexagon_height_from_sidelength(sidelength):
    return np.sqrt(3)*sidelength





plt.figure(figsize=(15,15))

n_hexagons = 5
sidelength = 2.5

for hexagon in range(n_hexagons):
    hexagon_height = get_hexagon_height_from_sidelength(sidelength)
    x_0 = hexagon*hexagon_height
    y_0 = 0

    draw_hexagon(x_0, y_0, sidelength)

plt.axis('square')
plt.tight_layout()
if export_figure:
    matplotlib.pyplot.savefig(PDF_filepath, format='pdf', bbox_inches='tight')

plt.show()


