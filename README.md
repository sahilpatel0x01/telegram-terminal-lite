# telegram-terminal-lite

A minimal, fast, and interactive command-line interface (CLI) client (MVP) for Telegram, built with Python. 

This project allows you to navigate through your Telegram chats (Users, Groups, Channels, and Bots) and view recent messages directly in your terminal, using an elegant Textual User Interface.

## 🌟 Features

- **Interactive CLI Navigation**: Built with `questionary` for easy, arrow-key navigation through menus.
- **Categorized Chats**: Automatically organized into Users, Groups, Channels, and Bots.
- **Rich Terminal UI**: Beautiful rendering of messages and UI elements using `rich`.
- **Fast & Minimal**: Powered by `telethon`, ensuring extremely fast operations and low resource usage.

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- A Telegram API ID and Hash (Get it from [my.telegram.org](https://my.telegram.org))

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/telegram-cli.git
cd telegram-cli
```

### 2. Set up virtually environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory (you can copy `.env.example` and rename it.) and add your Telegram API credentials:

```ini
TG_API_ID=your_api_id
TG_API_HASH=your_api_hash
```

*Note: Never commit your `.env` or `session/` folder to GitHub. They are already included in the `.gitignore`.*

## 💻 Usage

Run the main script to start the application:

```bash
python main.py
```

On your first run, you will be prompted to log in using your phone number and the login code sent to your Telegram account.

### Navigation Flow:
1. **Select a category**: Users, Groups, Channels, or Bots.
2. **Select a chat/dialog**: Choose the specific entity you want to view.
3. **View Messages**: The CLI will fetch and display the last 20 messages in an organized table.
4. Press `Enter` to go back to the chat selection menu.

## 📁 Project Structure

- `main.py` - Application entry point. Handles the main loop and ties components together.
- `auth.py` - Manages Telegram client initialization, session handling, and authentication.
- `chat_loader.py` - Fetches and categorizes all your active Telegram dialogs.
- `ui.py` - Contains the logic for the interactive prompt selections and rendering message tables.

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

