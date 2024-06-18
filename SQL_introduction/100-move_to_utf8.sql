-- Convertir la base de datos hbtn_0c_0 a UTF8 (utf8mb4) con collation utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convertir la tabla first_table a UTF8 (utf8mb4) con collation utf8mb4_unicode_ci
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convertir el campo name en la tabla first_table a UTF8 (utf8mb4) con collation utf8mb4_unicode_ci
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
