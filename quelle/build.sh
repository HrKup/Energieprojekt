set -e
D=/tmp/claude-0/-home-user/4ea94787-b298-5048-82ac-b19bdfe2c68e/scratchpad/web
cd $D
python3 gen_web.py >/dev/null
python3 integrate.py >/dev/null
python3 codefix.py
S=$D/lernpfad.html; cd /home/user/energieprojekt
{ printf '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="robots" content="noindex">\n'; sed -n '1,/<\/style>/p' $S; printf '</head>\n<body>\n'; sed -n '/<\/style>/,$p' $S | tail -n +2; printf '</body>\n</html>\n'; } > index.html
