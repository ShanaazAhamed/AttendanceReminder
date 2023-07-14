# Attendance Reminder

This Python code is designed to notify users to mark their attendance for school, office, or university. It utilizes the Telegram Bot API and the aiogram library to send messages to users and handle user commands. The code runs as a Telegram bot and sends reminders at specified times to remind users to mark their attendance.

## Prerequisites
Before running the code, make sure you have the following:
 - Python installed on your system.
 - A Telegram account.
 - Telegram API token for your bot. You can obtain this token by creating a new bot on Telegram's BotFather platform.

## Getting Started

1. install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy the provided code into a Python file (e.g., `main.py`).
3. Replace `API_TOKEN = get_token()` with your Telegram API token.
4. Run the Python script using the following command:
   ```bash
     python main.py
   ```
5. Start a conversation with your bot on Telegram and use the following commands to interact with it
   
   - `/start`: Starts the conversation and provides initial instructions.
   - `/subscribe`: Subscribes the user to receive attendance notifications.
   - `/help`: Displays a help message with available commands.
   - `/in`: Sets the user's in-time for attendance.
   - `/out`: Sets the user's out-time for attendance.
   - `/url`: Adds a URL for additional attendance-related information.
  
## How it Works
1. The code uses the `aiogram` library to create a Telegram bot and handle user commands.
2. The bot sends messages to users based on the specified commands.
3. The code utilizes the `apscheduler` library to schedule and send reminder messages at specific times.
4. The `start_shedule()` function is responsible for retrieving attendance times, checking the current time, and sending notification messages to users who need to mark their attendance.
5. The code uses a database module (`client.db.DB`) to retrieve the attendance times and user IDs for sending notifications.
6. The code also includes state management using the aiogram library to handle multi-step commands (e.g., setting in-time, out-time, or URL).
7. The `send_message()` function sends the actual notification messages to users using the Telegram bot API.

## Customization
You can customize the code to fit your specific requirements:
- Modify the commands, messages, and response texts to match your desired workflow.
- Adjust the scheduling interval (seconds=10) in the `sched.add_job()` function to change how often the bot checks for attendance notifications.
- Customize the database module (client.db.DB) to store and retrieve attendance times and user information as per your needs.

Note: This code provides a basic framework for attendance notifications and can be expanded and customized as per your requirements.

Feel free to explore and enhance the code to add more functionality and improve the user experience.
   

