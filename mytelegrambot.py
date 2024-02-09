from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Define the button callback function
def button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'disclaimer':
        # Handle disclaimer button
        pass  # Placeholder, add your code here
    elif query.data == 'coding':
        coding_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Telegram Menu Bot Code", callback_data='menu_bot_code')],
            [InlineKeyboardButton("Telegram Credit Card Checker Bot Code", callback_data='credit_card_checker_code')],
        ])
        update.message.reply_text("You selected: Coding. Please select the code you wish to purchase using the buttons below.",
                                  reply_markup=coding_markup)
    elif query.data == 'menu_bot_code':
        payment_method_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("PayPal", callback_data='paypal')],
            [InlineKeyboardButton("Stripe", callback_data='stripe')],
            [InlineKeyboardButton("Bitcoin", callback_data='bitcoin')],
        ])
        update.message.reply_text("You have selected Telegram Menu Bot Code!! Please choose a payment method:",
                                  reply_markup=payment_method_markup)
    elif query.data == 'credit_card_checker_code':
        payment_method_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("PayPal", callback_data='paypal')],
            [InlineKeyboardButton("Stripe", callback_data='stripe')],
            [InlineKeyboardButton("Bitcoin", callback_data='bitcoin')],
        ])
        update.message.reply_text("You have selected Checker Bot Code!! Please choose a payment method:",
                                  reply_markup=payment_method_markup)
    elif query.data == 'fortnite_accounts':
        battle_pass_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Battle Pass (All pages Unlocked)", callback_data='battle_pass')],
            [InlineKeyboardButton("No Battle Pass (All Pages Free Pages Unlocked)", callback_data='no_battle_pass')],
        ])
        update.message.reply_text("You have selected Fortnite Accounts!! Please choose an option:",
                                  reply_markup=battle_pass_markup)
    # Handle other categories and options similarly

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Bot! Use /menu to access the main menu.")

# Define the menu command handler
def menu(update: Update, context: CallbackContext) -> None:
    main_menu_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Disclaimer", callback_data='disclaimer')],
        [InlineKeyboardButton("Coding", callback_data='coding')],
        [InlineKeyboardButton("Gaming", callback_data='gaming')],
        [InlineKeyboardButton("VPN", callback_data='vpn')],
        [InlineKeyboardButton("Premium", callback_data='premium')],
    ])
    update.message.reply_text("Please select a category:", reply_markup=main_menu_markup)

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("6714027735:AAGKdtQI3Pcgk_XInyuQY-GfqPTLOOC5lJA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))

    # Register callback query handler
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
