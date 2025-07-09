# 📚 Explicar un concepto con un modelo local y guardarlo markdown

Genera una explicación profesional y estructurada sobre cualquier término o concepto en formato markdown, utilizando únicamente modelos de inteligencia artificial locales. El sistema no depende de servicios externos: el contenido es generado por IA, aportando una plantilla clara y homogénea del propio concepto como resultado final. Ideal para herramientas como Obsidian.

## ✨ Características principales

- 🤖 **IA local**: Utiliza modelos Ollama (por defecto: gemma3:latest, configurable)
- 📄 **Formato estructurado**: Documentos Markdown con secciones académicas y emojis temáticos
- ⚡ **Procesamiento múltiple**: Genera documentación para uno o varios términos en una sola ejecución
- ⏱️ **Medición de tiempo**: Muestra tiempos de generación por término y total
- 📝 **Sin dependencias externas**: No requiere conexión a internet para generar el contenido, solamente ollama y un modelo.

## 📋 Estructura de los documentos generados

Cada archivo `.md` sigue una plantilla profesional y homogénea:

1. **📖 Definición**: Definición académica y clara
2. **🔍 Características principales**: 4 aspectos fundamentales
3. **📂 Clasificación y tipos**: Ramas y subdisciplinas
4. **🎯 Aplicaciones y métodos**: Métodos y aplicaciones prácticas
5. **🔗 Conceptos relacionados**: Términos y relaciones clave
6. **💡 Resumen**: Síntesis y puntos destacados

**Formato:**

- Markdown profesional, con emojis solo en encabezados
- Texto limpio, sin referencias ni símbolos extraños
- Metadatos: fecha y etiqueta de IA

## 🛠️ Requisitos del sistema

- **Python 3.8+**
- **Ollama** instalado y ejecutándose localmente (Ollama es imprescindible para realizar inferencia sobre un modelo descargado)
- Al menos un modelo descargado en Ollama (por defecto: gemma3:latest)

## 📦 Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd node-criteria
```

### 2. Instalar dependencias de Python

```bash
pip install -r requirements.txt
```

### 3. Instalar y configurar Ollama

Ollama es imprescindible para poder ejecutar modelos de IA locales y realizar inferencia. Si no tienes Ollama:

1. Descárgalo desde [ollama.ai](https://ollama.ai) e instálalo en tu sistema.
2. Si necesitas ayuda, sigue este tutorial paso a paso para Windows: [Guía de instalación de Ollama](https://www.geeknetic.es/Guia/2957/Ollama-Como-usar-LLM-de-IA-locales-desde-Windows.html)
3. Descarga al menos un modelo compatible (por ejemplo):

```bash
ollama pull gemma3:latest
```

### 4. Verificar instalación

```bash
ollama list
```

## 🚀 Uso

### Uso básico - Un concepto

```bash
python main.py "tu concepto"
```

### Varios conceptos a la vez

```bash
python main.py "un concepto, otro concepto, otro concepto más"
```

### Ejemplos de términos probados:

- **Científicos**: `apoptosis`, `criptografía`, `inteligencia artificial`
- **Políticos**: `liberalismo`, `democracia`
- **Tecnológicos**: `blockchain`, `fotografía digital`
- **Psicológicos**: `narcisismo`, `empatía`

## ⚙️ Configuración

Puedes cambiar el modelo de IA por defecto editando `config.py`:

```python
DEFAULT_MODEL = "gemma3:latest"  # Modelo por defecto
# DEFAULT_MODEL = "phi3:mini"
# DEFAULT_MODEL = "gemma:2b-instruct-q2_K"
```

El directorio de salida también es configurable:

```python
OUTPUT_DIR = "output"
```

## 📁 Estructura del proyecto

```
node-criteria/
├── main.py              # Script principal ejecutable
├── config.py            # Configuración del sistema
├── requirements.txt     # Dependencias de Python
├── README.md            # Este archivo
├── src/                 # Código fuente
│   ├── doc_generator.py      # Generador principal
│   └── content_enhancer.py   # Integración IA
└── output/              # Documentos generados (.md)
```

## 📊 Rendimiento

El tiempo de generación depende del modelo, el hardware y la longitud de la respuesta. En mi equipo, los tiempos estimados son:

- **Términos científicos**: 90-180 segundos
- **Términos generales**: 60-120 segundos

**Nota:** El rendimiento real puede variar significativamente según la máquina y los recursos disponibles de cada usuario.

**Factores:**

- 🖥️ CPU/RAM disponible
- 🤖 Modelo de IA elegido

## 🎯 Ejemplo de salida

```bash
🚀 Generador de Documentación con IA
========================================
📝 Término: apoptosis

📁 Creando documentación para: apoptosis
📄 Archivo: output\apoptosis.md
🤖 Generando contenido con IA...
✅ Conexión con IA establecida - Modelo: gemma3:latest
🤖 Generando contenido con gemma3:latest...
✅ Contenido generado exitosamente (6321 caracteres)
🎉 Documentación completa generada en: output\apoptosis.md

🎉 ¡Documentación generada!
📄 Archivo: output\apoptosis.md
⏱️ Tiempo: 120.60 segundos
```

## 🛠️ Desarrollo

### Clases principales

- `DocumentationGenerator`: Genera y guarda la documentación en formato markdown
- `ContentEnhancer`: Interfaz con Ollama para generación de contenido con IA

### Personalización del estilo de la respuesta

Si deseas modificar el estilo, la estructura o el tono de las respuestas generadas, puedes hacerlo editando el prompt en el archivo:

- `src/content_enhancer.py` → método `enhance_summary()`

Allí puedes ajustar la plantilla, los encabezados, la longitud, el nivel de detalle o cualquier instrucción para el modelo de IA según tus preferencias.

### Agregar nuevos modelos

1. Descargar con Ollama: `ollama pull <modelo>`
2. Añadir el nombre del modelo que se quiere usar en `config.py`
3. Ejecutar el script con el modelo deseado

## 🔧 Solución de Problemas

### Error: "Error conectando con Ollama"

```bash
# Verifica que Ollama esté ejecutándose
ollama list
# Si no está ejecutándose, inicia el servicio:
ollama serve
```

### Error: "Módulos de IA no disponibles"

```bash
pip install -r requirements.txt
```

### Documentos vacíos o incompletos

- Ollama debe estar en funcionamiento
- Prueba con otro modelo
- Revisa que el modelo esté completamente descargado

## 🙏 Agradecimientos

- **Ollama** por la infraestructura de modelos e inferencia
- **Microsoft Phi-3** y **Google Gemma** por los modelos de IA
- Comunidad open-source por las librerías utilizadas

---

## LICENSE

<p align="center">
    Repositorio generado por <a href="https://github.com/virtuanista" target="_blank">virtu 🎣</a>
</p>

<p align="center">
    <img src="https://open.soniditos.com/cat_footer.svg" />
</p>

<p align="center">
    Copyright © 2025
</p>

<p align="center">
    <a href="/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>

*Generado con ❤️ para crear documentación usando IA local*
