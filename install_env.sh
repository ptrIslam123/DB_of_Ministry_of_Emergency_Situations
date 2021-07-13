#! bin/bash



# Create directory for sqlite3 (sqlDB)
mkdir sqlDB
# Create file for DB
touch sqlDB/main.db


# chenge current directopy 
cd src/
USER_LOGIN="root" # default user login
USER_PASSWD="root" # default user password

# Create user account
python autointoxication.py ${USER_LOGIN} ${USER_PASSWD}



echo "Installetion successful"