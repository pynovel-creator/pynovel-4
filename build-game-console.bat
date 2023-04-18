pyinstaller --onefile --distpath="./console" game.py
md "%cd%\console\game"
md "%cd%\console\game\audio"
md "%cd%\console\game\images"
copy "%cd%\game\*" "%cd%\console\game\*"
copy "%cd%\game\images\*" "%cd%\console\game\images\*"
copy "%cd%\game\audio\*" "%cd%\console\game\audio\*"
md "%cd%\console\python"
copy "%cd%\python\*" "%cd%\console\python\*"
copy "%cd%\config.py" "%cd%\console\"
del build\game\*
del build\game\localpycs\*
rmdir build\game\localpycs
rmdir build\game
rmdir build 