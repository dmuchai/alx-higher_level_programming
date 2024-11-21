-- Script converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Change the default character set and collation of the database
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation of the table
ALTER TABLE `hbtn_0c_0`.`first_table`
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation of the 'name' field
ALTER TABLE `hbtn_0c_0`.`first_table`
    MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

