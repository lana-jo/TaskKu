package com.taskku.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
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
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Close
import androidx.compose.material.icons.rounded.Search
import androidx.compose.material.icons.rounded.Sort
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
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.Categories
import com.taskku.data.TaskRepository
import com.taskku.data.TaskSort
import com.taskku.data.search
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.DockBar
import com.taskku.ui.FabButton
import com.taskku.ui.FieldBox
import com.taskku.ui.TaskCard
import com.taskku.ui.TaskKuChip

@Composable
fun TaskListScreen(
    tab: String,
    onTabChange: (String) -> Unit,
    onAdd: () -> Unit,
    onOpenTask: (Int) -> Unit,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    var query by remember { mutableStateOf("") }
    var categoryFilter by remember { mutableStateOf<String?>(null) } // null = Semua
    var sortMode by remember { mutableStateOf(TaskSort.Tanggal) }

    val results = TaskRepository.tasks.search(query, categoryFilter, sortMode)

    Box(Modifier.fillMaxSize().background(colors.bg)) {
        Column(
            verticalArrangement = Arrangement.spacedBy(12.dp),
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(start = 24.dp, top = 8.dp, end = 24.dp, bottom = 112.dp),
        ) {
            Text("Semua Tugas", style = txt.section.copy(fontSize = 19.sp), color = colors.text)
            FieldBox(
                value = query,
                onValueChange = { query = it },
                placeholder = "Cari tugas...",
                leading = {
                    Icon(Icons.Rounded.Search, contentDescription = null, tint = colors.textMuted, modifier = Modifier.size(18.dp))
                },
                trailing = if (query.isNotEmpty()) {
                    {
                        Icon(
                            Icons.Rounded.Close,
                            contentDescription = "Hapus pencarian",
                            tint = colors.textMuted,
                            modifier = Modifier
                                .size(18.dp)
                                .clickable { query = "" },
                        )
                    }
                } else {
                    null
                },
            )
            Row(
                horizontalArrangement = Arrangement.spacedBy(8.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .horizontalScroll(rememberScrollState()),
            ) {
                TaskKuChip("Semua", selected = categoryFilter == null) { categoryFilter = null }
                Categories.all.forEach { cat ->
                    TaskKuChip(cat.label, selected = categoryFilter == cat.label) { categoryFilter = cat.label }
                }
            }
            Row(verticalAlignment = Alignment.CenterVertically) {
                Icon(Icons.Rounded.Sort, contentDescription = null, tint = colors.textMuted, modifier = Modifier.size(15.dp))
                Spacer(Modifier.width(6.dp))
                Text("Urutkan:", style = txt.small, color = colors.textMuted)
                Spacer(Modifier.width(6.dp))
                TaskSort.entries.forEach { mode ->
                    TaskKuChip(mode.label, selected = sortMode == mode) { sortMode = mode }
                    Spacer(Modifier.width(6.dp))
                }
            }
            Text(
                "${results.size} tugas ditemukan",
                style = txt.small.copy(fontSize = 11.5.sp),
                color = colors.textMuted,
            )
            if (results.isEmpty()) {
                Text(
                    if (query.isBlank() && categoryFilter == null) {
                        "Belum ada tugas. Tekan + untuk menambahkan."
                    } else {
                        "Tidak ada tugas yang cocok dengan pencarian atau filter."
                    },
                    style = txt.small,
                    color = colors.textMuted,
                    modifier = Modifier.fillMaxWidth().padding(top = 24.dp),
                    textAlign = androidx.compose.ui.text.style.TextAlign.Center,
                )
            } else {
                results.forEach { task ->
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
