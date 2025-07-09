"""
Módulo de integración con modelos de IA
======================================

Este módulo maneja la comunicación con modelos de IA locales
para generar contenido estructurado y documentación de calidad.
"""

# Importar configuración
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import DEFAULT_MODEL, DOC_FOOTER_AI_LABEL

import ollama
from datetime import datetime
import re
from typing import Dict

class ContentEnhancer:
    """
    Clase que mejora el contenido usando modelos de IA locales.
    
    Esta clase se encarga de usar modelos de IA local para generar 
    contenido estructurado y documentación de calidad.
    """
    
    def __init__(self, model_name: str = None):
        """
        Inicializa el enhancer de contenido.
        
        Args:
            model_name (str): Nombre del modelo de IA a utilizar
        """
        self.model_name = model_name or DEFAULT_MODEL
        self.connection_verified = False
    
    def _check_ollama_connection(self) -> bool:
        """
        Verifica la conexión con el servicio de IA y la disponibilidad del modelo.
        
        Returns:
            bool: True si la conexión es exitosa
        """
        try:
            models = ollama.list()
            # Si la respuesta es un objeto con atributo 'models', usarlo; si es lista, usar directamente
            if hasattr(models, 'models'):
                model_list = models.models
            elif isinstance(models, dict) and 'models' in models:
                model_list = models['models']
            elif isinstance(models, list):
                model_list = models
            else:
                print(f"❌ Respuesta inesperada de ollama.list(): {models}")
                return False

            # Obtener nombres de modelos según la estructura
            available_models = []
            for model in model_list:
                # Puede ser objeto con atributo 'model', o dict con clave 'model', o 'name'
                if hasattr(model, 'model'):
                    available_models.append(model.model)
                elif isinstance(model, dict) and 'model' in model:
                    available_models.append(model['model'])
                elif isinstance(model, dict) and 'name' in model:
                    available_models.append(model['name'])
                else:
                    available_models.append(str(model))

            if self.model_name not in available_models:
                print(f"⚠️ Advertencia: El modelo {self.model_name} no está disponible")
                print(f"📋 Modelos disponibles: {', '.join(available_models)}")
                return False

            print(f"✅ Conexión con IA establecida - Modelo: {self.model_name}")
            return True

        except Exception as e:
            print(f"❌ Error conectando con el servicio de IA: {e}")
            print("💡 Asegúrate de que el servicio de IA esté ejecutándose")
            return False
    
    def generate_content_with_ai(self, prompt: str) -> str:
        """
        Genera contenido usando el modelo de IA.
        
        Args:
            prompt (str): Prompt para el modelo
            
        Returns:
            str: Contenido generado por el modelo
        """
        try:
            # Verificar conexión solo cuando sea necesario
            if not self.connection_verified:
                if not self._check_ollama_connection():
                    return f"Error: No se pudo conectar con el servicio de IA"
                self.connection_verified = True
            
            print(f"🤖 Generando contenido con {self.model_name}...")
            
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )
            
            content = response['message']['content']
            print(f"✅ Contenido generado exitosamente ({len(content)} caracteres)")
            return content
            
        except Exception as e:
            print(f"❌ Error generando contenido con IA: {e}")
            return f"Error al generar contenido: {e}"
    
    def enhance_summary(self, term: str) -> str:
        """
        Genera un resumen mejorado usando solo IA.
        
        Args:
            term (str): Término para el resumen
            
        Returns:
            str: Resumen mejorado
        """
        prompt = f"""
        Eres un experto en documentación académica. Crea un documento completo y profesional sobre "{term}".

        INSTRUCCIONES ESTRICTAS:
        - NUNCA uses referencias como [1], [2], [3], ✅, etc.
        - NO agregues símbolos extraños
        - Usa solo texto limpio en español
        - Respeta EXACTAMENTE la estructura que te doy
        - NO añadas contenido extra al final
        - Basa el contenido en tu conocimiento, sé preciso y académico

        FORMATO OBLIGATORIO:

        # {term.title()}

        ## 📖 Definición
        [Definición clara y académica en 1-2 líneas, SIN referencias]

        ## 🔍 Características principales
        - **Aspecto 1**: Descripción específica y detallada
        - **Aspecto 2**: Descripción específica y detallada
        - **Aspecto 3**: Descripción específica y detallada
        - **Aspecto 4**: Descripción específica y detallada

        ## 📂 Clasificación y tipos
        ### Ramas principales
        1. **Rama 1**: Descripción académica
        2. **Rama 2**: Descripción académica
        3. **Rama 3**: Descripción académica

        ### Subdisciplinas
        - Disciplina 1: Enfoque específico
        - Disciplina 2: Enfoque específico
        - Disciplina 3: Enfoque específico

        ## 🎯 Aplicaciones y métodos
        ### Métodos de estudio
        - **Método 1**: Descripción técnica detallada
        - **Método 2**: Descripción técnica detallada
        - **Método 3**: Descripción técnica detallada

        ### Aplicaciones prácticas
        - Aplicación 1: Contexto específico y real
        - Aplicación 2: Contexto específico y real
        - Aplicación 3: Contexto específico y real

        ## 🔗 Conceptos relacionados
        - **Concepto 1**: Relación específica con {term}
        - **Concepto 2**: Relación específica con {term}
        - **Concepto 3**: Relación específica con {term}

        ## 💡 Resumen
        > **En síntesis**: Resumen académico en 1-2 líneas

        **Puntos clave:**
        - Punto destacado 1 (específico y relevante)
        - Punto destacado 2 (específico y relevante)
        - Punto destacado 3 (específico y relevante)

        ---
        **📅**: {datetime.now().strftime("%d/%m/%Y")} | **🤖**: {DOC_FOOTER_AI_LABEL}

        IMPORTANTE:
        - USA tu conocimiento académico y científico
        - NO uses NINGUNA referencia [1][2][3] ni símbolos ✅
        - Mantén los emojis SOLO en headers (##)
        - Completa TODAS las secciones con contenido real
        - Sé específico, preciso y académico
        - Termina EXACTAMENTE en el footer, no agregues nada más
        """
        
        return self.generate_content_with_ai(prompt)

# Funciones de utilidad
def clean_ai_content(content: str) -> str:
    """
    Limpia y formatea el contenido generado por IA.
    
    Args:
        content (str): Contenido original
        
    Returns:
        str: Contenido limpio y formateado
    """
    # Remover caracteres problemáticos
    content = re.sub(r'\*\*\*+', '**', content)  # Normalizar negritas
    content = re.sub(r'\n{3,}', '\n\n', content)  # Normalizar saltos de línea
    
    # Asegurar formato markdown correcto
    content = re.sub(r'^#+ ', '# ', content, flags=re.MULTILINE)  # Normalizar headers
    
    return content.strip()

def test_connection(model_name: str = None) -> bool:
    """
    Prueba la conexión con el servicio de IA.
    
    Args:
        model_name (str): Nombre del modelo a probar
        
    Returns:
        bool: True si la conexión es exitosa
    """
    try:
        enhancer = ContentEnhancer(model_name)
        return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False
