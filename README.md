# dice_tools
Rolls dice based on the provided dice notation and returns the result, with options for advantage and disadavantage rolls.

Notation examples:

    - 2d6+3
    - 1d20
    - 3d8-1
    
## Usage
Simply call your desired function with dice notation as a string (Dice notation format: [number of dice]d[number of sides]+/-[modifier])

Function returns int with results of roll.

### Functions
roll_dice: Roll dice via provided notation, with applicable modifier. Returns total.

roll_advantage: Roll dice via provided notation, keeping highest roll, with applicable modifier. Returns total.

roll_disadvantage: Roll dice via provided notation, keeping lowest roll, with applicable modifier. Returns total.
