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
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.TaskRepository
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.DockBar
import com.taskku.ui.FabButton
import com.taskku.ui.SectionHeader
import com.taskku.ui.TaskCard

private val weekdays = listOf("MIN", "SEN", "SEL", "RAB", "KAM", "JUM", "SAB")
private const val daysInMonth = 30
private const val today = 13
private val daysWithTasks = setOf(5, 8, 10, 12, 13, 16, 19, 23, 26)
private val selectedDay = 13

@Composable
fun CalendarScreen(
    tab: String,
    onTabChange: (String) -> Unit,
    onAdd: () -> Unit,
    onOpenTask: (Int) -> Unit,
) {
    val colors = LocalTaskKuColors.current

    val txt = LocalTaskKuText.current
    Box(Modifier.fillMaxSize().background(colors.bg)) {
        Column(
            verticalArrangement = Arrangement.spacedBy(12.dp),
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(start = 24.dp, top = 8.dp, end = 24.dp, bottom = 112.dp),
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("November 2026", style = txtJudul(), color = colors.text, modifier = Modifier.weight(1f))
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(36.dp)
                        .clip(CircleShape)
                        .background(colors.surface)
                        .clickable { /* TODO: navigasi bulan nyata butuh sumber tanggal */ },
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
                        .clickable { /* TODO: navigasi bulan nyata butuh sumber tanggal */ },
                ) {
                    Icon(Icons.Rounded.ChevronRight, contentDescription = "Bulan berikutnya", tint = colors.text, modifier = Modifier.size(16.dp))
                }
            }
            Row(modifier = Modifier.fillMaxWidth()) {
                weekdays.forEach { d ->
                    Box(Modifier.width(45.dp), contentAlignment = Alignment.Center) {
                        Text(d, style = txt.micro.copy(fontSize = 9.5.sp), color = colors.textMuted)
                    }
                }
            }
            // Grid: 1 Nov 2026 jatuh di hari Minggu (kolom 0); data demo sesuai desain
            val rows = (0 until 5).map { row ->
                (1..7).map { col -> row * 7 + col }
            }
            rows.forEach { week ->
                Row(horizontalArrangement = Arrangement.spacedBy(2.dp), modifier = Modifier.fillMaxWidth()) {
                    week.forEach { day ->
                        val valid = day <= daysInMonth
                        val isToday = day == today
                        Box(
                            contentAlignment = Alignment.Center,
                            modifier = Modifier.weight(1f).height(46.dp),
                        ) {
                            if (valid) {
                                Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.spacedBy(3.dp)) {
                                    Box(
                                        contentAlignment = Alignment.Center,
                                        modifier = Modifier
                                            .size(34.dp)
                                            .clip(CircleShape)
                                            .background(if (day == selectedDay) colors.primary else Color.Transparent),
                                    ) {
                                        Text(
                                            "$day",
                                            style = txt.small.copy(
                                                fontSize = 13.sp,
                                                fontWeight = if (isToday || day == selectedDay) FontWeight.SemiBold else FontWeight.Normal,
                                            ),
                                            color = if (day == selectedDay) colors.primaryFg else colors.text,
                                        )
                                    }
                                    Box(
                                        modifier = Modifier.height(4.dp).width(if (day in daysWithTasks) 4.dp else 0.dp).clip(CircleShape).background(colors.primary),
                                    )
                                }
                            }
                        }
                    }
                }
            }
            SectionHeader("Jumat, 13 November", 4, action = "Semua")
            val todayTasks = TaskRepository.tasks.filter { it.section == "Hari Ini" }
            if (todayTasks.isEmpty()) {
                Text("Tidak ada tugas pada tanggal ini.", style = txt.small, color = colors.textMuted, textAlign = TextAlign.Center, modifier = Modifier.fillMaxWidth())
            } else {
                todayTasks.forEach { task ->
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

@Composable
private fun txtJudul() = LocalTaskKuText.current.section.copy(fontSize = 19.sp)
