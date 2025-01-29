
# Slot Machine Game

A text-based slot machine game implemented in Python where players can deposit money, place bets on multiple lines, and try their luck at matching symbols.

## Features

- Interactive text-based interface
- Customizable betting system
- Multiple betting lines (1-3)
- Balance management
- Random symbol generation
- Different symbol frequencies for varied gameplay

## Requirements

- Python 3.x
- Random module (built-in)

## Installation

1. Clone the repository:
```
git clone [repository-url]
cd slot-machine-game
```

2. Run the game:
```
python slot_machine.py
```

## How to Play

1. **Start the Game**
   - Run the script
   - Enter your initial deposit amount

2. **Place Your Bet**
   - Choose number of lines to bet on (1-3)
   - Select bet amount per line ($10-$100)

3. **Game Rules**
   - Match symbols across your chosen betting lines
   - Different symbols have different values:
     - A: Highest value (rare)
     - B: Medium-high value
     - C: Medium-low value
     - D: Lowest value (common)

## Game Configuration

```
LINES_MAX = 3    # Maximum betting lines
MAX_BET = 100    # Maximum bet per line
MIN_BET = 10     # Minimum bet per line
ROWS = 3         # Slot machine rows
COLUMNS = 3      # Slot machine columns
```

## Symbol Distribution

| Symbol | Frequency | Value |
|--------|-----------|-------|
| A | 2 | Highest |
| B | 4 | Medium-High |
| C | 6 | Medium-Low |
| D | 8 | Lowest |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the Creative Commons Zero v1.0 Universal - see the LICENSE file for details.

## Author

Yasharth Bajpai

## Version History

- 1.0
  - Initial Release
  - Basic game functionality
  - Betting system implementation

## Acknowledgments

- Inspired by classic slot machine games
- Built as a learning project for Python programming

## Future Improvements

- Add graphical user interface
- Implement more complex winning patterns
- Add sound effects
- Include progressive jackpot system
- Save high scores
- Add multiplayer functionality

## Support

For support, open an issue in the repository.


