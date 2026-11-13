package com.taskku.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.taskku.data.Categories
import com.taskku.data.TaskRepository
import com.taskku.theme.LocalTaskKuColors
import com.taskku.ui.DockBar
import com.taskku.ui.FabButton
import com.taskku.ui.HeroCard
import com.taskku.ui.ProgressCard
import com.taskku.ui.SectionHeader
import com.taskku.ui.TaskCard
import com.taskku.ui.TaskKuChip

@Composable
fun HomeScreen(
    tab: String,
    twoColumns: Boolean = false,
    onTabChange: (String) -> Unit,
    onOpenTask: (Int) -> Unit,
    onAdd: () -> Unit,
) {
    val colors = LocalTaskKuColors.current
    var filter by remember { mutableStateOf<String?>(null) } // null = Semua

    Box(Modifier.fillMaxSize().background(colors.bg)) {
        Column(
            verticalArrangement = Arrangement.spacedBy(14.dp),
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(start = 24.dp, top = 8.dp, end = 24.dp, bottom = 118.dp),
        ) {
            HeroCard()
            val todayTasks = remember { TaskRepository.tasks.filter { it.section == "Hari Ini" } }
            val doneToday = todayTasks.count { it.isDone }
            ProgressCard(
                pct = if (todayTasks.isEmpty()) 0 else (doneToday * 100 / todayTasks.size),
                done = doneToday,
                total = todayTasks.size,
                note = if (todayTasks.isEmpty()) {
                    "Belum ada tugas untuk hari ini"
                } else {
                    val sisa = todayTasks.size - doneToday
                    if (sisa == 0) "Semua tugas hari ini selesai!"
                    else "$sisa tugas lagi untuk diselesaikan"
                },
            )
            Row(
                horizontalArrangement = Arrangement.spacedBy(8.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .horizontalScroll(rememberScrollState()),
            ) {
                TaskKuChip("Semua", selected = filter == null) { filter = null }
                Categories.all.forEach { cat ->
                    TaskKuChip(cat.label, selected = filter == cat.label) { filter = cat.label }
                }
            }
            TaskRepository.sections.forEach { section ->
                val group = TaskRepository.tasks.filter {
                    it.section == section && (filter == null || it.category.label == filter)
                }
                if (group.isNotEmpty()) {
                    SectionHeader(section, group.size)
                    if (twoColumns) {
                        // Tablet (>= 720): daftar 2 kolom
                        group.chunked(2).forEach { pair ->
                            Row(
                                horizontalArrangement = Arrangement.spacedBy(12.dp),
                                modifier = Modifier.fillMaxWidth(),
                            ) {
                                pair.forEach { task ->
                                    Box(Modifier.weight(1f)) {
                                        TaskCard(
                                            task = task,
                                            onClick = { onOpenTask(task.id) },
                                            onToggle = { TaskRepository.toggleDone(task.id) },
                                        )
                                    }
                                }
                                if (pair.size == 1) Box(Modifier.weight(1f))
                            }
                        }
                    } else {
                        group.forEach { task ->
                            TaskCard(
                                task = task,
                                onClick = { onOpenTask(task.id) },
                                onToggle = { TaskRepository.toggleDone(task.id) },
                            )
                        }
                    }
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
