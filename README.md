# Discord Joke Bot 🤖😄

A simple Discord bot that tells jokes when users type the `!joke` command.

## Prerequisites

Before running the bot, make sure you have:

- Python 3.7 or higher installed
- `discord.py` library installed
- A Discord bot token from the Discord Developer Portal

## Installation

1. **Install discord.py**:
   ```bash
   pip install discord.py
   ```

2. **Clone or download the bot script**

3. **Set up your Discord bot token**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application and bot
   - Copy the bot token
   - **IMPORTANT**: Replace `YOUR_BOT_TOKEN_HERE` in the script with your actual bot token

## Usage

1. **Run the bot**:
   ```bash
   python bot.py
   ```

2. **Invite the bot to your server**:
   - Go to the Discord Developer Portal
   - Navigate to your bot's OAuth2 section
   - Select the "bot" scope and necessary permissions
   - Use the generated URL to invite the bot to your server

3. **Use the bot**:
   - Type `!joke` in any channel where the bot has access
   - The bot will respond with a random joke

## Bot Permissions

The bot needs the following permissions:
- Read Messages
- Send Messages
- Read Message History

## Customization

You can easily customize the bot by:
- Changing the command prefix from `!` to something else
- Adding additional commands and features

## Troubleshooting

**Bot doesn't respond:**
- Check if the bot is online and has proper permissions
- Verify the bot token is correct
- Make sure the bot can read and send messages in the channel

**Installation issues:**
- Ensure you have Python 3.7+ installed
- Try upgrading pip: `pip install --upgrade pip`
- Use `python3` and `pip3` if you have multiple Python versions

## Support

If you encounter any issues:
1. Check the console for error messages
2. Verify your bot token and permissions
3. Make sure discord.py is properly installed

---

**Happy joking! 🎭**