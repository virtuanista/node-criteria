#!/usr/bin/env python3
"""
Generador de Documentación Estructurada
=======================================

Este módulo permite generar documentación estructurada sobre cualquier término
especificado por el usuario, creando un archivo markdown con formato estándar.
"""

import sys
from pathlib import Path
from datetime import datetime

# Importar configuración
sys.path.append(str(Path(__file__).parent.parent))
from config import OUTPUT_DIR, DEFAULT_MODEL

# Importar el enhancer de contenido
try:
    from content_enhancer import ContentEnhancer
    AI_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Módulos de IA no disponibles: {e}")
    print("📝 Usando modo básico.")
    AI_AVAILABLE = False

class DocumentationGenerator:
    """
    Generador de documentación estructurada en formato markdown.
    
    Crea un archivo .md con estructura estándar para cualquier término.
    """
    
    def __init__(self, output_dir: str = None, use_ai: bool = True, model_name: str = None):
        """
        Inicializa el generador de documentación.
        
        Args:
            output_dir (str): Directorio donde se guardarán los archivos
            use_ai (bool): Si usar IA (Ollama + Wikipedia) para mejorar el contenido
            model_name (str): Nombre del modelo de Ollama a utilizar
        """
        self.output_dir = Path(output_dir or OUTPUT_DIR)
        self.output_dir.mkdir(exist_ok=True)
        self.use_ai = use_ai and AI_AVAILABLE
        self.model_name = model_name or DEFAULT_MODEL
        
        # Inicializar el enhancer de contenido si está disponible
        self.enhancer = None
        if self.use_ai:
            try:
                self.enhancer = ContentEnhancer(self.model_name)
                print(f"🤖 Modo IA activado con modelo: {self.model_name}")
            except Exception as e:
                print(f"⚠️ Error inicializando IA: {e}")
                print("📝 Continuando en modo básico...")
                self.use_ai = False
        
        if not self.use_ai:
            print("📝 Usando modo básico (plantillas estáticas)")
    
    def generate_documentation(self, term: str) -> str:
        """
        Genera la documentación completa para un término en un solo archivo.
        
        Args:
            term (str): Término sobre el cual generar la documentación
            
        Returns:
            str: Ruta del archivo creado
        """
        # Crear nombre de archivo limpio
        filename = f"{term.lower().replace(' ', '_')}.md"
        file_path = self.output_dir / filename
        
        print(f"📁 Creando documentación para: {term}")
        print(f"📄 Archivo: {file_path}")
        
        # Generar contenido completo
        content = self._generate_complete_document(term)
        
        # Escribir archivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"🎉 Documentación completa generada en: {file_path}")
        
        return str(file_path)
    
    def _generate_complete_document(self, term: str) -> str:
        """
        Genera el documento completo con la estructura estándar.
        
        Args:
            term (str): Término para generar la documentación
            
        Returns:
            str: Contenido completo del documento
        """
        if self.use_ai and self.enhancer:
            try:
                print("🤖 Generando contenido con IA...")
                return self.enhancer.enhance_summary(term)
            except Exception as e:
                print(f"⚠️ Error con IA, usando plantilla básica: {e}")
        
        # Plantilla básica de respaldo
        return self._get_basic_template(term)
    
    def _get_basic_template(self, term: str) -> str:
        """
        Genera plantilla básica con la estructura estándar.
        
        Args:
            term (str): Término para personalizar la plantilla
            
        Returns:
            str: Contenido de la plantilla básica
        """
        return f"""# {term.title()}

## Definición inicial y concisa
{term.title()} es un concepto que se define como [definición breve y clara del término]. Este concepto es relevante en su campo debido a [razón de importancia].

## Características principales
• **Característica 1:** [Descripción de la primera característica principal]
• **Característica 2:** [Descripción de la segunda característica principal]
• **Característica 3:** [Descripción de la tercera característica principal]
• **Característica 4:** [Descripción de la cuarta característica principal]

## Ejemplos concretos
1. **Ejemplo práctico 1:** [Descripción detallada del primer ejemplo]
2. **Ejemplo práctico 2:** [Descripción detallada del segundo ejemplo]
3. **Ejemplo práctico 3:** [Descripción detallada del tercer ejemplo]

## Diferenciación y aclaración

### {term.title()} vs. [Concepto relacionado]
[Explicación de las diferencias principales entre ambos conceptos]

### Límites
• [Limitación o aspecto que no abarca {term}]
• [Otra limitación importante]
• [Qué NO es {term}]

---
*Documento generado automáticamente el {datetime.now().strftime("%d/%m/%Y")} usando {'IA' if self.use_ai else 'plantillas básicas'}*
"""

def main():
    """Función principal para testing."""
    print("🚀 Generador de Documentación Estructurada")
    print("=" * 50)
    
    generator = DocumentationGenerator()
    
    term = input("📝 Introduce el término: ").strip()
    if term:
        try:
            file_path = generator.generate_documentation(term)
            print(f"\n🎉 ¡Documentación generada!")
            print(f"📄 Archivo: {file_path}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
