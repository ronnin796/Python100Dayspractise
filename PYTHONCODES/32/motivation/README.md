
# Motivation

A Python script that sends motivational quotes via email every specified day.

## Features

- Reads quotes from a local text file
- Sends a random quote via email using Gmail SMTP
- Runs automatically on Tuesdays
- Uses environment variables for secure credential management

## Requirements

- Python 3.x
- `python-decouple` library

## Setup

1. Install dependencies:
    ```bash
    pip install python-decouple
    ```

2. Create a `.env` file in the project directory:
    ```
    EMAIL_USER=your_gmail@gmail.com
    EMAIL_PASSWORD=your_app_password
    receiver_email=recipient@example.com
    ```

3. Create a `quotes.txt` file with one quote per line

4. Run the script:
    ```bash
    python main.py
    ```

## Notes

- The script only sends emails on days specified 
- For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password
- Schedule with cron or task scheduler for automated execution
