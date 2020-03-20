# Cell-Game
A Python command line game which simulate the life of cells

In short, the program should keep track of a board of any size, where each field
in the board contains a cell. A cell can be alive or dead. The simulation takes place
through multiple generations using regular updates, where cells die or live
depending on their surroundings.

A screenshot of the game:

![cellegae](https://user-images.githubusercontent.com/20997734/77190167-0efb0200-6ad9-11ea-83c5-0d52cc9e20ab.png)


The new status of a cell is determined by the following rules:
  If the cell's current status is "alive":
  <li>
    ○ In fewer than two living neighboring cells, the cell dies (subpopulation).
    ○ With two or three living neighbor cells, the cell will live on.
    ○ If the cell has more than three living neighboring cells, it will die (overpopulation)
  </li>
  If the cell is "dead":
  <li>
    The cell's status becomes "alive" (reproduction) if it has exactly three
    living neighbors.
  </li>
