from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.filters import Command
from keyboards.keyboards import kb1, kb2
from ext_api.ext_api_random_fox import fox

router = Router()

# Обрабатываем команду /Start
@router.message(Command("start"))
async def start_handler(msg: types.Message):
    name = msg.chat.first_name
    await msg.answer(f"Привет, {name} !\n\n")   #, reply_markup=keyboard2)
    await msg.answer("Пока я знаю только 3 команды:\n")
    await msg.answer("/start - То, что ты читаешь сейчас, Бро!\n")
    await msg.answer("/info  - Описание меня, если оно есть :)\n")
    await msg.answer("А еще я могу помочь тебе узнать твой ID, просто отправь мне любое другое сообщение.", reply_markup=kb1)

# Хэндлер на команду /Info
@router.message(Command("info"))
async def info_handler(msg: types.Message):
    description = msg.chat.title
    await msg.answer(f"Описание: {description}", reply_markup=kb1)

# Хэндлер на команду /Zevs (Покажи батяню)
@router.message(Command("zevs"))
@router.message(Command("Покажи батяню!"))
@router.message(F.text.lower() == "покажи батяню!")
async def zevs_handler(msg: types.Message):
    name = msg.chat.first_name
    zevs_photo = FSInputFile("../photos/zevs.jpg")
    await msg.answer(f"Вот мой батяня, {name} !")
    # await msg.answer_photo(photo=zevs_photo, caption="Это мой батек!")
    # await bot.send_photo(msg.from_user.id, photo=img_fox)


# Хэндлер на команду /Fox (Покажи лису)
@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(F.text.lower() == "покажи лису")
async def fox_handler(msg: types.Message):
    name = msg.chat.first_name
    img_fox = fox()
    await msg.answer(f"Держи лису, {name} !")
    await msg.answer_photo(photo=img_fox)
    # await bot.send_photo(msg.from_user.id, photo=img_fox)


# Хэндлер по тексту
@router.message(F.text)
async def msg_echo(msg: types.Message):
    usermsg = msg.text.lower()
    name = msg.chat.first_name
    if 'привет' in usermsg:
        await msg.answer(f"Ну, здорово, {name} !")
    elif 'ты кто' in usermsg:
        await msg.answer(f"Я - бот, {name}. Просто бот...")
        await msg.answer_dice(emoji="🤷")
    elif 'фото' in usermsg:
        await msg.answer(f"Здесь будет фото Зевса")
        # await msg.answer_photo(photo="photos/zevs.jpg", "Это моя батяня!")
    else:
        await msg.answer(f"Ты написал мне:\n {usermsg} \n")
        await msg.answer(f"А че те надо-то? Не догоняю.", reply_markup=kb2)

#@dp.message(F.text == 'Информация')
#@dp.message(Command("info"))
#async def cmd_info(message: types.Message):
#await message.reply("Я бот - твой друг и товарищ 😊")


# Обработчик на любые другие сообщения, не определенные выше.
@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Друг мой, твой ID: {msg.from_user.id}")