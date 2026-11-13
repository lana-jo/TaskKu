package com.taskku.data

import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.util.Locale

actual fun todayLabel(): String =
    LocalDate.now().format(DateTimeFormatter.ofPattern("EEEE, dd MMMM yyyy", Locale("id")))
