package com.taskku.data

import kotlinx.datetime.LocalDate

/** Tanggal hari ini (waktu lokal browser) sebagai ISO yyyy-MM-dd. */
private fun todayIso(): String = js("new Date().toLocaleDateString('sv-SE')")

actual fun today(): LocalDate = LocalDate.parse(todayIso())
