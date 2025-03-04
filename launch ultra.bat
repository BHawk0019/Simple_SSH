cd Documents\WOW Raid Leading Docs\ULTRA
python getData.py || echo "!!!Python Script Failed" && exit /b
scp character-json.json john@HomeNet:Desktop/lc-script
ssh john@HomeNet "cd Desktop/lc-script && ./launch_ultra.sh"
pause
