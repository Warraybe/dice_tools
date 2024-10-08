import random
import re


def roll_dice(dice_notation: str) -> int:
    """
    Rolls dice based on the provided dice notation and returns the result.

    Examples:
    - 2d6+3
    - 1d20
    - 3d8-1

    Args:
        dice_notation (str): Dice notation format: [number of dice]d[number of sides]+/-[modifier].

    Returns:
        int: Sum of dice rolled, with modifier applied to result if provided.
    """
    num_dice, num_sides, modifier = check_notation(dice_notation)

    return sum(get_rolls(num_dice, num_sides)) + modifier


def roll_advantage(dice_notation: str) -> int:
    """
    Rolls dice based on the provided dice notation and returns the result with advantage.

    Examples:
    - 2d6+3
    - 1d20
    - 3d8-1

    Args:
        dice_notation (str): Dice notation format: [number of dice]d[number of sides]+/-[modifier].

    Returns:
        int: Max of dice rolled, with modifier applied to result if provided.
    """
    num_dice, num_sides, modifier = check_notation(dice_notation)

    return max(get_rolls(num_dice, num_sides)) + modifier


def roll_disadvantage(dice_notation: str) -> int:
    """
    Rolls dice based on the provided dice notation and returns the result with disadvantage.

    Examples:
    - 2d6+3
    - 1d20
    - 3d8-1

    Args:
        dice_notation (str): Dice notation format: [number of dice]d[number of sides]+/-[modifier].

    Returns:
        int: Min of dice rolled, with modifier applied to result if provided.
    """
    num_dice, num_sides, modifier = check_notation(dice_notation)

    return min(get_rolls(num_dice, num_sides)) + modifier


def check_notation(dice_notation: str) -> tuple[int]:
    match = re.match(r"(\d+)d(\d+)([+\-]?\d*)", dice_notation)
    if not match:
        raise ValueError("Invalid dice notation format")

    num_dice = int(match.group(1))
    num_sides = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    return num_dice, num_sides, modifier


def get_rolls(num_dice: int, num_sides: int) -> list[int]:
    return [random.randint(1, num_sides) for _ in range(num_dice)]
