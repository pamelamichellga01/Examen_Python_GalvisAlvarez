# 🍽️ Simulador de Propina en Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Calificación](https://img.shields.io/badge/Calificación-98%2F100-brightgreen)

## 📚 Tabla de Contenidos

1. [Descripción del Proyecto](#-descripción)
2. [Instalación](#-instalación)
3. [Uso del Proyecto](#-uso)
4. [Estructura del Código](#-estructura-del-código)
5. [Autores y Contribuciones](#-autores)
6. [Calificación Obtenida](#-calificación)

---

## 📋 Descripción

Aplicación de consola que calcula automáticamente:

- Monto de propina (10%, 15%, 20% o personalizado)
- Total a pagar (cuenta + propina)
- División equitativa entre comensales

**Funcionalidades clave:**

```python
def calcular_propina(total, porcentaje):
    """Calcula $7.50 para $50 con 15%"""
    return total * (porcentaje / 100)
```

---

## 🛠️ Instalación

### Requisitos

- Python 3.10+

### Pasos:

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/Examen_Python_GalvisPamela.git
cd Examen_Python_GalvisPamela
```

2. Ejecutar el programa:

```bash
python main.py
```

---

## 🚀 Uso del Proyecto

1. Ingresar el monto de la cuenta.
2. Seleccionar el porcentaje de propina (o introducir uno personalizado).
3. Visualizar propina, total a pagar y monto por persona (si se divide).

### Ejemplo de flujo

- Monto de cuenta: `$50`
- Propina: `15%`
- Propina calculada: `$7.50`
- Total: `$57.50`
- División entre 4: `$14.38` por persona

---

## 🧩 Estructura del Código

```python
calcular_propina(total, porcentaje)
# Entrada: monto total y porcentaje
# Salida: propina

calcular_total_con_propina(total, propina)
# Entrada: total y propina
# Salida: total a pagar

dividir_total(total, personas)
# Entrada: total y cantidad de personas
# Salida: pago por persona

mostrar_resultados(propina, total, total_persona)
# Entrada: propina, total, por persona
# Salida: impresión en consola
```

Menú interactivo: [Ver diseño del menú](https://gist.github.com/programmersland/3c53a84bcc2c3c1e661856238a9edba0)

---

## 👨‍💻 Autores y Contribuciones

**Docente**: Cristian Díaz  
**Estudiante**: Pamela Galvis  
Repositorio: [Examen_Python_GalvisAlvarez](https://github.com/pamelamichellga01/Examen_Python_GalvisAlvarez)

---

## 🏆 Calificación

**Calificación obtenida**: 98/100  
**Comentarios del docente**:

- Excelente dominio del proyecto.
- Funciones claras, validadas y explicadas.
- Código documentado y limpio.
- Menú funcional y validaciones bien hechas.
