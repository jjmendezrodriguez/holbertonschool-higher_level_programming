-- Este script convierte la base de datos hbtn_0c_0 a UTF8 (utf8mb4) con collation utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Este script convierte la tabla first_table a UTF8 (utf8mb4) con collation utf8mb4_unicode_ci
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Este script convierte el campo name en la tabla first_table a UTF8 (utf8mb4) con collation utf8mb4_unicode_ci
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
