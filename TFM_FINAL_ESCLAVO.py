from email.message import EmailMessage
import matplotlib.pyplot as plt
from tkinter import messagebox
from datetime import datetime
from   tkinter  import *
from PIL import Image
import tkinter as tk
import numpy as np
import pytesseract
import imapclient
import random
import smtplib
import pyautogui
import pyzmail
import time
import cv2
import csv
import re
import os

from openai import OpenAI

def generar_respuesta():
    client = OpenAI(api_key="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")
    titulos = titulo
    prompt = f"Regalame una respuesta para postear en Reddit con respecto al siguiente titulo: {titulos}, pero dame sola la descripcion sin poner titulo ni descripcion: y tampoco quiero que la respuesta tenga caracteres especiales o tildes, si pregunto el mismo titulo dame otra respuesta distinta"
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content

def movimiento_mause():
    x = random.randint(150, 700)
    y = random.randint(150, 700)
    
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.moveTo(x, y, duration=0.3)
    
def estabilidad():
    time.sleep(2)

def abrir_google():

    # ============================================
    # FASE 1: ABRIR NAVEGADOR CHROME DESDE ESCRITORIO
    # ============================================

    print("Esperando que el escritorio esté listo...")
    estabilidad()
    print("Buscando icono de Chrome en pantalla...")
    pos = pyautogui.locateCenterOnScreen('chrome_icon.png', confidence=0.7)

    if pos:
        pyautogui.moveTo(pos, duration=0.5)
        pyautogui.click(clicks=2)
        print("Chrome encontrado y abierto.")
    else:
        print("No se encontró el icono de Chrome.")
        exit()
        
    estabilidad()
    pyautogui.click()    
    logueo()
    
def logueo():
    
    # =====================================
    # FASE 1: NAVEGAR A HTTPS://REDDIT.COM
    # =====================================

    print("Accediendo a la barra de direcciones...")
    
    movimiento_mause()
    pyautogui.moveTo(150, 75, duration=0.2)
    pyautogui.click()
    estabilidad()
    
    # Limpiar contenido previo con un espacio
    estabilidad()

    # Escribir la URL de Reddit
    print("Escribiendo URL de Reddit...")
    pyautogui.press('space')
    pyautogui.write('reddit.com', interval=0.05)
    pyautogui.press('space')
    pyautogui.press('enter')
    estabilidad()

    # ===============================
    # FASE 4: INICIO DE SESIÓN EN REDDIT
    # ===============================

    # Clic en botón 'Iniciar sesión'
    print("Haciendo clic en 'Iniciar sesión'...")
    

    movimiento_mause()    
    pyautogui.moveTo(1750, 165, duration=0.5)
    pyautogui.click(clicks=2)  

    # Ingresar nombre de usuario
    print("Ingresando nombre de usuario...")
    
    movimiento_mause()
    pyautogui.moveTo(1000, 625, duration=0.5)   
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.write("Every-Cartoonist8180", interval=0.05)
    pyautogui.press('space')

    estabilidad()
    
    # Ingresar contraseña
    print("Ingresando contraseña...")

    movimiento_mause()
    pyautogui.moveTo(1000, 725, duration=0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.write("JULIAN1007896503", interval=0.05)

    # Clic en botón final para iniciar sesión
    print("Confirmando inicio de sesión...")

    estabilidad    
    movimiento_mause()
    pyautogui.moveTo(1000, 925, duration=0.5)
    pyautogui.click()
    
    publicar()
    
def publicar():
    estabilidad()
    print("Esperando carga de la interfaz de Reddit...")

    estabilidad()    
    movimiento_mause
    print("Abriendo menú de perfil...")
    pyautogui.moveTo(1860, 165, duration=0.5)
    pyautogui.click()

    estabilidad()    
    print("Ingresando al perfil...")
    pyautogui.moveTo(1860, 260, duration=0.5)
    pyautogui.click()
    
    estabilidad() 
    movimiento_mause
    print("Buscar perfil...")
    pyautogui.moveTo(880, 185, duration=0.5)
    pyautogui.click()

    estabilidad()
    print("Buscar User maestro...")
    pyautogui.write(str(usuario), interval=0.05)
    pyautogui.press('enter')
    estabilidad()

    estabilidad()
    print("Buscar Personas...")
    pyautogui.moveTo(1080, 260, duration=0.5)
    pyautogui.click()

    estabilidad()
    print("Click en personas Personas...")
    pyautogui.moveTo(1080, 260, duration=0.5)
    pyautogui.click()

    estabilidad()
    print("Click en el maestro")
    pyautogui.moveTo(680, 380, duration=0.5)
    pyautogui.click()
  
    estabilidad()
    print("Escribir Titulo...")
    pyautogui.moveTo(1100, 185, duration=0.5)
    pyautogui.click()
    pyautogui.write(str(titulo), interval=0.05)
    pyautogui.press('enter')

    estabilidad()
    print("Click en el post...")
    pyautogui.moveTo(1100, 485, duration=0.5)
    pyautogui.click()

    estabilidad()
    print("Click en el post, para verlo...")
    pyautogui.moveTo(1100, 485, duration=0.5)
    pyautogui.click()
        
    estabilidad()
    print("Click en upvote...")
    pyautogui.moveTo(470, 510, duration=0.5)
    pyautogui.click()

    estabilidad()
    print("Click en comentar...")
    pos = pyautogui.locateCenterOnScreen('comentar.png', confidence=0.7)
    
    if pos:
        pyautogui.moveTo(pos, duration=0.5)
        pyautogui.click(clicks=1)
        print("Chrome encontrado y abierto.")
    else:
        print("No se encontró el icono de Chrome.")
        exit()
        
    descripcion = generar_respuesta()
    pyautogui.write(str(descripcion), interval=0.05)

    pos = pyautogui.locateCenterOnScreen('upcomentar.png', confidence=0.7)
    
    if pos:
        pyautogui.moveTo(pos, duration=0.5)
        pyautogui.click(clicks=1)
        print("Chrome encontrado y abierto.")
    else:
        print("No se encontró el icono de Chrome.")
        exit()
        
    correo()
    
    while True:
        print("=== Ejecutando función... ===")
        publicar()
        print("=== Esperando 60 minutos para la siguiente ejecución... ===")
        time.sleep(3600)
        
def correo():
    
    global usuario,titulo
    # ==== CONFIGURACIÓN ====
    EMAIL = 'julianpinto258@gmail.com'
    APP_PASSWORD = 'dwfo xpdi ilhu lswh'  # tu contraseña de aplicación
    ASUNTO_BUSCADO = "Comando para el bot esclavo"

    # ==== CONEXIÓN ====
    imap = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap.login(EMAIL, APP_PASSWORD)
    imap.select_folder('INBOX', readonly=True)

    # ==== BÚSQUEDA DE CORREOS POR ASUNTO ====
    UIDs = imap.search(['SUBJECT', ASUNTO_BUSCADO])
    if not UIDs:
        print("No se encontró ningún correo con ese asunto.")
        exit()

    ultimo_UID = UIDs[-1]
    mensaje_raw = imap.fetch([ultimo_UID], ['BODY[]', 'FLAGS'])[ultimo_UID][b'BODY[]']
    mensaje = pyzmail.PyzMessage.factory(mensaje_raw)

    # ==== PROCESO DE ADJUNTO ====
    for parte in mensaje.mailparts:
        if parte.filename == 'comando.txt':
            contenido = parte.get_payload().decode(parte.charset or 'utf-8')
            
            # Guardar en la carpeta Descargas
            descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'comando.txt')
            with open(descargas_path, 'w', encoding='utf-8') as f:
                f.write(contenido)
            
            print(f"Archivo 'comando.txt' guardado en: {descargas_path}")
            break
    else:
        print(" No se encontró el archivo comando.txt adjunto.")

    imap.logout()

    # Ruta al archivo descargado desde el correo (en carpeta Descargas)
    ruta = os.path.join(os.path.expanduser("~"), "Downloads", "comando.txt")

    # Verificar si el archivo existe
    if not os.path.exists(ruta):
        print("No se encontró el archivo comando.txt en Descargas.")
        exit()

    # Leer contenido
    with open(ruta, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    # Inicializar variables
    usuario = ""
    titulo = ""

    # Extraer valores
    for linea in lineas:
        if linea.startswith("usuario="):
            usuario = linea.split("=")[1].strip()
        elif linea.startswith("titulo="):
            titulo = linea.split("=")[1].strip()

    # Mostrar en consola
    print("Archivo leído correctamente.")
    print(f"Usuario maestro: {usuario}")
    print(f"Título del post: {titulo}")
    
correo()
abrir_google()
