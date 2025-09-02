
from modules.reading_markedonw import readingMarkedown
from modules.break_documents import breakDocument
from modules.create_db import createDB
from modules.create_agent import agentAI
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import os

from modules.bot_telegram import *
from dotenv import load_dotenv

load_dotenv()


def executor():
    #Carregador do documento
    documento =readingMarkedown()
    #Dividir o texto
    chunk = breakDocument(documento)
    #Base De Dados
    createDB(chunk)
    #agentAI()
   




if __name__=="__main__":
    #executor()
    application = ApplicationBuilder().token(os.environ.get("TELEGRAM_API_KEY")).build()
    
    
    application.add_handler(MessageHandler(filters.TEXT, mensagem))
    application.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, audio_handler))  
    application.add_error_handler(error)
    
    print("Bot do Telegram iniciando...")
   
    application.run_polling(timeout=3)

   
    