package com.taskku.data

import app.cash.sqldelight.db.SqlDriver
import app.cash.sqldelight.driver.native.NativeSqliteDriver
import com.taskku.db.TaskDb

actual fun createTaskDbDriver(): SqlDriver? =
    NativeSqliteDriver(TaskDb.Schema, "taskku.db")
