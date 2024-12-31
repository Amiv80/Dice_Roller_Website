# Dice Roller Web Application

Welcome to the Dice Roller Web Application! This project allows users to roll dice with different configurations (such as D4, D6, D20) and apply modifiers (e.g., +2, -1). Users can customize their dice rolls by specifying the number of dice, the sides of the dice, and any additional modifiers. It also includes the ability to toggle between Dark and Light mode for a better user experience.

## Features

- **Dice Type Selection**: Choose from predefined dice types (D4, D6, D8, D10, D12, D20) or input custom dice values (e.g., D30).
- **Roll Dice**: Roll the dice multiple times, and view the results with a total and modifier.
- **Modifier Input**: Add modifiers to your dice rolls (e.g., +3, -2).
- **Dark Mode Toggle**: Switch between Light and Dark modes for a personalized viewing experience.
- **Responsive Design**: The app is mobile-friendly and adjusts to various screen sizes.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/dice-roller.git
   ```
2. Install the required dependencies (make sure you have Python and Django installed):
   ```bash
   cd dice-roller
   pip install -r requirements.txt
   ```

3. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and go to `http://127.0.0.1:8000/` to use the application.

## Usage

- When you load the page, you can:
  - Select the number of dice to roll and the type of dice (e.g., D6, D20).
  - Add any modifiers (e.g., +2 or -1) to the rolls.
  - Press the "Roll Dice" button to get the results.
- You can also toggle between **Light Mode** and **Dark Mode** for a better user experience.

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.
