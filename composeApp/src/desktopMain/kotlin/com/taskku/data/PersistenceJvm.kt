package com.taskku.data

import app.cash.sqldelight.db.SqlDriver
import app.cash.sqldelight.driver.jdbc.sqlite.JdbcSqliteDriver
import com.taskku.db.TaskDb
import java.io.File
import java.nio.file.Files
import java.nio.file.attribute.PosixFilePermissions
import java.util.Properties

actual fun createTaskDbDriver(): SqlDriver? {
    val dir = File(System.getProperty("user.home"), ".taskku").apply { mkdirs() }
    val dbFile = File(dir, "taskku.db")
    val driver = JdbcSqliteDriver("jdbc:sqlite:${dbFile.absolutePath}", Properties(), TaskDb.Schema)
    // Data pribadi: batasi file DB ke pemilik saja (rw-------). Best-effort:
    // filesystem non-POSIX mengabaikan ini tanpa menggagalkan startup.
    runCatching {
        Files.setPosixFilePermissions(dbFile.toPath(), PosixFilePermissions.fromString("rw-------"))
    }
    return driver
}
