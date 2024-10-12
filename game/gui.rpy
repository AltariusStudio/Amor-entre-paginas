################################################################################
## Inicialización
################################################################################

## La sentencia 'init offset' da preferencia a las sentencias de inicialización
## de este archivo respecto a otros archivos.
init offset = -2

## Llamando 'qui.init' se resetean los estilos a los valores por defecto y se
## establecen la anchura y altura del juego.
init python:
    gui.init(3840, 2160)

## Habilitar comprobaciones de propiedades no válidas o inestables en pantallas
## o transformaciones.
define config.check_conflicting_properties = True


################################################################################
## Variables de configuración de la interfaz.
################################################################################


## Colores #####################################################################
##
## Los colores del texto de la interfaz

## El color enfatizado usado en la interfaz para subrayar texto.
define gui.accent_color = '#9011f8'

## El color del botón de texto cuando no está seleccionado ni enfocado.
define gui.idle_color = '#9409d4'

## El color 'small' se usa para el texto pequeño, que necesita destacar más.
define gui.idle_small_color = '#9e9d9e'

## El color usado en botones y barras que ganan foco.
define gui.hover_color = '#8412f7'

## El color del botón de texto seleccionado pero no enfocado. Un botón está
## seleccionado si indica el valor actual de la pantalla o preferencia.
define gui.selected_color = '#a23cf5'

## El color de los botones de texto que no pueden ser seleccionados.
define gui.insensitive_color = '#8888887f'

## Colores de la parte vacía de las barras. No se usan directamente, sino en la
## regeneración de las imágenes de barra.
define gui.muted_color = '#3d1466'
define gui.hover_muted_color = '#5b1e99'

## Colores del texto del diálogo y menú.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#eeeeeb'


## Tipos y tamaños de letra ####################################################

## El tipo de letra del texto del juego
define gui.text_font = "Fuentes/Fredoka-Regular.ttf"

## El tipo de letra de los nombres de personajes
define gui.name_text_font = "Fuentes/Fredoka-Medium.ttf"

## El tipo de letra del texto externo al juego.
define gui.interface_text_font = "Fuentes/Fredoka-SemiBold.ttf"

## El tamaño normal del texto del diálogo.
define gui.text_size = 66

## El tamaño de los nombres de los personajes
define gui.name_text_size = 90

## El tamaño del texto en la interfaz.
define gui.interface_text_size = 75

## El tamaño de etiquetas en la interfaz.
define gui.label_text_size = 72

## El tamaño del texto en las notificaciones.
define gui.notify_text_size = 48

## El tamaño del título del juego.
define gui.title_text_size = 150


## Menú principal y menús del juego ############################################

## Imágenes del menú principal y menús del juego.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diálogo #####################################################################
##
## Estas variables controlan cómo se muestra el diálogo en le pantalla, una
## línea cada vez.

## Altura de la caja de texto que contiene el diálogo.
define gui.textbox_height = 370

## Colocación vertical de la caja de texto en la pantalla. 0.0 para la parte
## superior, 0.5 para el centro y 1.0 para la parte inferior.
define gui.textbox_yalign = 1.0


## Colocación del nombre del personaje hablante, relativa a la caja de texto.
## Puede ser el númerode píxels desde la esquina superior izquierda, o 0.5 para
## centrar.
define gui.name_xpos = 1800
define gui.name_ypos = -50

## La alineación horizontal del nombre del personaje. (0.0 es izquierda, 0.5 es
## centro, 1.0 es derecha).
define gui.name_xalign = 0.5

## La anchura, altura y bordes de la caja que contiene el nombre del personaje,
## o 'None' para dimensión automática.
define gui.namebox_width = None
define gui.namebox_height = None

## Los bordes de la caja que contiene el nombre del personaje, en orden:
## izquierda, arriba, derecha, abajo.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Si es 'True, el fondo de la caja del nombre será en mosaico, si es 'False',
## el fondo, si la caja del nombre es escalada.
define gui.namebox_tile = False


## Colocación del diálogo relativa a la caja de texto. Puede ser el número de
## píxels relativos a la esquina superor izquierda o 0.5 para centrar.
define gui.dialogue_xpos = 804
define gui.dialogue_ypos = 50

## La anchura máxima del texto del diálogo, en píxels.
define gui.dialogue_width = 2232

## La alineación horizontal del texto del diálogo. (0.0 es izquierda, 0.5 es
## centro, 1.0 es derecha).
define gui.dialogue_text_xalign = 0.0


## Botones #####################################################################
##
## Estas variables, junto con las imágenes de 'gui/button', controla el aspecto
## de los botones.

## La anchura y altura del botón, en píxels. Si es 'None', Ren'Py calcula el
## tamaño.
define gui.button_width = None
define gui.button_height = None

## Los bordes de cada lado del botón, en orden: izquerda, arriba, derecha,
## abajo.
define gui.button_borders = Borders(12, 12, 12, 12)

## Si es 'True, la imagen de fondo será en mosaico. Si es 'False', la imagen de
## fondo será escalada linealmente.
define gui.button_tile = False

## Tipo de letra del botón.
define gui.button_text_font = gui.interface_text_font

## Tamaño de letra del botón.
define gui.button_text_size = gui.interface_text_size

## El color del texto del botón en varios estados.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## La alineación horizontal del texto del botón. (0.0 es izquierda, 0.5 es
## centro, 1.0 es derecha).
define gui.button_text_xalign = 0.0


## Estas variables invalidan ajustes para diversos tipos de botones. Ver en la
## documentación los tipos de botones disponibles y el uso de cada uno.
##
## Personalizaciones de la interfaz por defecto:

define gui.radio_button_borders = Borders(54, 12, 12, 12)

define gui.check_button_borders = Borders(54, 12, 12, 12)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(30, 12, 30, 12)

define gui.quick_button_borders = Borders(30, 12, 30, 0)
define gui.quick_button_text_size = 42
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Se pueden añadir personalizaciones propias con variables con los nombres
## adecuados. Por ejemplo, es posible descomentar la linea siguiente para
## ajustar la anchura de los botones de navegación.

# define gui.navigation_button_width = 250


## Botones de opción ###########################################################
##
## Los botones de opción se utilizan en los menús del juego.

define gui.choice_button_width = 2370
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(300, 15, 300, 15)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Botones de partidas #########################################################
##
## El botón de hueco de partida es un botón especial. Contiene una miniatura y
## texto que describe el contenido del hueco de partida. Usa imágenes de 'gui/
## button' como los otros botones.

## Botón de guardar partida
define gui.slot_button_width = 828
define gui.slot_button_height = 618
define gui.slot_button_borders = Borders(30, 30, 30, 30)
define gui.slot_button_text_size = 42
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## La anchura y altura de las miniaturas de las partidas guardadas.
define config.thumbnail_width = 768
define config.thumbnail_height = 432

## Número de columnas y filas de la cuadrícula de partidas guardadas.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posicionamiento y espacios ##################################################
##
## Estas variables controlan la posición y espacios de diversos elementos de la
## interfaz.

## Posición del lado izquierdo de los botones de navegación, relativo al lado
## izquierdo de la pantalla.
define gui.navigation_xpos = 120

## Posición vertical del indicador de salto.
define gui.skip_ypos = 30

## Posición vertical de la pantalla de notificación.
define gui.notify_ypos = 135

## Espacio entre opciones de menú.
define gui.choice_spacing = 66

## Botones en la sección de navegación del menú principal y el menú del juego.
define gui.navigation_spacing = 12

## Controla el espacio entre preferencias.
define gui.pref_spacing = 30

## Controla el espacio entre botones de preferencia.
define gui.pref_button_spacing = 0

## Espacio entre botones de página.
define gui.page_spacing = 0

## Espacio entre huecos de guardado.
define gui.slot_spacing = 30

## Posición del texto del menú principal.
define gui.main_menu_text_xalign = 1.0


## Marcos ######################################################################
##
## Estas variables controlan la apariencia de los marcos que pueden contener
## componentes de la interfaz cuando no está presente una ventana.

## Marcos genéricos
define gui.frame_borders = Borders(12, 12, 12, 12)

## Marco usado en la pantalla de confirmación.
define gui.confirm_frame_borders = Borders(120, 120, 120, 120)

## Marco usado en la pantalla de salto.
define gui.skip_frame_borders = Borders(48, 15, 150, 15)

## Marco usado en la pantalla de notificación.
define gui.notify_frame_borders = Borders(48, 15, 120, 15)

## ¿El fondo del marco debe ser en mosaico?
define gui.frame_tile = False


## Barras, barras de desplazamiento y deslizadores #############################
##
## Aquí se controla la apariencia y dimensiones de barras, barras de
## deslizamiento y deslizadores.
##
## La GUI por defecto solo usa deslizadores y barras de deslizamiento
## verticales. Las otras barras solo se usan en pantallas escritas por el
## desarrollador.

## Altura de las barras, barras de deslizamiento y deslizadores horizontales.
## Anchura de barras, barras de deslizamiento y deslizadores verticales.
define gui.bar_size = 75
define gui.scrollbar_size = 36
define gui.slider_size = 75

## 'True' si la imagen de las barras debe ser en mosaico. 'False' si deben ser
## escaladas linealmente.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordes horizontales.
define gui.bar_borders = Borders(12, 12, 12, 12)
define gui.scrollbar_borders = Borders(12, 12, 12, 12)
define gui.slider_borders = Borders(12, 12, 12, 12)

## Bordes verticales.
define gui.vbar_borders = Borders(12, 12, 12, 12)
define gui.vscrollbar_borders = Borders(12, 12, 12, 12)
define gui.vslider_borders = Borders(12, 12, 12, 12)

## Qué hacer con barras de deslizamiento no deslizables en la 'gui'. "hide" las
## esconde mientras que 'None' las muestra.
define gui.unscrollable = "hide"


## Historial ###################################################################
##
## La pantalla de historial muestra diálogo que el jugador ya ha visto.

## Número de bloques de historial de diálogo que Ren'Py conserva.
define config.history_length = 250

## Altura de una entrada de la pantalla de historial, o 'None' para altura
## variable a costa de rendimiento.
define gui.history_height = 420

## Espacio adicional para añadir entre las entradas de la pantalla de historial.
define gui.history_spacing = 0

## Posición, anchura y alineación de la etiqueta con el nombre del personaje
## hablante.
define gui.history_name_xpos = 465
define gui.history_name_ypos = 0
define gui.history_name_width = 465
define gui.history_name_xalign = 1.0

## Posición, anchura y alineación del texto del diálogo.
define gui.history_text_xpos = 510
define gui.history_text_ypos = 6
define gui.history_text_width = 2220
define gui.history_text_xalign = 0.0


## Modo-NVL ####################################################################
##
## La pantalla NVL-mode presenta el diálogo hablado por personajes en modo NVL.

## Bordes del fondo de la ventana del modo NVL.
define gui.nvl_borders = Borders(0, 30, 0, 60)

## Máximo número de entradas en modo NVL que Ren'Py presentará. Al presentar más
## entradas, se borrarán las más antiguas.
define gui.nvl_list_length = 6

## Altura de una entrada en modo NVL. Ajusta a 'None' para que las entradas
## ajusten la altura dinámicamente.
define gui.nvl_height = 345

## Espacio entre entradas en modo NVL cuando 'gui.nvl_height' es None, y entre
## las entradas en modo NVL y el menú en modo NVL.
define gui.nvl_spacing = 30

## Posición, anchura y alineación de la etiqueta con el nombre del personaje
## hablante.
define gui.nvl_name_xpos = 1290
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 450
define gui.nvl_name_xalign = 1.0

## Posición, anchura y alineación del texto del diálogo.
define gui.nvl_text_xpos = 1350
define gui.nvl_text_ypos = 24
define gui.nvl_text_width = 1770
define gui.nvl_text_xalign = 0.0

## Posición, anchura y alineación del texto 'nvl_thought' (texto dicho por el
## personaje 'nvl_narrator').
define gui.nvl_thought_xpos = 720
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 2340
define gui.nvl_thought_xalign = 0.0

## Posición de los botones de menú NVL.
define gui.nvl_button_xpos = 1350
define gui.nvl_button_xalign = 0.0


## Localización ################################################################

## Esto controla donde se permite un salto de línea. El valor por defecto es
## adecuado para la mayoria de idiomas. Puede encontrar una lista de valores
## disponibles en https://www.renpy.org/doc/html/style_properties.html#style-
## property-language

define gui.language = "unicode"


################################################################################
## Dispositivos Móviles
################################################################################

init python:

    ## Esto aumenta el tamaño de los bottones rápidos para facilitar su acceso
    ## en tablets y teléfonos.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(120, 42, 120, 0)

    ## Esto cambia el tamaño y espaciado de varios elementos de la GUI para
    ## asegurar que sean fácilmente visibles en los teléfonos.
    @gui.variant
    def small():

        ## Tamaños de letra.
        gui.text_size = 90
        gui.name_text_size = 108
        gui.notify_text_size = 75
        gui.interface_text_size = 90
        gui.button_text_size = 90
        gui.label_text_size = 102

        ## Ajusta la colocación de la caja de texto.
        gui.textbox_height = 720
        gui.name_xpos = 240
        gui.dialogue_xpos = 270
        gui.dialogue_width = 3300

        ## Cambia el tamaño y espaciado de varios elementos.
        gui.slider_size = 108

        gui.choice_button_width = 3720
        gui.choice_button_text_size = 90

        gui.navigation_spacing = 60
        gui.pref_button_spacing = 30

        gui.history_height = 570
        gui.history_text_width = 2070

        gui.quick_button_text_size = 60

        ## Distribución de botones de archivo.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Modo-NVL
        gui.nvl_height = 510

        gui.nvl_name_width = 915
        gui.nvl_name_xpos = 975

        gui.nvl_text_width = 2745
        gui.nvl_text_xpos = 1035
        gui.nvl_text_ypos = 15

        gui.nvl_thought_width = 3720
        gui.nvl_thought_xpos = 60

        gui.nvl_button_width = 3720
        gui.nvl_button_xpos = 60
