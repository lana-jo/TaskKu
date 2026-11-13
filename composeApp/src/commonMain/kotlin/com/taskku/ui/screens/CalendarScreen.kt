package com.taskku.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.ChevronLeft
import androidx.compose.material.icons.rounded.ChevronRight
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.TaskRepository
import com.taskku.data.daysInMonth
import com.taskku.data.daysInMonthView
import com.taskku.data.minusMonths
import com.taskku.data.monthShortId
import com.taskku.data.plusMonths
import com.taskku.data.today
import com.taskku.data.weekdayShortId
import com.taskku.data.weekdayIndex
import kotlinx.datetime.DayOfWeek
import kotlinx.datetime.LocalDate
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.DockBar
import com.taskku.ui.FabButton
import com.taskku.ui.SectionHeader
import com.taskku.ui.TaskCard

private val weekdays = DayOfWeek.entries.map { weekdayShortId(it) } // SEN..MIN

@Composable
fun CalendarScreen(
    tab: String,
    onTabChange: (String) -> Unit,
    onAdd: () -> Unit,
    onOpenTask: (Int) -> Unit,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val todayDate = remember { today() }
    var viewMonth by remember { mutableStateOf(todayDate.dateOrMonthStart()) }
    var selectedDay by remember { mutableStateOf(todayDate) }

    Box(Modifier.fillMaxSize().background(colors.bg)) {
        Column(
            verticalArrangement = Arrangement.spacedBy(12.dp),
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(start = 24.dp, top = 8.dp, end = 24.dp, bottom = 112.dp),
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    "${monthShortId(viewMonth.month)} ${viewMonth.year}",
                    style = txtJudul(), color = colors.text, modifier = Modifier.weight(1f),
                )
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(36.dp)
                        .clip(CircleShape)
                        .background(colors.surface)
                        .clickable { viewMonth = viewMonth.minusMonths(1) },
                ) {
                    Icon(Icons.Rounded.ChevronLeft, contentDescription = "Bulan sebelumnya", tint = colors.text, modifier = Modifier.size(16.dp))
                }
                Spacer(Modifier.width(8.dp))
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(36.dp)
                        .clip(CircleShape)
                        .background(colors.surface)
                        .clickable { viewMonth = viewMonth.plusMonths(1) },
                ) {
                    Icon(Icons.Rounded.ChevronRight, contentDescription = "Bulan berikutnya", tint = colors.text, modifier = Modifier.size(16.dp))
                }
            }
            Row(modifier = Modifier.fillMaxWidth()) {
                weekdays.forEach { d ->
                    Box(Modifier.weight(1f), contentAlignment = Alignment.Center) {
                        Text(d, style = txt.micro.copy(fontSize = 9.5.sp), color = colors.textMuted)
                    }
                }
            }
            // Grid mulai Senin (index 0); sel kosong di awal bulan sesuai weekday-nya.
            val cellCount = viewMonth.daysInMonthView()
            val rows = (0 until (cellCount + 6) / 7).map { row ->
                (0..6).map { col -> row * 7 + col }
            }
            rows.forEach { week ->
                Row(horizontalArrangement = Arrangement.spacedBy(2.dp), modifier = Modifier.fillMaxWidth()) {
                    week.forEach { cell ->
                        val dayNum = cell - viewMonth.weekdayIndexStart() + 1
                        val valid = dayNum in 1..viewMonth.month.daysInMonth(viewMonth.year)
                        val date = if (valid) LocalDate(viewMonth.year, viewMonth.month, dayNum) else null
                        val isToday = date == todayDate
                        Box(
                            contentAlignment = Alignment.Center,
                            modifier = Modifier.weight(1f).height(46.dp),
                        ) {
                            if (date != null) {
                                val hasTask = TaskRepository.tasks.any { it.date == date }
                                Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(3.dp)) {
                                    Box(
                                        contentAlignment = Alignment.Center,
                                        modifier = Modifier
                                            .size(34.dp)
                                            .clip(CircleShape)
                                            .background(if (date == selectedDay) colors.primary else Color.Transparent)
                                            .clickable { selectedDay = date },
                                    ) {
                                        Text(
                                            "$dayNum",
                                            style = txt.small.copy(
                                                fontSize = 13.sp,
                                                fontWeight = if (isToday || date == selectedDay) FontWeight.SemiBold else FontWeight.Normal,
                                            ),
                                            color = when {
                                                date == selectedDay -> colors.primaryFg
                                                isToday -> colors.primary
                                                else -> colors.text
                                            },
                                        )
                                    }
                                    Box(
                                        modifier = Modifier
                                            .height(4.dp)
                                            .width(if (hasTask) 4.dp else 0.dp)
                                            .clip(CircleShape)
                                            .background(colors.primary),
                                    )
                                }
                            }
                        }
                    }
                }
            }
            val dayTasks = TaskRepository.tasks
                .filter { it.date == selectedDay }
                .sortedWith(compareBy({ it.section }, { it.time }))
            SectionHeader(
                "${weekdayShortId(selectedDay.dayOfWeek)}, ${selectedDay.dayOfMonth} ${monthShortId(selectedDay.month)}",
                dayTasks.size,
                action = "Semua",
            )
            if (dayTasks.isEmpty()) {
                Text("Tidak ada tugas pada tanggal ini.", style = txt.small, color = colors.textMuted, textAlign = TextAlign.Center, modifier = Modifier.fillMaxWidth())
            } else {
                dayTasks.forEach { task ->
                    TaskCard(
                        task = task,
                        onClick = { onOpenTask(task.id) },
                        onToggle = { TaskRepository.toggleDone(task.id) },
                    )
                }
            }
        }
        DockBar(
            active = tab,
            onSelect = onTabChange,
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .padding(start = 16.dp, end = 16.dp, bottom = 14.dp),
        )
        FabButton(
            onClick = onAdd,
            modifier = Modifier
                .align(Alignment.BottomEnd)
                .padding(end = 24.dp, bottom = 90.dp),
        )
    }
}

private fun LocalDate.dateOrMonthStart(): LocalDate = LocalDate(year, month, 1)

private fun LocalDate.weekdayIndexStart(): Int = LocalDate(year, month, 1).weekdayIndex()

@Composable
private fun txtJudul() = LocalTaskKuText.current.section.copy(fontSize = 19.sp)
