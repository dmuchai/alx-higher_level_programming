-- Script converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Change the default character set and collation of the database
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the character set and collation of the table
ALTER TABLE `hbtn_0c_0`.`first_table`
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the 'id' column to explicitly use int(11)
ALTER TABLE `hbtn_0c_0`.`first_table`
    MODIFY `id` int(11) DEFAULT NULL;

-- Modify the 'name' column to explicitly use utf8mb4 with utf8mb4_unicode_ci collation
ALTER TABLE `hbtn_0c_0`.`first_table`
    MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL;
