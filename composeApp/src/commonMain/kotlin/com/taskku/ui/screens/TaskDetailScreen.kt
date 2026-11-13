package com.taskku.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
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
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Check
import androidx.compose.material.icons.rounded.ChevronLeft
import androidx.compose.material.icons.rounded.MoreVert
import androidx.compose.material.icons.rounded.Edit
import androidx.compose.material.icons.rounded.Schedule
import androidx.compose.material.icons.rounded.Delete
import androidx.compose.material3.Icon
import androidx.compose.material3.Surface
import androidx.compose.material3.Switch
import androidx.compose.material3.SwitchDefaults
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
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import com.taskku.data.Task
import com.taskku.data.TaskRepository
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.TaskKuShapes
import com.taskku.theme.LocalTaskKuText

@Composable
fun TaskDetailScreen(
    taskId: Int,
    onBack: () -> Unit,
    onEdit: (Task) -> Unit,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val task = TaskRepository.byId(taskId)
    if (task == null) {
        onBack()
        return
    }
    var showDelete by remember { mutableStateOf(false) }

    Box(Modifier.fillMaxSize().background(colors.bg)) {
        Column(
            verticalArrangement = Arrangement.spacedBy(14.dp),
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(start = 24.dp, end = 24.dp, bottom = 32.dp, top = 12.dp),
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                HeaderCircle(Icons.Rounded.ChevronLeft, "Kembali") { onBack() }
                Spacer(Modifier.weight(1f))
                HeaderCircle(Icons.Rounded.MoreVert, "Menu lainnya") { }
            }
            Text(task.title, style = txt.display.copy(fontSize = 24.sp), color = colors.text)
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                MetaChip(text = task.category.label, color = task.category.color, soft = task.category.soft)
                MetaChip(text = task.priority.label, color = task.priority.color, soft = task.priority.color.copy(alpha = 0.12f))
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp),
                ) {
                    Icon(Icons.Rounded.Schedule, contentDescription = null, tint = colors.textMuted, modifier = Modifier.size(14.dp))
                    Text("Hari ini, ${task.time}", style = txt.small, color = colors.textMuted)
                }
            }
            if (!task.description.isNullOrBlank()) {
                Surface(shape = TaskKuShapes.card, color = colors.surface, shadowElevation = 4.dp) {
                    Column(Modifier.padding(16.dp)) {
                        Text("DESKRIPSI", style = txt.micro, color = colors.textMuted)
                        Spacer(Modifier.height(8.dp))
                        Text(task.description, style = txt.body, color = colors.text)
                    }
                }
            }
            if (task.subtasks.isNotEmpty()) {
                val doneCount = task.subtasks.count { it.isDone }
                Surface(shape = TaskKuShapes.card, color = colors.surface, shadowElevation = 4.dp) {
                    Column(
                        verticalArrangement = Arrangement.spacedBy(10.dp),
                        modifier = Modifier.padding(14.dp),
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Text("SUBTUGAS", style = txt.micro, color = colors.textMuted, modifier = Modifier.weight(1f))
                            Box(
                                modifier = Modifier
                                    .clip(RoundedCornerShape(999.dp))
                                    .background(colors.surface2)
                                    .padding(horizontal = 8.dp, vertical = 2.dp),
                            ) {
                                Text(
                                    "$doneCount/${task.subtasks.size}",
                                    style = txt.small.copy(fontSize = 10.5.sp, fontWeight = FontWeight.SemiBold),
                                    color = colors.textMuted,
                                )
                            }
                        }
                        task.subtasks.forEachIndexed { index, sub ->
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.spacedBy(10.dp),
                                modifier = Modifier.clickable { TaskRepository.toggleSubtask(task.id, index) },
                            ) {
                                Box(
                                    contentAlignment = Alignment.Center,
                                    modifier = Modifier
                                        .size(22.dp)
                                        .clip(CircleShape)
                                        .background(if (sub.isDone) colors.primary else Color.Transparent)
                                        .then(
                                            if (sub.isDone) Modifier
                                            else Modifier.border(2.dp, colors.border, CircleShape),
                                        ),
                                ) {
                                    if (sub.isDone) {
                                        Icon(
                                            Icons.Rounded.Check,
                                            contentDescription = null,
                                            tint = Color.White,
                                            modifier = Modifier.size(12.dp),
                                        )
                                    }
                                }
                                Text(
                                    sub.title,
                                    style = if (sub.isDone) txt.body else txt.bodyMedium,
                                    color = if (sub.isDone) colors.textMuted else colors.text,
                                    textDecoration = if (sub.isDone) TextDecoration.LineThrough else null,
                                )
                            }
                        }
                    }
                }
            }
            Surface(shape = TaskKuShapes.card, color = colors.surface, shadowElevation = 4.dp) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 13.dp),
                ) {
                    Box(
                        contentAlignment = Alignment.Center,
                        modifier = Modifier
                            .size(32.dp)
                            .clip(RoundedCornerShape(10.dp))
                            .background(colors.surface2),
                    ) {
                        Icon(Icons.Rounded.Schedule, contentDescription = null, tint = colors.textMuted, modifier = Modifier.size(16.dp))
                    }
                    Spacer(Modifier.width(12.dp))
                    Text("Pengingat 10 menit sebelumnya", style = txt.body, color = colors.text, modifier = Modifier.weight(1f))
                    Switch(
                        checked = task.reminder,
                        onCheckedChange = { TaskRepository.update(task.copy(reminder = it)) },
                        colors = SwitchDefaults.colors(
                            checkedTrackColor = colors.primary,
                            checkedThumbColor = Color.White,
                            uncheckedTrackColor = colors.border,
                            uncheckedThumbColor = Color.White,
                        ),
                    )
                }
            }
            Spacer(Modifier.weight(1f))
            Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                ActionButton(
                    label = "Edit",
                    icon = Icons.Rounded.Edit,
                    tint = colors.primary,
                    modifier = Modifier.weight(1f),
                ) { onEdit(task) }
                ActionButton(
                    label = "Hapus",
                    icon = Icons.Rounded.Delete,
                    tint = colors.danger,
                    modifier = Modifier.weight(1f),
                ) { showDelete = true }
            }
        }

        if (showDelete) {
            DeleteConfirmDialog(
                taskTitle = task.title,
                onDismiss = { showDelete = false },
                onConfirm = {
                    TaskRepository.delete(task.id)
                    showDelete = false
                    onBack()
                },
            )
        }
    }
}

@Composable
private fun HeaderCircle(icon: ImageVector, desc: String, onClick: () -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Box(
        contentAlignment = Alignment.Center,
        modifier = Modifier
            .size(44.dp)
            .clip(CircleShape)
            .background(colors.surface)
            .clickable(onClick = onClick),
    ) {
        Icon(icon, contentDescription = desc, tint = colors.text, modifier = Modifier.size(20.dp))
    }
}

@Composable
private fun MetaChip(text: String, color: Color, soft: Color) {
    val txt = LocalTaskKuText.current
    Row(
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(5.dp),
        modifier = Modifier
            .clip(RoundedCornerShape(999.dp))
            .background(soft)
            .padding(horizontal = 10.dp, vertical = 4.dp),
    ) {
        Box(Modifier.size(5.dp).clip(CircleShape).background(color))
        Text(
            text,
            style = txt.small.copy(fontSize = 11.sp, fontWeight = FontWeight.SemiBold),
            color = color,
        )
    }
}

@Composable
private fun ActionButton(label: String, icon: ImageVector, tint: Color, modifier: Modifier = Modifier, onClick: () -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Box(
        contentAlignment = Alignment.Center,
        modifier = modifier
            .height(52.dp)
            .clip(RoundedCornerShape(999.dp))
            .background(colors.surface)
            .clickable(onClick = onClick),
    ) {
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp), verticalAlignment = Alignment.CenterVertically) {
            Icon(icon, contentDescription = null, tint = tint, modifier = Modifier.size(17.dp))
            Text(label, style = txt.bodyMedium.copy(fontWeight = FontWeight.SemiBold), color = tint)
        }
    }
}

@Composable
private fun DeleteConfirmDialog(taskTitle: String, onDismiss: () -> Unit, onConfirm: () -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Dialog(onDismissRequest = onDismiss) {
        Surface(shape = RoundedCornerShape(24.dp), color = colors.surface) {
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.spacedBy(14.dp),
                modifier = Modifier.padding(24.dp),
            ) {
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(60.dp)
                        .clip(CircleShape)
                        .background(colors.danger.copy(alpha = 0.12f)),
                ) {
                    Icon(Icons.Rounded.Delete, contentDescription = null, tint = colors.danger, modifier = Modifier.size(26.dp))
                }
                Text("Hapus tugas?", style = txt.section.copy(fontSize = 18.sp), color = colors.text)
                Text(
                    "Tugas \u201c$taskTitle\u201d akan dihapus permanen. Tindakan ini tidak bisa dibatalkan.",
                    style = txt.small,
                    color = colors.textMuted,
                    textAlign = TextAlign.Center,
                )
                Row(horizontalArrangement = Arrangement.spacedBy(10.dp), modifier = Modifier.fillMaxWidth()) {
                    Box(
                        contentAlignment = Alignment.Center,
                        modifier = Modifier
                            .weight(1f)
                            .height(46.dp)
                            .clip(RoundedCornerShape(999.dp))
                            .background(colors.surface)
                            .clickable(onClick = onDismiss),
                    ) {
                        Text(
                            "Batal",
                            style = txt.bodyMedium.copy(fontWeight = FontWeight.SemiBold),
                            color = colors.text,
                        )
                    }
                    Box(
                        contentAlignment = Alignment.Center,
                        modifier = Modifier
                            .weight(1f)
                            .height(46.dp)
                            .clip(RoundedCornerShape(999.dp))
                            .background(colors.danger)
                            .clickable(onClick = onConfirm),
                    ) {
                        Text(
                            "Hapus",
                            style = txt.bodyMedium.copy(fontWeight = FontWeight.SemiBold),
                            color = colors.primaryFg,
                        )
                    }
                }
            }
        }
    }
}
