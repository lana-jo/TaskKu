package com.taskku.ui.screens

import androidx.compose.foundation.background
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
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.Categories
import com.taskku.data.TaskRepository
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.TaskKuShapes
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.DockBar
import com.taskku.ui.FabButton
import com.taskku.ui.MicroLabel
import com.taskku.ui.Ring
import com.taskku.ui.TaskKuChip

private val barValues = listOf(5, 7, 4, 8, 6, 3, 7) // data demo sementara (belum ada persistensi)
private val barLabels = listOf("SEN", "SEL", "RAB", "KAM", "JUM", "SAB", "MIN")
private const val todayBarIndex = 4 // Jumat

@Composable
fun StatisticsScreen(
    tab: String,
    onTabChange: (String) -> Unit,
    onAdd: () -> Unit,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val todayTasks = TaskRepository.tasks.filter { it.section == "Hari Ini" }
    val doneToday = todayTasks.count { it.isDone }
    val pct = if (todayTasks.isEmpty()) 0 else (doneToday * 100 / todayTasks.size)
    val byCategory = Categories.all.map { cat -> cat to TaskRepository.tasks.count { it.category.label == cat.label } }
    val maxCategory = byCategory.maxOf { it.second }.coerceAtLeast(1)

    Box(Modifier.fillMaxSize().background(colors.bg)) {
        Column(
            verticalArrangement = Arrangement.spacedBy(14.dp),
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(start = 24.dp, top = 8.dp, end = 24.dp, bottom = 112.dp),
        ) {
            Text("Statistik", style = txt.section.copy(fontSize = 19.sp), color = colors.text)
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                TaskKuChip("Harian", selected = true)
                TaskKuChip("Mingguan")
                TaskKuChip("Bulanan")
            }
            Surface2 {
                Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.padding(horizontal = 20.dp, vertical = 18.dp)) {
                    Ring(pct, 92.dp, labelSize = 15.sp)
                    Spacer(Modifier.width(18.dp))
                    Column {
                        MicroLabel("Progres hari ini")
                        Spacer(Modifier.height(5.dp))
                        Text("$doneToday dari ${todayTasks.size} tugas", style = txt.section.copy(fontSize = 17.sp), color = colors.text)
                        Spacer(Modifier.height(3.dp))
                        Text("+12% dari kemarin (demo)", style = txt.small.copy(fontSize = 11.5.sp, fontWeight = FontWeight.SemiBold), color = colors.success)
                    }
                }
            }
            Surface2 {
                Column(verticalArrangement = Arrangement.spacedBy(12.dp), modifier = Modifier.padding(18.dp)) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text("Aktivitas 7 Hari", style = txt.bodyMedium.copy(fontWeight = FontWeight.SemiBold), color = colors.text, modifier = Modifier.weight(1f))
                        Box(
                            modifier = Modifier
                                .clip(RoundedCornerShape(999.dp))
                                .background(colors.primarySoft)
                                .padding(horizontal = 9.dp, vertical = 3.dp),
                        ) {
                            Text("28 tugas (demo)", style = txt.small.copy(fontSize = 11.sp, fontWeight = FontWeight.SemiBold), color = colors.primary)
                        }
                    }
                    Row(horizontalArrangement = Arrangement.spacedBy(10.dp), modifier = Modifier.fillMaxWidth().height(118.dp), verticalAlignment = Alignment.Bottom) {
                        barValues.forEachIndexed { index, value ->
                            Box(contentAlignment = Alignment.BottomCenter, modifier = Modifier.weight(1f).height(118.dp)) {
                                Box(
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height((value * 13).dp)
                                        .clip(RoundedCornerShape(8.dp))
                                        .background(if (index == todayBarIndex) colors.primary else colors.primarySoft),
                                )
                            }
                        }
                    }
                    Row(horizontalArrangement = Arrangement.spacedBy(10.dp), modifier = Modifier.fillMaxWidth()) {
                        barLabels.forEachIndexed { index, label ->
                            Box(Modifier.weight(1f), contentAlignment = Alignment.Center) {
                                Text(
                                    label,
                                    style = txt.micro.copy(fontSize = 9.sp, letterSpacing = 0.4.sp),
                                    color = if (index == todayBarIndex) colors.primary else colors.textMuted,
                                )
                            }
                        }
                    }
                }
            }
            Surface2 {
                Column(verticalArrangement = Arrangement.spacedBy(12.dp), modifier = Modifier.padding(18.dp)) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text("Berdasarkan Kategori", style = txt.bodyMedium.copy(fontWeight = FontWeight.SemiBold), color = colors.text, modifier = Modifier.weight(1f))
                        Text("Bulan ini (demo)", style = txt.small.copy(fontSize = 11.sp), color = colors.textMuted)
                    }
                    byCategory.forEach { (cat, count) ->
                        Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(9.dp), modifier = Modifier.fillMaxWidth()) {
                            Box(Modifier.size(9.dp).clip(CircleShape).background(cat.color))
                            Text(cat.label, style = txt.body.copy(fontSize = 13.5.sp), color = colors.text)
                            Spacer(Modifier.weight(1f))
                            Box(
                                modifier = Modifier
                                    .width(72.dp)
                                    .height(5.dp)
                                    .clip(RoundedCornerShape(999.dp))
                                    .background(colors.surface2),
                            ) {
                                Box(
                                    modifier = Modifier
                                        .fillMaxWidth(count.toFloat() / maxCategory)
                                        .height(5.dp)
                                        .clip(RoundedCornerShape(999.dp))
                                        .background(cat.color),
                                )
                            }
                            Text("$count", style = txt.small.copy(fontSize = 12.sp, fontWeight = FontWeight.SemiBold), color = colors.textMuted)
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

@Composable
private fun Surface2(content: @Composable () -> Unit) {
    val colors = LocalTaskKuColors.current
    androidx.compose.material3.Surface(shape = TaskKuShapes.card, color = colors.surface, shadowElevation = 4.dp, modifier = Modifier.fillMaxWidth()) {
        content()
    }
}
