import xbmcgui
import xbmcplugin
from xbmcswift2 import Plugin
import requests
from bs4 import BeautifulSoup

plugin = Plugin()

# Definición de canales ficticios
channels = [
    {'TC': 'Canal 13', 'url': 'https://www.dailymotion.com/embed/video/x7wijay?autoplay=1'}
    # Agrega más canales aquí
]

# Ruta principal del complemento
@plugin.route('/')
def main_menu():
    items = []
    for channel in channels:
        items.append({
            'label': channel['TC'],  # MODIFICAR
            'path': plugin.url_for('play_stream', channel_name=channel['TC']),  # MODIFICAR
            'thumbnail': 'https://www.dailymotion.com/embed/video/x7wijay?autoplay=1'  # MODIFICAR
        })
    return items

# Ruta para reproducir un canal
@plugin.route('/play/<channel_name>')
def play_stream(channel_name):
    # Obtener la URL del canal según el nombre
    for channel in channels:
        if channel['TC'] == channel_name:  # MODIFICAR
            channel_url = channel['https://www.dailymotion.com/embed/video/x7wijay?autoplay=1']  # MODIFICAR
            break
    else:
        plugin.notify('Canal no encontrado', 'El canal no está disponible')
        return
    
    # Reproducir el canal utilizando xbmc.Player()
    player = xbmc.Player()
    player.play(channel_url)

if __name__ == '__main__':
    plugin.run()
