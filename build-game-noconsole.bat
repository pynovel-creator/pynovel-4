@echo off
pyinstaller --onefile --windowed run_game.py
md "%cd%\dist\game"
copy "%cd%\game" "%cd%\dist\game\*"
md "%cd%\dist\script"
md "%cd%\dist\script\display"
md "%cd%\dist\script\audio"
copy "%cd%\script\display\*" "%cd%\dist\script\display\*"
copy "%cd%\script\audio\*" "%cd%\dist\script\audio\*"
copy "%cd%\script\*" "%cd%\dist\script\*"
del *.spec
del build\run_game\*
del build\run_game\localpycs\*
rmdir build\run_game\localpycs
rmdir build\run_game
rmdir build
copy "%cd%\*.py" "%cd%\dist\*.py"