-- Script converts a database to utf-8

-- Convert database to utf-8
ALTER DATABASE
	hbtn_0c_0
	CHARACTER SET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

-- converts the table hbtn_0c_0 to utf-8
ALTER TABLE 
	hbtn_0c_0.first_table
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;

-- convert the field 'name' to utf-8
ALTER TABLE
	hbtn_0c_0.first_table
	MODIFY name
	VARCHAR(256)
	CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci;
