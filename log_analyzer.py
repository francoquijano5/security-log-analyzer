import re
from collections import Counter

# Simulamos un archivo de log de servidor (en un caso real, leerías un archivo .log)
log_data = """
2026-01-16 10:05:20 - IP: 192.168.1.5 - Login Failed - User: admin
2026-01-16 10:05:22 - IP: 192.168.1.5 - Login Failed - User: root
2026-01-16 10:05:25 - IP: 192.168.1.5 - Login Failed - User: support
2026-01-16 10:06:01 - IP: 45.23.12.1 - Login Success - User: franco
2026-01-16 10:07:12 - IP: 192.168.1.5 - Login Failed - User: guest
2026-01-16 10:08:45 - IP: 88.12.34.56 - Login Failed - User: admin
"""

def analyze_logs(data):
    print("--- 🛡️ Reporte de Seguridad de Logs ---")
    
    # Buscamos todas las IPs que tuvieron fallos de login
    failed_attempts = re.findall(r"IP: ([\d\.]+) - Login Failed", data)
    
    # Contamos intentos por IP
    ip_counts = Counter(failed_attempts)
    
    # Umbral de alerta (más de 3 intentos fallidos)
    threshold = 3
    
    for ip, count in ip_counts.items():
        status = "🚨 ALERTA: Posible Fuerza Bruta" if count >= threshold else "⚠️ Sospechoso"
        print(f"IP: {ip} | Intentos fallidos: {count} | Estado: {status}")

if _name_ == "_main_":
    analyze_logs(log_data)
