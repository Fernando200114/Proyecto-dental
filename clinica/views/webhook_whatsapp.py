# clinica/views/webhook_whatsapp.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from clinica.models.pacientes import Pacientes
from clinica.models.citas import Citas
import re
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse


# Decorador para permitir recibir POST de servicios externos (Twilio)
@csrf_exempt
def whatsapp_webhook(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    # Twilio envía los datos en POST
    numero = request.POST.get("From", "")  # viene con formato "whatsapp:+593988825960"
    mensaje = request.POST.get("Body", "")

    # Limpiamos el número
   # Limpiamos el número
    numero = numero.replace("whatsapp:", "")

    # convertir formato internacional a formato Ecuador
    if numero.startswith("+593"):
        numero = "0" + numero[4:]

    # Buscar paciente por número
 
    # Buscar paciente por número
    try:
        paciente = Pacientes.objects.get(telefono=numero)
    except Pacientes.DoesNotExist:
        return JsonResponse({"error": "Paciente no encontrado. Regístrese primero."})

    # --------------------------
    # PARSING DEL MENSAJE
    # Ejemplo esperado: "Cita 12/03/2026 15:30 Motivo: Consulta general"
    # --------------------------
    fecha = None
    hora = None
    motivo = "Consulta general"  # default si no lo ponen
    estado = "Pendiente"  # default siempre al crear desde WhatsApp

    # Buscar fecha en formato DD/MM/YYYY
    fecha_match = re.search(r"(\d{2}/\d{2}/\d{4})", mensaje)
    if fecha_match:
        fecha_str = fecha_match.group(1)
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            return JsonResponse({"error": "Formato de fecha incorrecto. Use DD/MM/YYYY."})

    # Buscar hora en formato HH:MM
    hora_match = re.search(r"(\d{1,2}:\d{2})", mensaje)
    if hora_match:
        hora_str = hora_match.group(1)
        try:
            hora = datetime.strptime(hora_str, "%H:%M").time()
        except ValueError:
            return JsonResponse({"error": "Formato de hora incorrecto. Use HH:MM."})

    # Buscar motivo después de "Motivo:" o "motivo:"
    motivo_match = re.search(r"[Mm]otivo: (.+)", mensaje)
    if motivo_match:
        motivo = motivo_match.group(1).strip()

    # --------------------------
    # CREAR LA CITA
    # --------------------------
    if not fecha or not hora:
        return JsonResponse({"error": "Debes incluir fecha y hora en el mensaje."})

    # Validación de cita única por fecha y hora
    if Citas.objects.filter(fecha=fecha, hora=hora).exists():
        return JsonResponse({"error": "Ya existe una cita en esa fecha y hora."})

    cita = Citas.objects.create(
        paciente=paciente,
        fecha=fecha,
        hora=hora,
        motivo=motivo,
        estado=estado
    )

    # Respuesta de confirmación
    respuesta = f"Hola {paciente.nombre}, tu cita ha sido agendada para el {fecha.strftime('%d/%m/%Y')} a las {hora.strftime('%H:%M')}. Estado: {estado}"

    resp = MessagingResponse()
    resp.message(respuesta)

    return HttpResponse(str(resp), content_type="application/xml")