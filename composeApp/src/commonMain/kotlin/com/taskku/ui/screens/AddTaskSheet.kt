package com.taskku.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Close
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.Switch
import androidx.compose.material3.SwitchDefaults
import androidx.compose.material3.Text
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
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
import com.taskku.data.Priorities
import com.taskku.data.Task
import com.taskku.data.TaskRepository
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.TaskKuShapes
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.FieldBox
import com.taskku.ui.PrimaryButton


@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddTaskSheet(
    visible: Boolean,
    editing: Task?,
    onDismiss: () -> Unit,
) {
    if (!visible) return
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)

    var title by remember { mutableStateOf("") }
    var note by remember { mutableStateOf("") }
    var category by remember { mutableStateOf(Categories.Pekerjaan) }
    var priority by remember { mutableStateOf(Priorities.Tinggi) }
    var reminder by remember { mutableStateOf(true) }

    LaunchedEffect(editing) {
        if (editing != null) {
            title = editing.title
            note = editing.description ?: ""
            category = editing.category
            priority = editing.priority
            reminder = editing.reminder
        } else {
            title = ""
            note = ""
            category = Categories.Pekerjaan
            priority = Priorities.Tinggi
            reminder = true
        }
    }

    ModalBottomSheet(
        onDismissRequest = onDismiss,
        sheetState = sheetState,
        containerColor = colors.surface,
        shape = TaskKuShapes.sheet,
        dragHandle = null,
    ) {
        Column(
            verticalArrangement = Arrangement.spacedBy(14.dp),
            modifier = Modifier.padding(start = 24.dp, end = 24.dp, bottom = 30.dp, top = 4.dp),
        ) {
            Box(Modifier.fillMaxWidth(), contentAlignment = Alignment.Center) {
                Box(
                    Modifier
                        .width(44.dp)
                        .height(4.5.dp)
                        .clip(RoundedCornerShape(999.dp))
                        .background(colors.border),
                )
            }
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    if (editing == null) "Tugas Baru" else "Edit Tugas",
                    style = txt.section.copy(fontSize = 18.sp),
                    color = colors.text,
                    modifier = Modifier.weight(1f),
                )
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(34.dp)
                        .clip(CircleShape)
                        .background(colors.surface2)
                        .clickable(onClick = onDismiss),
                ) {
                    Icon(
                        Icons.Rounded.Close,
                        contentDescription = "Tutup",
                        tint = colors.textMuted,
                        modifier = Modifier.size(15.dp),
                    )
                }
            }
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text("Judul tugas", style = txt.small.copy(fontWeight = FontWeight.SemiBold, fontSize = 12.5.sp), color = colors.textMuted)
                FieldBox(title, { title = it }, "Judul tugas")
            }
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text("Catatan", style = txt.small.copy(fontWeight = FontWeight.SemiBold, fontSize = 12.5.sp), color = colors.textMuted)
                FieldBox(note, { note = it }, "Tambahkan catatan (opsional)", height = 64.dp)
            }
            Column(verticalArrangement = Arrangement.spacedBy(9.dp)) {
                Text("Kategori", style = txt.small.copy(fontWeight = FontWeight.SemiBold, fontSize = 12.5.sp), color = colors.textMuted)
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    Categories.all.forEach { cat ->
                        val selected = cat.label == category.label
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(5.dp),
                            modifier = Modifier
                                .clip(RoundedCornerShape(999.dp))
                                .background(if (selected) cat.soft else colors.surface2)
                                .clickable { category = cat }
                                .padding(horizontal = 13.dp, vertical = 8.dp),
                        ) {
                            Box(Modifier.size(6.dp).clip(CircleShape).background(cat.color))
                            Text(
                                cat.label,
                                style = txt.small.copy(
                                    fontSize = 12.5.sp,
                                    fontWeight = if (selected) FontWeight.SemiBold else FontWeight.Normal,
                                ),
                                color = if (selected) cat.color else colors.textMuted,
                            )
                        }
                    }
                }
            }
            Column(verticalArrangement = Arrangement.spacedBy(9.dp)) {
                Text("Prioritas", style = txt.small.copy(fontWeight = FontWeight.SemiBold, fontSize = 12.5.sp), color = colors.textMuted)
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    Priorities.all.forEach { prio ->
                        val selected = prio.label == priority.label
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center,
                            modifier = Modifier
                                .weight(1f)
                                .height(42.dp)
                                .clip(RoundedCornerShape(14.dp))
                                .background(if (selected) prio.color.copy(alpha = 0.12f) else colors.surface2)
                                .clickable { priority = prio },
                        ) {
                            Box(Modifier.size(8.dp).clip(CircleShape).background(prio.color))
                            Spacer(Modifier.width(6.dp))
                            Text(
                                prio.label,
                                style = txt.small.copy(
                                    fontSize = 13.sp,
                                    fontWeight = if (selected) FontWeight.SemiBold else FontWeight.Normal,
                                ),
                                color = if (selected) prio.color else colors.textMuted,
                            )
                        }
                    }
                }
            }
            Row(verticalAlignment = Alignment.Bottom, modifier = Modifier.fillMaxWidth()) {
                Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    Text("Tanggal & waktu", style = txt.small.copy(fontWeight = FontWeight.SemiBold, fontSize = 12.5.sp), color = colors.textMuted)
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                        modifier = Modifier
                            .clip(RoundedCornerShape(14.dp))
                            .background(colors.surface2)
                            .padding(horizontal = 14.dp, vertical = 10.dp),
                    ) {
                        Text(
                            "Besok, 09:00",
                            style = txt.small.copy(fontWeight = FontWeight.SemiBold),
                            color = colors.text,
                        )
                    }
                }
                Spacer(Modifier.weight(1f))
                Column(
                    verticalArrangement = Arrangement.spacedBy(8.dp),
                    horizontalAlignment = Alignment.End,
                ) {
                    Text("Ingatkan saya", style = txt.small.copy(fontWeight = FontWeight.SemiBold, fontSize = 12.5.sp), color = colors.textMuted)
                    Switch(
                        checked = reminder,
                        onCheckedChange = { reminder = it },
                        colors = SwitchDefaults.colors(
                            checkedTrackColor = colors.primary,
                            checkedThumbColor = Color.White,
                            uncheckedTrackColor = colors.border,
                            uncheckedThumbColor = Color.White,
                        ),
                    )
                }
            }
            PrimaryButton(
                if (editing == null) "Simpan Tugas" else "Simpan Perubahan",
                modifier = Modifier.fillMaxWidth(),
            ) {
                val base = editing
                if (base != null) {
                    TaskRepository.update(
                        base.copy(
                            title = title.ifBlank { base.title },
                            description = note.ifBlank { null },
                            category = category,
                            priority = priority,
                            reminder = reminder,
                        ),
                    )
                } else {
                    TaskRepository.add(
                        Task(
                            id = 0,
                            title = title.ifBlank { "Tugas baru" },
                            category = category,
                            priority = priority,
                            time = "09:00",
                            section = "Hari Ini",
                            description = note.ifBlank { null },
                            reminder = reminder,
                        ),
                    )
                }
                onDismiss()
            }
        }
    }
}
