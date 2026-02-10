# Birthday Wisher

## Description

An automated email service that sends birthday greetings to contacts on their birthdays. Reads birthday data from CSV and sends personalized emails using SMTP.

## Features

- Automated birthday detection
- Personalized email templates
- Multiple letter variations
- SMTP email delivery
- CSV-based contact management
- Environment variable security for credentials

## Learning Outcomes

- Email automation with SMTP
- Date/time handling and comparison
- CSV file operations with Pandas
- Environment variables for security
- File templating and string replacement
- Conditional scheduling logic
- Email configuration best practices

## How It Works

1. Reads today's date
2. Checks birthday CSV for matches
3. Selects random letter template
4. Customizes letter with recipient name
5. Sends via Gmail SMTP
6. Logs successful delivery

## Setup

1. Create a .env file with credentials:
```
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
MY_NAME=Your Name
```

2. Prepare birthdays.csv with columns:
   - names
   - email
   - month
   - day

3. Create letter_templates with:
   - letter_1.txt
   - letter_2.txt
   - letter_3.txt

## Usage

```bash
python main.py
```

Schedule daily execution using cron or task scheduler.

## Required Files

- birthdays.csv (contact information)
- letter_templates/ (email templates)
- .env (credentials)

## Technologies Used

- Python 3
- smtplib for email
- Pandas for data handling
- python-decouple for environment variables
