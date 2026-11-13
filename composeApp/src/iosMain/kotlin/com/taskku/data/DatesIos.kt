package com.taskku.data

import kotlinx.datetime.Clock
import kotlinx.datetime.LocalDate
import kotlinx.datetime.TimeZone
import kotlinx.datetime.todayIn

actual fun today(): LocalDate = Clock.System.todayIn(TimeZone.currentSystemDefault())
