import PyInstaller.__main__
import os

package_name = "Catapult Moonshot"
PyInstaller.__main__.run([
    '--name=%s' % package_name,
    '--onefile',
    '--windowed',
    '--add-binary=%s;images/' % os.path.join('images', '*.png'),
    '--add-binary=%s;images/astronaut/' % os.path.join('images/astronaut', '*.png'),
    '--add-binary=%s;sounds/' % os.path.join('sounds', '*.wav'),
    '--add-binary=%s;fonts/' % os.path.join('fonts', '*.ttf'),
    '--hidden-import=pygame',
    '--hidden-import=pygame_gui',
    '--paths=src/',
    '--icon=%s' % os.path.join('images', 'icon.ico'),
    os.path.join('main.py'),
])
