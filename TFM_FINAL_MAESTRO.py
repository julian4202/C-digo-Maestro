from email.message import EmailMessage
import matplotlib.pyplot as plt
from tkinter import messagebox
from datetime import datetime
from   tkinter  import *
from PIL import Image
import tkinter as tk
import numpy as np
import pytesseract
import unicodedata
import pyautogui
import smtplib
import random
import time
import cv2
import csv
import re
import os

def enviar_comando_por_email():
    remitente = "fosaken12gt@gmail.com"
    contraseña = "cjaqdoandsogdspd"  # App password SIN espacios

    destinatario = "julianpinto258@gmail.com"  # <-- CORRECTO, este es el destino

    mensaje = EmailMessage()
    mensaje['Subject'] = "Comando para el bot esclavo"
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje.set_content("Adjunto el archivo comando.txt para el bot esclavo.")

    try:
        with open("comando.txt", 'rb') as f:
            mensaje.add_attachment(
                f.read(),
                maintype='text',
                subtype='plain',
                filename='comando.txt'
            )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remitente, contraseña)
            smtp.send_message(mensaje)
            print(f"✅ Enviado a {destinatario}")

    except Exception as e:
        print(f"❌ Error al enviar: {e}")

def movimientos_mause():
    x = random.randint(150, 700)
    y = random.randint(150, 700)
    
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.moveTo(x, y, duration=0.3)
 
def logueo():
    global USER_GET 
    global PASS_GET
    
    USER_GET = USER.get()
    PASS_GET = PASS.get()
    # ============================================
    # FASE 1: COMPROBACIÓN DE USUARIO
    # ============================================
    if USER_GET == "USER" or PASS_GET == "PASS":
        messagebox.showwarning("Campos vacíos", "Por favor, completa usuario y contraseña.")
        return
    
    # ============================================
    # FASE 2: ABRIR NAVEGADOR CHROME DESDE ESCRITORIO
    # ============================================

    print("Esperando que el escritorio esté listo...")
    time.sleep(2)

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
    movimientos_mause()
    
    # =====================================
    # FASE 3: NAVEGAR A HTTPS://REDDIT.COM
    # =====================================

    print("Accediendo a la barra de direcciones...")
    pyautogui.moveTo(1000, 70, duration=0.5)
    pyautogui.click()
    estabilidad()  

    # Escribir la URL de Reddit
    print("Escribiendo URL de Reddit...")
    pyautogui.write('reddit.com', interval=0.05)
    pyautogui.press('space')
    pyautogui.press('enter')
    estabilidad()
    movimientos_mause()
    
    # ===============================
    # FASE 4: INICIO DE SESIÓN EN REDDIT
    # ===============================

    # Clic en botón 'Iniciar sesión'
    print("Haciendo clic en 'Iniciar sesión'...")
    pyautogui.moveTo(1750, 165, duration=0.5)
    pyautogui.click(clicks=2)

    # Cerrar la ventana de la interfaz gráfica después de iniciar sesión
    ventana.destroy()
    estabilidad()
    movimientos_mause()
    
    # Ingresar nombre de usuario
    print("Ingresando nombre de usuario...")
    pyautogui.moveTo(1000, 625, duration=0.5)
    pyautogui.click()
    estabilidad()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.write(str(USER_GET), interval=0.05)
    pyautogui.press('space')
    pyautogui.moveTo(1000, 580, duration=0.5)
    pyautogui.click()
    
    estabilidad()
    # Ingresar contraseña
    print("Ingresando contraseña...")
    pyautogui.moveTo(1000, 725, duration=0.5)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.write(str(PASS_GET), interval=0.05)

    # Clic en botón final para iniciar sesión
    print("Confirmando inicio de sesión...")
    pyautogui.moveTo(1000, 925, duration=0.5)
    pyautogui.click()
    
    with open("comando.txt", "w", encoding="utf-8") as f:
        f.write(f"usuario={USER_GET}\n")
      
    #publicar()
    extraer_metricas()
    
def publicar():

    # ============================================
    # FASE 1: DEFINICIÓN DE CONTENIDO A PUBLICAR
    # ============================================

    titulos = [
        "Alertan sobre químicos peligrosos en el agua de Bogotá",
        "Gobierno estaría negociando en secreto con disidencias armadas",
        "Documentos filtrados sugieren plan para monitorear celulares durante marchas",
        "Estudio no publicado afirma que ciertas vacunas podrían alterar el sueño",
        "“Desde que mi hijo se vacunó no ha vuelto a dormir bien”, denuncia madre bogotana",
        "Última hora: se reportan apagones en múltiples barrios de Medellín",
        "¿Por qué los medios tradicionales no están hablando del nuevo impuesto digital?",
        "Informe señala posible manipulación en encuestas, pero no ha sido publicado"
    ]

    descripciones = [
        "Padres de familia en redes sociales han reportado casos de irritaciones y dolores estomacales en niños, presuntamente vinculados al agua del grifo.",
        "Varios medios alternativos han sugerido que altos funcionarios estarían sosteniendo diálogos no autorizados con grupos armados, generando gran rechazo político.",
        "Capturas de pantalla muestran supuestos contratos entre entidades del Estado y operadores móviles para rastrear dispositivos durante movilizaciones sociales..",
        "Un grupo de investigadores independientes compartió hallazgos preliminares sobre trastornos del sueño post-vacunación, especialmente en adultos mayores.",
        "Una madre bogotana comparte su experiencia en un video viral donde denuncia cambios en el sueño de su hijo tras la vacunación, sin recibir respuesta médica adecuada.",
        "Vecinos de al menos cinco comunas han informado cortes simultáneos sin previo aviso. Empresas Públicas aún no emite comunicado oficial.",
        "Un ajuste tributario silencioso estaría afectando a quienes hacen compras por apps. ¿Por qué tanto silencio mediático sobre este tema?",
        "Un periodista afirma haber visto cifras que contradicen los resultados oficiales, pero aún no se conoce el documento completo"
    ]

    # ============================================
    # FASE 2: RECORRER Y PUBLICAR CADA POST
    # ============================================
    movimientos_mause()
    
    for i in range(1):
        titulo = titulos[i]
        descripcion = descripciones[i]
        
        with open("comando.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()

        usuario = ""
        for linea in lineas:
            if linea.startswith("usuario="):
                usuario = linea.strip().split("=")[1]

        with open("comando.txt", "w", encoding="utf-8") as f:
            f.write(f"usuario={usuario}\n")
            f.write(f"titulo={titulo}\n")

        print(f"\n=== PUBLICACIÓN {i + 1}/8 ===")

        # ============================================
        # FASE 3: ACCESO AL PERFIL Y CREACIÓN DE POST
        # ============================================

        print("Esperando carga de la interfaz de Reddit...")
        time.sleep(10)

        print("Abriendo menú de perfil...")
        pyautogui.moveTo(1860, 165, duration=0.5)
        pyautogui.click()
        time.sleep(3)

        print("Ingresando al perfil...")
        pyautogui.moveTo(1860, 260, duration=0.5)
        pyautogui.click()
        time.sleep(10)

        print("Haciendo click en publicar...")
        pos = pyautogui.locateCenterOnScreen('post.png', confidence=0.7)

        if pos:
            pyautogui.moveTo(pos, duration=0.5)
            pyautogui.click(clicks=1)
            print("Chrome encontrado y abierto.")
        else:
            print("No se encontró el icono de Chrome.")
            exit()


        # ============================================
        # FASE 4: LLENADO DE FORMULARIO DE POST
        # ============================================
        estabilidad()
        print("Cambiar a subreddit (click user)...")
        pyautogui.moveTo(730, 330, duration=0.5)
        pyautogui.click()
       
        estabilidad()
        print("Cambiar a subreddit...")
        pyautogui.moveTo(610, 480, duration=0.5)
        pyautogui.click()

        time.sleep(10)          
        print("Escribiendo título...")
        pyautogui.moveTo(610, 530, duration=0.5)
        pyautogui.click()
        pyautogui.write(titulo, interval=0.05)

        estabilidad()
        print("Escribiendo descripción...")
        pyautogui.moveTo(610, 760, duration=0.5)  # Ajusta si cambia el campo
        pyautogui.click()
        pyautogui.write(descripcion, interval=0.03)

        # ============================================
        # FASE 5: PUBLICACIÓN DEL POST
        # ============================================

        print("Haciendo clic en 'Publicar'...")
        pyautogui.moveTo(1300, 905, duration=0.5)  # Ajusta si cambia el botón
        pyautogui.click()
        time.sleep(10)

        print("Publicación completada.")
        enviar_comando_por_email()
        
        for _ in range(360):
            time.sleep(3600)  # Espera 1 HORA
            
def extraer_metricas():
    
    
    # ============================================
    # FASE 1: ACCESO AL PERFIL DE USUARIO
    # ============================================

    print("Esperando carga de la interfaz de Reddit...")
    time.sleep(10)

    print("Haciendo clic en el ícono de perfil...")
    pyautogui.moveTo(1860, 165, duration=0.5)
    pyautogui.click()
    time.sleep(3)

    print("Ingresando al perfil...")
    pyautogui.moveTo(1860, 260, duration=0.5)
    pyautogui.click()
    time.sleep(10)

    # ============================================
    # FASE 2: EXTRACCIÓN DE DATOS DEL PERFIL
    # ============================================

    print("Capturando información general del perfil...")
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    screenshot = pyautogui.screenshot()
    region = (1390, 240, 1780, 780)
    recorte = screenshot.crop(region)
    recorte.save("perfil_datos.png")

    # OCR: extraer texto
    texto = pytesseract.image_to_string(recorte, lang="spa+eng")
    
    # Sustituye 'O' u 'o' solo cuando es un número aislado o tras ':'
    texto = re.sub(r":\s*[Oo]\b", ":0", texto)   # ej: "Participa en: O" -> ":0"
    texto = re.sub(r"\b[Oo]\b", "0", texto)      # ej: "O 1" -> "0 1"

    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    karma = antig = oro = contrib  = "No encontrado"

    for i, l in enumerate(lineas):
        if "karma" in l.lower() and i > 0:
            karma = lineas[i-1]

        if "antig" in l.lower() and i > 0:
            antig = lineas[i-1].replace("d", "").strip()

        if "oro" in l.lower() and "ganado" in l.lower() and i > 0:
            oro = lineas[i-1]

        if "contrib" in l.lower() and i > 0:
            contrib = lineas[i-1]
                
    print(f"Karma:{karma}")
    print(f"Antiguedad en Reddit:{antig}")
    print(f"Oro ganado:{oro}")
    print(f"Contribuciones:{contrib}")

    movimientos_mause()

# ===========================INICIALIZACIÓN GRAFICAS ===========================

# Función auxiliar para pausas entre acciones
def estabilidad():
    time.sleep(2)

def click_USER(event):
    if USER.get() == "USER":
        USER.delete(0, END)

def click_PASS(event):
    if PASS.get() == "PASS":
        PASS.delete(0, END)
        PASS.config(show="*")  

def restaurar_usuario(event):
    if USER.get() == "":
        USER.insert(0, "USER")

def restaurar_contraseña(event):
    if PASS.get() == "":
        PASS.insert(0, "PASS")
        PASS.config(show="")  

def activar_contraseña(event):
    if PASS.get() == "PASS":
        PASS.delete(0, END)
        PASS.config(show="*")
    
ventana = tk.Tk()
automatizar = tk.IntVar()
ventana.geometry("140x111")
ventana.title("Remedy v2")
ventana.resizable(0, 0)

USER = Entry(ventana, font=("Arial", 8), fg="blue")
USER.place(x=10, y=10, height=25, width=120)
USER.insert(0, "USER")

PASS = Entry(ventana, font=("Arial", 8), fg="blue")
PASS.place(x=10, y=40, height=25, width=120)
PASS.insert(0, "PASS")

USER.bind("<Button-1>", click_USER)
USER.bind("<FocusOut>", restaurar_usuario)
PASS.bind("<Button-1>", activar_contraseña)     
PASS.bind("<FocusIn>",  activar_contraseña)      
PASS.bind("<FocusOut>", restaurar_contraseña)   
    

logueo = Button(ventana, text="Logueo", width=14, height=0, command=logueo)
logueo.place(x=10, y=70)
