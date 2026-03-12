# Función dinámica: ahora recibe al usuario para consultar su chat_id en el perfil
import requests


def enviar_telegram(mensaje, user):
    token = "8331430908:AAHZRJi45VlZbaSoQ9YioO8p9615_Bw2_Jc"
    chat_id = getattr(user, 'profile', None) and user.profile.telegram_id
    
    print(f"DEBUG: Intentando enviar a {chat_id} | Mensaje: {mensaje}") # <-- Pista 1
    
    if chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        try:
            response = requests.post(url, data={'chat_id': chat_id, 'text': mensaje}, timeout=5)
            print(f"DEBUG: Respuesta Telegram Status: {response.status_code}") # <-- Pista 2
            print(f"DEBUG: Respuesta Telegram Cuerpo: {response.text}")      # <-- Pista 3
        except Exception as e:
            print(f"DEBUG: Error crítico: {e}")
    else:
        print("DEBUG: No se encontró un chat_id para este usuario.")