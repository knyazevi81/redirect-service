@echo off
chcp 65001 > nul
echo "  ____  ____  ____       _  _      ____  _____  ____  _     _      "
echo " /   _\/ ___\/  _ \     / \/ \  /|/ ___\/__ __\/  _ \/ \   / \     "
echo " |  /  |    \| / \|     | || |\ |||    \  / \  | / \|| |   | |     "
echo " |  \__\___ || |-||     | || | \||\___ |  | |  | |-||| |_/\| |_/\  "
echo " \____/\____/\_/ \|_____\_/\_/  \|\____/  \_/  \_/ \|\____/\____/  "
echo "                   \____\                                          "
echo выберите режим установки
echo 1 - драйвера asus
echo 2 - активация виндовс
echo 3 - все выше перечисленное
set /p input=set_status:
if %input% == 1 (
    cls
    echo "  ____  ____  ____       _  _      ____  _____  ____  _     _      "
    echo " /   _\/ ___\/  _ \     / \/ \  /|/ ___\/__ __\/  _ \/ \   / \     "
    echo " |  /  |    \| / \|     | || |\ |||    \  / \  | / \|| |   | |     "
    echo " |  \__\___ || |-||     | || | \||\___ |  | |  | |-||| |_/\| |_/\  "
    echo " \____/\____/\_/ \|_____\_/\_/  \|\____/  \_/  \_/ \|\____/\____/  "
    echo "                   \____\                                          "
    echo установка драйверов....
    curl -sLo WirelessLan_DCH_Realtek_Z_V2024.0.10.132_24223.exe https://cloclo50.cloud.mail.ru/public/cLsZWrYj1zbVaHZP7gY/g/no/aFHL/4GRqnP3N2
    curl -sLo I2C_DCH_Intel_Z_V30.100.2237.26Sub1_32096.exe https://cloclo56.cloud.mail.ru/public/2u6r44afq614W9G9ojb3/g/no/4bq3/dJxZ89mJZ
    curl -sLo GPIO_DCH_Intel_Z_V30.100.2237.26Sub1_32093.exe https://cloclo50.cloud.mail.ru/public/aVRFftVt3faveD5daX5/g/no/6QaN/gSokY65N
    echo установка завершена
    pause
) else if %input% == 2 (
    cls
    echo "  ____  ____  ____       _  _      ____  _____  ____  _     _      "
    echo " /   _\/ ___\/  _ \     / \/ \  /|/ ___\/__ __\/  _ \/ \   / \     "
    echo " |  /  |    \| / \|     | || |\ |||    \  / \  | / \|| |   | |     "
    echo " |  \__\___ || |-||     | || | \||\___ |  | |  | |-||| |_/\| |_/\  "
    echo " \____/\____/\_/ \|_____\_/\_/  \|\____/  \_/  \_/ \|\____/\____/  "
    echo "                   \____\                                          "
    echo активация...
    slmgr/ipk W269N-WFGWX-YVC9B-4J6C9-T83GX 
 
    slmgr /skms kms.digiboy.ir 
 
    slmgr /ato

    echo windows activated...
) else if %input% == 3 (
    cls
    echo "  ____  ____  ____       _  _      ____  _____  ____  _     _      "
    echo " /   _\/ ___\/  _ \     / \/ \  /|/ ___\/__ __\/  _ \/ \   / \     "
    echo " |  /  |    \| / \|     | || |\ |||    \  / \  | / \|| |   | |     "
    echo " |  \__\___ || |-||     | || | \||\___ |  | |  | |-||| |_/\| |_/\  "
    echo " \____/\____/\_/ \|_____\_/\_/  \|\____/  \_/  \_/ \|\____/\____/  "
    echo "                   \____\                                          "
    echo установка драйверов....
    curl -sLo WirelessLan_DCH_Realtek_Z_V2024.0.10.132_24223.exe https://cloclo50.cloud.mail.ru/public/cLsZWrYj1zbVaHZP7gY/g/no/aFHL/4GRqnP3N2
    curl -sLo I2C_DCH_Intel_Z_V30.100.2237.26Sub1_32096.exe https://cloclo56.cloud.mail.ru/public/2u6r44afq614W9G9ojb3/g/no/4bq3/dJxZ89mJZ
    curl -sLo GPIO_DCH_Intel_Z_V30.100.2237.26Sub1_32093.exe https://cloclo50.cloud.mail.ru/public/aVRFftVt3faveD5daX5/g/no/6QaN/gSokY65N
    echo установка завершена
    pause
    cls
    echo "  ____  ____  ____       _  _      ____  _____  ____  _     _      "
    echo " /   _\/ ___\/  _ \     / \/ \  /|/ ___\/__ __\/  _ \/ \   / \     "
    echo " |  /  |    \| / \|     | || |\ |||    \  / \  | / \|| |   | |     "
    echo " |  \__\___ || |-||     | || | \||\___ |  | |  | |-||| |_/\| |_/\  "
    echo " \____/\____/\_/ \|_____\_/\_/  \|\____/  \_/  \_/ \|\____/\____/  "
    echo "                   \____\                                          "
    echo активация...
    slmgr/ipk W269N-WFGWX-YVC9B-4J6C9-T83GX 
 
    slmgr /skms kms.digiboy.ir 
 
    slmgr /ato

    echo windows activated...
)

