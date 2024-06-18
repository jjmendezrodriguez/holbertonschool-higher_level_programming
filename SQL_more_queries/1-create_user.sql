-- Este script crea el usuario user_0d_1 con todos los privilegios en el servidor MySQL
-- Crear el usuario user_0d_1 con la contraseña user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Otorgar todos los privilegios al usuario user_0d_1 en el servidor MySQL
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- Aplicar los cambios
FLUSH PRIVILEGES;