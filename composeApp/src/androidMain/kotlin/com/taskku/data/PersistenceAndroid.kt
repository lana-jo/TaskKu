package com.taskku.data

import android.content.Context
import app.cash.sqldelight.db.SqlDriver
import app.cash.sqldelight.driver.android.AndroidSqliteDriver
import com.taskku.db.TaskDb

/** Context di-set dari MainActivity.onCreate sebelum App() dirender pertama kali. */
object AndroidDatabase {
    var appContext: Context? = null
}

actual fun createTaskDbDriver(): SqlDriver? {
    val context = AndroidDatabase.appContext
        ?: error("AndroidDatabase.appContext belum di-set di MainActivity.onCreate")
    return AndroidSqliteDriver(TaskDb.Schema, context, "taskku.db")
}
