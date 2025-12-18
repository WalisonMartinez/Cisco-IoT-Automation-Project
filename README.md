#  Smart Home Security Infrastructure: Cisco & Python Automation

Este proyecto integra el diseño de una red segura para una casa inteligente (Smart Home) utilizando segmentación por VLANs y un sistema de monitoreo automatizado desarrollado en Python.

##  Descripción General
El objetivo principal fue aislar el tráfico de los dispositivos de la familia de los dispositivos IoT (Cámaras de seguridad) para reducir la superficie de ataque, utilizando una arquitectura **Router-on-a-Stick**.

##  Estructura del Repositorio
* `/network_design`: Contiene el archivo `.pkt` (Cisco Packet Tracer) con la topología lógica.
* `/automation_tools`: Script `.py` de monitoreo de disponibilidad.
* `/assets/img`: Evidencia técnica del funcionamiento.

##  Guía de Evidencia Técnica
He documentado el proceso con capturas de pantalla para validar cada etapa de la implementación:

1. **`01_network_topology.png`**: Muestra la arquitectura física y lógica. Aquí se observa la convergencia de red (puntos verdes) entre la PC, el Switch y el Router.
![Topología de Red](assets/img/01_network_topology.png)

2. **`02_router_l3_interfaces.png`**: Resultado del comando `show ip interface brief`. Es la prueba de que las sub-interfaces virtuales (dot1Q) están activas y con sus IPs asignadas correctamente.
![Interfaces del Router](assets/img/02_router_l3_interfaces.png)

3. **`03_switch_trunk_config.png`**: Registro de los comandos CLI utilizados para crear las VLANs (10 y 50) y configurar el enlace Troncal (Trunk), permitiendo el paso de múltiples etiquetas de red por un solo cable.
![Configuración del Switch](assets/img/03_switch_trunk_config.png)

4. **`04_intervlan_ping_success.png`**: Prueba reina de conectividad ICMP. Muestra cómo la PC (VLAN 10) logra comunicarse exitosamente con la Cámara (VLAN 50) a través del Router.
![Prueba de Ping Exitosa](assets/img/04_intervlan_ping_success.png)

5. **`05_python_monitor_alert.png`**: Demostración de la lógica de automatización. El script detecta cuando un dispositivo se desconecta, enviando una alerta de seguridad inmediata. 
![Script de Monitoreo Python](assets/img/05_python_monitor_alert.png)
> **NOTA**: En la captura del script use mi consola real, por esta razón da el mensaje de alerta (al no detectar la red virtual de Cisco). Para detener el script usa `Ctrl + C`.

##  ¿Qué aprendí en este proyecto?
* **Troubleshooting Proactivo:** Aprendí a leer los errores de la consola (CLI) de Cisco para corregir fallos de sintaxis y de enrutamiento.
* **Integración NetDevOps:** Logré unir el mundo de las redes con la programación en Python para automatizar tareas de vigilancia.

##  Notas para implementación
Si deseas replicar este proyecto, toma en cuenta lo siguiente:
* **Versión de Software:** Se recomienda utilizar Cisco Packet Tracer 8.0 o superior.
* **Módulos IoT:** Algunas cámaras en Packet Tracer requieren cambiar la tarjeta de red (NIC) a una de tipo **FastEthernet** en la pestaña de configuración avanzada para aceptar cables de cobre.
* **Gateway:** Asegúrate de que el "Default Gateway" en los dispositivos finales coincida exactamente con la IP de la sub-interfaz del Router.
