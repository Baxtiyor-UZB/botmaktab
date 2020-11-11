from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
from telegram import update
from telegram import replymarkup
from telegram.callbackquery import CallbackQuery
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler,ConversationHandler,MessageHandler,Filters

STATE_START=1
STATE_BOSH_MENU=2
STATE_FANLAR=3
STATE_SINFLAR=4

bot_haqida,kurjoklar,tanlovlar='🏬BOT haqida',"👨‍💻👩‍💻‍To'garaklar","🏆Tanlovlar" 

algebra,geometriya,informatika,dasturlash,bosh_menu='algebra','geometriya','informatika','Texnalogiyalar va dasturlash tillari','Bosh menyuga'

python,html,css,js='PYTHON','HTML','CSS','JAVASCRIPT'

MENU_tugmalar = ReplyKeyboardMarkup([[bot_haqida],[kurjoklar],[tanlovlar]],resize_keyboard=True)

SINF_tugmalar = ReplyKeyboardMarkup([[5,6],[7,8],[9,10],[11]],resize_keyboard=True)

FANLAR_tugmalar = ReplyKeyboardMarkup([[algebra,geometriya],[informatika],[dasturlash]],resize_keyboard=True)

DASTURLASH_tugmalar=ReplyKeyboardMarkup([[python,html],[css,js],[bosh_menu]],resize_keyboard=True)


def start(Update,context):
    user = Update.message.from_user
    buttons = [
            [
                InlineKeyboardButton("BOTDAN FOYDALANISH",callback_data='bolim1')
           
            ]
            # ,
            # [
            #     InlineKeyboardButton("👨‍🎓O'qituvchi sifatida davom etish",callback_data='bolim2')
            # ]
        ]
    Update.message.reply_html("Asssalomu aleykum <b>{}</b> \n <b>Maktab botiga xush kelibsiz</b>\n " .
    format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_START    
def inline_callback(update,context):
    try:
        query=update.callback_query
        # query.message.delete()
        query.message.reply_html(text="👏<b>Juda ajoyib. </b>\nSizga foydam tegsa xursand bo'laman ",reply_markup=MENU_tugmalar)
        return STATE_BOSH_MENU
    except Exception as e:
        print('error',str(e))
################################################
def sinflaga(update,context):
    
    update.message.reply_html(text='<b>sinflar</b>',reply_markup=SINF_tugmalar)


def krujoklaga(update,context):
    update.message.reply_html(text="<b>To'garaklar</b>",reply_markup=FANLAR_tugmalar)
def tanlovlaga(update,context):
    update.message.reply_html(text="<b>Hurmatli foydalanuvchi har oyning \noxirgi ikki kunida , biz jamoamiz\n bilan o'quvchilar orasidan qiziquvchan, \nintiluvchan , o'quvchilarni saralab olamiz\n Murojaat uchun informatika xonasiga boring.</b>",reply_markup=MENU_tugmalar)
########################################fanlar###################################
def algebrafunk(update,context):
    update.message.reply_html(text='<b>sinflar</b>',reply_markup=MENU_tugmalar)
def geometriyafunk(update,context): 
    update.message.reply_html(text='<b>sinflar</b>',reply_markup=SINF_tugmalar)
def informatikafunk(update,context):
    update.message.reply_html(text='<b>sinflar</b>',reply_markup=SINF_tugmalar)
def dasturlashfunk(update,context):
   update.message.reply_html(text='<b>sinflar</b>',reply_markup=DASTURLASH_tugmalar)
def bosh_menufunk(update,context):
   update.message.reply_html(text='<b>sinflar</b>',reply_markup=MENU_tugmalar)
def bot_haqidaa(update,context):
    update.message.reply_html(text='<b>Bu BOT UZBEKpy asoschisi tomonidan\n python dasturlash tilida yozilgan\n Maqsad: Aniq fanlarni rivojlantirish.\n</b>',reply_markup=MENU_tugmalar)

##########################################main###########################################
def main():
    
    updater = Updater('token',use_context=True)
    dispatcher = updater.dispatcher
    # dispatcher.add_handler(CommandHandler('start', start))
    # dispatcher.add_handler(CallbackQueryHandler(inline_callback))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            STATE_START:[CallbackQueryHandler(inline_callback)],
            
            STATE_BOSH_MENU:[
                MessageHandler(Filters.regex('^('+bot_haqida+')$'), bot_haqidaa),
                MessageHandler(Filters.regex('^('+kurjoklar+')$'), krujoklaga),
                MessageHandler(Filters.regex('^('+tanlovlar+')$'), tanlovlaga) 
                ],
            STATE_FANLAR:[
                MessageHandler(Filters.regex('^('+algebra+')$'), algebrafunk),
                MessageHandler(Filters.regex('^('+geometriya+')$'), geometriyafunk),
                MessageHandler(Filters.regex('^('+informatika+')$'), informatikafunk),
                MessageHandler(Filters.regex('^('+dasturlash+')$'), dasturlashfunk),
                MessageHandler(Filters.regex('^('+bosh_menu+')$'), bosh_menufunk) 
                ],
                
        },
        fallbacks=[CommandHandler('start',start)]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
   
main()
