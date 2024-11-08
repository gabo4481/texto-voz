import dearpygui.dearpygui as dpg
import pyttsx3

# Inicialización de pyttsx3
engine = pyttsx3.init()
contenido = ""
voices = engine.getProperty('voices')
opciones_voices = {index: voice.name for index, voice in enumerate(voices)}

# Funciones
def leer_archivo(sender, app_data):
    ruta_archivo = app_data['file_path_name']
    try:
        with open(ruta_archivo, 'r') as file:
            contenido = file.read()
            dpg.set_value("texto_archivo", contenido)
            dpg.set_value("cantidad_caracteres",len(contenido))
            dpg.set_value("cantidad_palabras",len(contenido.split()))
    except Exception as e:
        print("Error al abrir el archivo:", e)

def texto_voz():
    contenido = dpg.get_value("texto_archivo")
    voz_seleccionada = dpg.get_value("combo_voces")
    velocidad = dpg.get_value("slider_velocidad")
    volumen = dpg.get_value("slider_volumen")
    
    # Obtener el índice de la voz seleccionada en el combo box
    voz_index = next((index for index, voice in opciones_voices.items() if voice == voz_seleccionada), None)
    
    if len(contenido) > 0 and voz_index is not None:
        # Configuración de velocidad, volumen y voz
        engine.setProperty('rate', velocidad)
        engine.setProperty('volume', volumen)
        engine.setProperty('voice', voices[voz_index].id)  
        
        # Guardar en archivo y reproducir
        engine.save_to_file(contenido, "output_file.mp3")
        engine.runAndWait()
        
        # Mostrar popup de éxito
        dpg.set_value("texto_popup", "Conversion realizada con exito")
        dpg.configure_item("popup_id", show=True)
    else:
        dpg.set_value("texto_popup", "Por favor carga un archivo de texto y elige una voz.")
        dpg.configure_item("popup_id", show=True)


def prueba_voz(sender, app_data):
    
    # Obtencion de valores velocidad, volumen y voz
    voz_seleccionada = dpg.get_value("combo_voces")
    velocidad = dpg.get_value("slider_velocidad")
    volumen = dpg.get_value("slider_volumen")

    voz_index = next((index for index, voice in opciones_voices.items() if voice == voz_seleccionada), None)
    
    if voz_index is not None:
        # Configuración de velocidad, volumen y voz
        engine.setProperty('rate', velocidad)
        engine.setProperty('volume', volumen)  
        engine.setProperty('voice', voices[voz_index].id)  # Usar el ID de la voz seleccionada
        engine.say(dpg.get_value("texto_archivo"))
        engine.runAndWait()
    else:
        dpg.set_value("texto_popup","Voz no encontrada en la lista...")
        dpg.configure_item("popup_id", show=True)

# Configuración de interfaz de DearPyGui
dpg.create_context()
with dpg.theme(tag="tema_sliders"):
    with dpg.theme_component(dpg.mvSliderInt):
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (255, 255, 255))  # Color del grab
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (138, 43, 226))  # Color del grab activo
    with dpg.theme_component(dpg.mvSliderFloat):
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (255, 255, 255))  # Color del grab
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (138, 43, 226))  # Color del grab activo

with dpg.window(label="Convertir Texto a Voz",tag="principal", width=800, height=600,):
    dpg.add_separator(label="Contenido del archivo")
    with dpg.group(width=745,indent=20):
        dpg.add_input_text(tag="texto_archivo", multiline=True, readonly=True, height=200)

    dpg.add_separator(label="Configuraciones de Voz")
    with dpg.group(indent=20):
        dpg.add_slider_int(tag="slider_velocidad", label="Velocidad", default_value=125, min_value=100, max_value=300)
        dpg.bind_item_theme(dpg.last_item(), "tema_sliders")
        dpg.add_slider_float(tag="slider_volumen", label="Volumen", default_value=0.8, min_value=0.0, max_value=1.0)
        dpg.bind_item_theme(dpg.last_item(), "tema_sliders")
        dpg.add_combo(items=list(opciones_voices.values()), label="Listado de Voces", tag="combo_voces")
    
    dpg.add_separator(label="Estadisticas")
    with dpg.group(label="Estadisticas",tag="Estadisticas",horizontal=True,horizontal_spacing=50,width=730,indent=20):    
        with dpg.group(horizontal=True):
            dpg.add_text("Cantidad De Caracteres: ")
            dpg.add_text(label="cantidad_caracteres",tag="cantidad_caracteres",default_value=0)
        with dpg.group( horizontal=True):
            dpg.add_text("Cantidad De Palabras:")
            dpg.add_text(label="cantidad_palabras",tag="cantidad_palabras",default_value=0)

    dpg.add_separator(label="Acciones")
    with dpg.group(tag="Acciones",horizontal=True,horizontal_spacing=40,width=200,height=40,indent=50):
        with dpg.theme(tag="tema_boton_cargar"):
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button,(255, 0, 0, 128))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(255, 0, 0,50))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 0, 0, 255))
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 24)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3, 3)
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 8)  # gap
                dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5 )
                with dpg.theme(tag="tema_boton_prueba"):
                    with dpg.theme_component(dpg.mvButton):
                        dpg.add_theme_color(dpg.mvThemeCol_Button, (10, 56, 113) )  # background-color
                        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (138, 43, 226) )  # hover background-color
                        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (138, 43, 226) )  # active background-color
                        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255) )  # color
                        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 24 )  # border-radius
                        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3,3)  # padding
                        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 8)  # gap
                        dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5 )  # text-align
                    with dpg.theme(tag="tema_boton_convertir"):
                        with dpg.theme_component(dpg.mvButton):
                            dpg.add_theme_color(dpg.mvThemeCol_Button, (216, 223, 232))  # background-color
                            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (138, 43, 226))  # hover background-color
                            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (138, 43, 226))  # active background-color
                            dpg.add_theme_color(dpg.mvThemeCol_Text, (10, 56, 113))  # color
                            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 24)  # border-radius
                            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3, 3)  # padding
                            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 8)  # gap
                            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0.5, 0.5)  # text-align
                        
        dpg.add_button(label="Convertir", callback=texto_voz)
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_convertir")
        dpg.add_button(label="Probar Voz", callback=prueba_voz)
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_prueba")
        dpg.add_button(label="Cargar texto", callback=lambda: dpg.show_item("cargar_texto_id"))
        dpg.bind_item_theme(dpg.last_item(), "tema_boton_cargar")
        
    

with dpg.file_dialog(directory_selector=False, show=False, modal=True, callback=leer_archivo, tag="cargar_texto_id", width=600, height=400):
    dpg.add_file_extension(".txt", color=(0, 255, 0, 255))

with dpg.window(label="Estatus de Conversión", autosize=True, show=False, modal=True, tag="popup_id"):
    dpg.add_text(default_value="Conversión Completada con Éxito.",tag="texto_popup")
    dpg.add_button(label="Cerrar", callback=lambda: dpg.configure_item("popup_id", show=False))

# Configuración final
dpg.create_viewport(title="Conversor texto a voz",width=816,height=600,x_pos=250,y_pos=100)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
