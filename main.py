from aiogram import Dispatcher, Bot, F, filters, types
import asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import TOKEN, Admin
from database import Database
from reply_button import main_button1, main_button2
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Add_new_food(StatesGroup):
    name_of_food = State()
    price_of_food = State()


class Add_new_drink(StatesGroup):
    name_of_drink = State()
    price_drink = State()


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = Database()

db.create_table()
db.create_food_table()
db.create_drinks_table()

table1 = db.select_from_table()
# table2 = db.select_food_table()


@dp.message(filters.Command('start'))
async def start_bot(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    db.insert_into_table(user_id, user_fullname)
    # db.delete_data()
    # db.drop_table()

    if message.from_user.id == Admin:
        await message.answer("Добро пожаловать", reply_markup=main_button1)
    else:
        await message.answer("Добро пожаловать", reply_markup=main_button2)


@dp.message(F.text == "Еда🍔")
async def show_foods(message: types.Message):
    data2 = db.select_food_table()
    all_foods_keyboard = ReplyKeyboardMarkup(keyboard=[])
    for every_food in data2:
        button = [KeyboardButton(text=every_food[0])]
        all_foods_keyboard.keyboard.append(button)
    all_foods_keyboard.keyboard.append([KeyboardButton(text="Вернутся")])

    await message.answer("Вы выбрали категорию еды:", reply_markup=all_foods_keyboard)


@dp.message(F.text == "Вернутся")
async def back(message: types.Message):
    await message.answer("Вы вернулись: ", reply_markup=main_button1)


@dp.message(F.text == "Добавить новое блюдо🍔")
async def add_new_food(message: types.Message, state: FSMContext):
    if message.from_user.id == Admin:
        await message.answer("Вы выбрали категорию добавить блюдо: ")
        await state.set_state(Add_new_food.name_of_food)
        await message.answer("Напишите название блюда: ")
    else:
        await message.answer("Пожалуйста не пытайтесь взломать мой бот")


@dp.message(Add_new_food.name_of_food)
async def add_new_food2(message: types.Message, state: FSMContext):
    await state.update_data(name_of_food=message.text)
    await state.set_state(Add_new_food.price_of_food)
    await message.answer("Напишите цену нового блюда: ")


@dp.message(Add_new_food.price_of_food)
async def add_new_food3(message: types.Message, state: FSMContext):
    await state.update_data(price_of_food=message.text)
    data = await state.get_data()
    await message.answer(f"Вы добавили новое блюдо: {data['name_of_food']}")
    db.insert_food_table(data['name_of_food'], data['price_of_food'])
    await state.clear()


@dp.message(F.text == "Напитки🍹")
async def show_drinks(message: types.Message):
    data2 = db.select_drinks_table()
    all_drinks = ReplyKeyboardMarkup(keyboard=[])
    for every_drink in data2:
        button = [KeyboardButton(text=every_drink[0])]
        all_drinks.keyboard.append(button)
    all_drinks.keyboard.append([KeyboardButton(text="Вернутся")])
    await message.answer("Вы выбрали категорию еды:", reply_markup=all_drinks)


@dp.message(F.text == "Добавить напиток🍹")
async def add_drinks(message: types.Message, state: FSMContext):
    await message.answer("Вы выбрали категорию добавить напиток:")
    await state.set_state(Add_new_drink.name_of_drink)
    await message.answer("Какой напиток хотите добавить:")


@dp.message(Add_new_drink.name_of_drink)
async def add_drink2(message: types.Message, state: FSMContext):
    await state.update_data(name_of_drink=message.text)
    await state.set_state(Add_new_drink.price_drink)
    await message.answer("Добавьте цену напитка:")


@dp.message(Add_new_drink.price_drink)
async def add_drink3(message: types.Message, state: FSMContext):
    await state.update_data(price_drink=message.text)
    data = await state.get_data()
    await message.answer(f"Вы добавили новый напиток: {data['name_of_drink']}")
    db.add_drinks_table(data['name_of_drink'], data['price_drink'])
    await state.clear()


@dp.message(F.text == "Hot-Dog")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-shedevrum/12896721/video_preview_dc9669c1f2921"
                                     "1eeb85926f09d66c8ac_3/orig",
                               caption="Hot-Dog: 18000")


@dp.message(F.text == "Hamburger")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://sportal365images.com/process/smp-images-production/profit.bg/24012024/d5e"
                                     "e70dd-0dec-481d-84b2-d75cad31a57c.jpg?operations=autocrop(256:256)",
                               caption="Hamburger: 24000")


@dp.message(F.text == "Longer")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShA_7N2AVupvf6ZihrGg6oQX4Jt"
                                     "-MwY0xPIQ&s",
                               caption="Longer: 28000")


@dp.message(F.text == "Lavash")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://www.gorodtaraz.kz/upload/000/u1/0a/a2/lavash-big-photo-normal.jpg",
                               caption="Lavash: 21000")


@dp.message(F.text == "Coca Cola")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQS3IIZueHsv8q33-6zn4SjfLiFz"
                                     "LpFDyUt3Q&s",
                               caption="Coca Cola: 9000")


@dp.message(F.text == "Fanta")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeRmi4bdyzUsuH5JW-k32ElkuyC"
                                     "0BYvECxng&s",
                               caption="Fanta: 9000")


@dp.message(F.text == "Lipton")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScvi3vsMnWWinP2EtYjBO5yC-7s"
                                     "JSem3ZZwg&s",
                               caption="Lipton: 8000")


@dp.message(F.text == "Sprite")
async def hotdog(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFNoDgjBuzLhUgMKOrxZZxRcmSu"
                                     "dA29IzG4A&s",
                               caption="Sprite: 9000")


@dp.message(F.text == 'Все пользователи')
async def all_users(message: types.Message):
    user_id = message.from_user.id
    if user_id == Admin:
        users = db.select_from_table()
        my_list = []
        for user in users:
            my_list.append(user[1])
            await message.answer(f"{"\n".join(my_list)}")
    else:
        await message.answer("У вас нету прав на эту команду")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
