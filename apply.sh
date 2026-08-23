cd ~/dev/background

theme=`noctalia msg color-scheme-get | cut -d' ' -f2- | tr '[:upper:]' '[:lower:]' | tr ' ' '-'`
mode=`noctalia msg theme-mode-get`
gen_mode=light
if [ "$mode" = "dark" ]; then
    gen_mode=dark
fi

file="$HOME/dev/background/bg/$theme-$gen_mode.png"

if [ -f "$file" ]; then
    notify-send "Background already exists."
else
    notify-send "Generating background..."
    uv run ~/dev/background/build.py $gen_mode
    cp ~/dev/background/out.png $file
fi

noctalia msg wallpaper-set "$file"

