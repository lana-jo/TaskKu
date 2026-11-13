package com.taskku.data

import app.cash.sqldelight.db.SqlDriver

// wasmJs belum memiliki driver sqlite terpasang — repository berjalan in-memory.
actual fun createTaskDbDriver(): SqlDriver? = null
