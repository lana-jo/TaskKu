package com.taskku.data

import kotlin.time.Clock
import kotlin.time.ExperimentalTime
import kotlinx.datetime.LocalDate
import kotlinx.datetime.TimeZone
import kotlinx.datetime.todayIn

@OptIn(ExperimentalTime::class)
actual fun today(): LocalDate = Clock.System.todayIn(TimeZone.currentSystemDefault())
