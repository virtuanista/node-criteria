#!/usr/bin/env python3
"""
Script ejecutable principal para el Generador de Documentación.
Uso: python main.py "término" o python main.py "término1,término2,término3"
"""

import sys
import argparse
import time
from pathlib import Path

# Agregar el directorio src al path para importar el módulo
sys.path.insert(0, str(Path(__file__).parent / "src"))

from doc_generator import DocumentationGenerator
from config import DEFAULT_MODEL

def main():
    """Función principal simplificada."""
    parser = argparse.ArgumentParser(
        description="Generador de Documentación con IA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py "biología"                    # Un término
  python main.py "arte moderno"                # Términos con espacios
  python main.py "biología,física,química"     # Múltiples términos
        """
    )
    
    parser.add_argument(
        "term",
        type=str,
        help="Término para generar documentación (puedes incluir varios términos separados por comas)"
    )
    
    args = parser.parse_args()
    
    # Separar términos por comas y limpiar espacios
    term_list = [term.strip() for term in args.term.split(',') if term.strip()]
    
    if not term_list:
        print("❌ Error: No se proporcionaron términos válidos")
        sys.exit(1)
    
    # Crear instancia del generador (siempre con IA)
    generator = DocumentationGenerator(
        output_dir="output", 
        use_ai=True, 
        model_name=DEFAULT_MODEL
    )
    
    # Mostrar banner
    print("🚀 Generador de Documentación con IA")
    print("=" * 40)
    
    if len(term_list) == 1:
        # Un solo término
        print(f"📝 Término: {term_list[0]}")
        print()
        
        # Generar documentación
        try:
            start_time = time.time()
            file_path = generator.generate_documentation(term_list[0])
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            print(f"\n🎉 ¡Documentación generada!")
            print(f"📄 Archivo: {file_path}")
            print(f"⏱️ Tiempo: {elapsed_time:.2f} segundos")
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        # Múltiples términos
        print(f"📝 Procesando {len(term_list)} términos...")
        print()
        
        generated_files = []
        failed_terms = []
        total_start_time = time.time()
        
        for i, term in enumerate(term_list, 1):
            try:
                print(f"📄 [{i}/{len(term_list)}] Procesando: {term}")
                start_time = time.time()
                file_path = generator.generate_documentation(term)
                end_time = time.time()
                elapsed_time = end_time - start_time
                
                generated_files.append(file_path)
                print(f"✅ Completado: {term} ({elapsed_time:.2f}s)")
                print()
            except Exception as e:
                print(f"❌ Error con '{term}': {e}")
                failed_terms.append(term)
                print()
        
        total_end_time = time.time()
        total_elapsed_time = total_end_time - total_start_time
        
        # Resumen final
        print("🎉 RESUMEN FINAL")
        print("=" * 40)
        print(f"✅ Archivos generados: {len(generated_files)}")
        for file_path in generated_files:
            print(f"   📄 {Path(file_path).name}")
        
        if failed_terms:
            print(f"❌ Errores en: {len(failed_terms)}")
            for term in failed_terms:
                print(f"   💥 {term}")
        
        print(f"⏱️ Tiempo total: {total_elapsed_time:.2f} segundos")
        
        if failed_terms:
            sys.exit(1)

if __name__ == "__main__":
    main()