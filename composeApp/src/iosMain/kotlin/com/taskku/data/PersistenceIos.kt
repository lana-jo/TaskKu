package com.taskku.data

import app.cash.sqldelight.db.SqlDriver
import app.cash.sqldelight.drivers.native.NativeSqliteDriver
import com.taskku.db.TaskDb

actual fun createTaskDbDriver(): SqlDriver? =
    NativeSqliteDriver(TaskDb.Schema, "taskku.db")
