# Personal Expense Tracker

A Python-based command-line application for recording, managing, and analyzing personal expenses.

The application allows users to add, view, edit, and delete expenses while also providing total spending, category-wise summaries, and monthly spending analysis.

## Features

- Add new expenses with date, item, amount, and category
- View all recorded expenses
- Calculate total spending
- View category-wise spending summaries
- Edit existing expenses
- Delete expenses
- View monthly spending summaries
- Store expense data using JSON for persistence
- Validate user input to prevent invalid entries

## Technologies Used

- Python
- JSON
- VS Code

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python expense_tracker.py
```
5. Follow the instructions shown in the terminal.


## Project Structure

expense_tracker.py - Main Python program containing all expense tracking features.

expenses.json - Stores expense data so it remains available after the program is closed.