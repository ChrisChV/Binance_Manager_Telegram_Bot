#HEADERS
#TokenFlag True
import sys
import os
from telegram.ext import Updater
import ravegen.Decorators.functionManager as functionManager
sys.path.insert(0, '.')
import modules
import logging

if __name__ == "__main__":
	TOKEN = "717847509:AAGRWVNN9Q_GvH5C82czncUfYmhrzjdX7xk"
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	logger = logging.getLogger(__name__)
	updater = Updater(TOKEN)
	dispatcher = updater.dispatcher
	functionManager.functionManager.generateHandlers(dispatcher)
	updater.bot.deleteWebhook()
	updater.start_polling()
	updater.idle()
