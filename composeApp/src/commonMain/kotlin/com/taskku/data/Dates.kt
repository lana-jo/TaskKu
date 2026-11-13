package com.taskku.data

import kotlinx.datetime.DatePeriod
import kotlinx.datetime.DayOfWeek
import kotlinx.datetime.LocalDate
import kotlinx.datetime.Month
import kotlinx.datetime.daysUntil
import kotlinx.datetime.minus
import kotlinx.datetime.plus

/** Tanggal hari ini sebagai LocalDate (satu sumber kebenaran untuk app). */
expect fun today(): LocalDate

fun LocalDate.plusMonths(count: Int): LocalDate {
    val total = (month.ordinal + 1) + count - 1
    val year2 = year + total / 12
    val month2 = Month.entries[total % 12]
    val day2 = minOf(dayOfMonth, month2.daysInMonth(year2))
    return LocalDate(year2, month2, day2)
}

fun LocalDate.minusMonths(count: Int): LocalDate = plusMonths(-count)

fun Month.daysInMonth(year: Int): Int = when (this) {
    Month.JANUARY, Month.MARCH, Month.MAY, Month.JULY, Month.AUGUST, Month.OCTOBER, Month.DECEMBER -> 31
    Month.APRIL, Month.JUNE, Month.SEPTEMBER, Month.NOVEMBER -> 30
    Month.FEBRUARY -> if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) 29 else 28
}

/** Senin sebagai awal minggu (klausul desain Indonesia). */
fun LocalDate.weekdayIndex(): Int = (dayOfWeek.ordinal + 6) % 7 // SEN=0..MIN=6

fun LocalDate.startOfWeek(): LocalDate = minus(DatePeriod(days = weekdayIndex()))

fun LocalDate.daysInMonthView(): Int {
    val first = LocalDate(year, month, 1)
    return first.weekdayIndex() + month.daysInMonth(year)
}

/** Label Indonesia singkat: SEN, SEL, RAB, KAM, JUM, SAB, MIN. */
fun weekdayShortId(day: DayOfWeek): String = when (day) {
    DayOfWeek.MONDAY -> "SEN"
    DayOfWeek.TUESDAY -> "SEL"
    DayOfWeek.WEDNESDAY -> "RAB"
    DayOfWeek.THURSDAY -> "KAM"
    DayOfWeek.FRIDAY -> "JUM"
    DayOfWeek.SATURDAY -> "SAB"
    DayOfWeek.SUNDAY -> "MIN"
}

fun monthShortId(month: Month): String = when (month) {
    Month.JANUARY -> "Januari"
    Month.FEBRUARY -> "Februari"
    Month.MARCH -> "Maret"
    Month.APRIL -> "April"
    Month.MAY -> "Mei"
    Month.JUNE -> "Juni"
    Month.JULY -> "Juli"
    Month.AUGUST -> "Agustus"
    Month.SEPTEMBER -> "September"
    Month.OCTOBER -> "Oktober"
    Month.NOVEMBER -> "November"
    Month.DECEMBER -> "Desember"
}
