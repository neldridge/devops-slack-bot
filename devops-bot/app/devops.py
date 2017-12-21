
from slackbot import settings
from slackbot.bot import respond_to, listen_to
import re



@listen_to('@devops', re.IGNORECASE)
def devops(message):
    message.reply('Ayyyy', in_thread=True)
    # Hook into creating a jira ticket
    # 
    # Notify the on call person...
