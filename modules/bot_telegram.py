from telegram import Update
from telegram.ext import filters,ApplicationBuilder,ContextTypes,CommandHandler,MessageHandler
from modules.create_agent import agentAI
from telegram.constants import ChatAction
import asyncio
import os
import tempfile
#AIMEDICARE = agentAI()


#Função que monitora qualquer no telegram
async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

#Função que lida com a mensagem
async def mensagem(update:Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text:str = update.message.text
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(2)

    
    #await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    #await asyncio.sleep(2)
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    AI_ANGOLA = agentAI(text=text)
    await update.message.reply_text(AI_ANGOLA)

# Função que lida com voz
async def audio_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice or update.message.audio
    if not voice:
        return

    try:
        # Mostra "gravando"
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.RECORD_VOICE)

        # Faz download do áudio
        file = await context.bot.get_file(voice.file_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = os.path.join(tmpdir, "input.ogg")
            await file.download_to_drive(audio_path)

            
            from openai import OpenAI
            client = OpenAI()  
            
            with open(audio_path, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
                text = transcript.text  
                
            
            
            if not text.strip():
                await update.message.reply_text("Não consegui entender o áudio. Tente novamente.")
                return

           
            AI_ANGOLA = agentAI(text=text)
            await update.message.reply_text(AI_ANGOLA)

    except Exception as e:
        
        print(f"Erro no processamento de áudio: {e}")
        await update.message.reply_text("Ocorreu um erro ao processar o áudio. Tente novamente.")
    
    finally:
       
        pass