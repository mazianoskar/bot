from pyrogram import Client,filters
from pyrogram.errors import SessionPasswordNeeded,PhoneCodeExpired
from pyrogram.errors.exceptions.bad_request_400 import PasswordHashInvalid,PhoneCodeInvalid
from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid
from pyromod import listen
API_ID = 26022259
API_HASH = "fbe8ef03027d2372bf5a646879df8112"
TOKEN = "6852472981:AAFXjv7DeyvWt3D9w4P_zJOBMP8XI1kGSPE"
app = Client("Session",api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN, in_memory=True)
@app.on_message(filters.command("start"))
async def Send(app,msg):
  c = Client("Pyrogram",
  API_ID,API_HASH,
  device_model="Paddington3",
  in_memory=True)
  await c.connect()
  a = msg.text
  msg = await app.ask(msg.chat.id,f""" 
✓ 👋 مرحباً بك عزيزي في بوت استخراج جلسات 𝖯𝖸𝖱𝖮𝖦𝖱𝖠𝖬 
✓ ⛔ ارسل رقم الهاتف بهذا شكل 
✓ 📲 مثل :- +964772939**927
✓ 📬 اعلاه مثال ارسل رقم كاملاً :-
@T62RS 
"""
,filters=filters.text)
  Number = msg.text
  try:
  	send = await c.send_code(Number)
  except PhoneNumberInvalid:
  	return await msg.reply("""
✓ ⛔ يرجى ارسال رقم هاتف صالح
""",quote=True)
  except Exception:
         return await msg.reply("✓ 🔱 هنالك صيانه في السيرفرات",quote=True)
  SendCode = send.phone_code_hash
  code = await app.ask(msg.chat.id,f""" 
✓ ✅ الان ارسل رمز التحقق 
✓ 📲 بهذا الشكل :-
✓ `1 2 3 4 5`
"""
,filters=filters.text)
  RecepionCode = code.text
  try:
  	await c.sign_in(Number,SendCode,RecepionCode)
  except SessionPasswordNeeded:
  	Password = await app.ask(msg.chat.id,f"""
✓ ⚠️ الان يرجى ارسال رمز التحقق خطوتين 
"""
  	 ,filters=filters.text)
  	PasswordAss = Password.text
  try:
  	await c.check_password(password=PasswordAss)
  except PasswordHashInvalid:
  	return await Password.reply("✓ ❗ الباسوورد خاطئ ",quote=True)
  except (PhoneCodeInvalid, PhoneCodeExpired):
    return await code.reply("✓ 💔 الكود خطئ ",quote=True)
  try:
  	await c.sign_in(Number,SendCode,RecepionCode)
  except:
  	pass
  a = await msg.reply("✓ 🖲️ انتظر | Wait ",quote=True)
  
  get = await c.get_me()
  text = "||**معلوماتك**|| :\n\n"
  text += f"**اسمك الاول **: {get.first_name}\n"
  text += f"**ايديك **: {get.id}\n"
  text += f"**رقمك** : {Number}\n"
  text += f"\n\n  الرسائل المحفوظه [{get.first_name}](tg://openmessage?user_id={get.id})\n"
  text += "للاستخراج مره اخر اضغط /start"
  Session = await c.export_session_string()
  await a.delete()
  await c.send_message("me",text=f""" 
✓ ♻️ عزيزي هذا هو كود الجلسة
✓ 📢 `{Session}` 
✓ 🔓 يرجى عدم مشاركة هذا الكود مع احد
""")
  await c.disconnect()
  await app.send_message(msg.chat.id,text)
print("Run..")
app.run()
