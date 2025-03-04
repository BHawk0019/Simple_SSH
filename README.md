## Simple_SSH
Simple SSH script that checks for a specified file name in your download directory and sends the file to your machine on your local network via windows batch and SSH.
Speficially optimized to work with Thatsmybis.com

#How-to-use
  - Install python and SSH on your devices
  - Download "character-json.json" from thatsmybis.com
  - Change your config.ini to your speficied paths
  - Create RSA keys between your two devices via SSH if you want to bypass password authentication (You may need to mkdir ./ssh on your machine and copy and paste your keys manually via SSH to properly set secure file transfer)
  - Create .sh script on your linux machine that runs "php ultra.php config.ini" 
  - Run launch ultra.bat 
