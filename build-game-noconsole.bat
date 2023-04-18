pyinstaller --onefile --distpath="./windowed" game.pyw
md "%cd%\windowed\game"
md "%cd%\windowed\game\audio"
md "%cd%\windowed\game\images"
copy "%cd%\game\*" "%cd%\windowed\game\*"
copy "%cd%\game\images\*" "%cd%\windowed\game\images\*"
copy "%cd%\game\audio\*" "%cd%\windowed\game\audio\*"
md "%cd%\windowed\python"
copy "%cd%\python\*" "%cd%\windowed\python\*"
copy "%cd%\config.py" "%cd%\windowed\"
del build\game\*
del build\game\localpycs\*
rmdir build\game\localpycs
rmdir build\game
rmdir build 