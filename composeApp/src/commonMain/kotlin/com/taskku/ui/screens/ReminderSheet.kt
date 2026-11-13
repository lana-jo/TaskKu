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
fun ReminderSheet(
    visible: Boolean,
    onDismiss: () -> Unit,
) {
    if (!visible) return
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)
    var text by remember { mutableStateOf("") }
    var notif by remember { mutableStateOf(true) }
    var repeat by remember { mutableStateOf(0) }

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
                        .fillMaxWidth()
                        .height(4.5.dp)
                        .clip(RoundedCornerShape(999.dp))
                        .background(colors.border),
                )
            }
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    "Pengingat Cepat",
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
                    Icon(Icons.Rounded.Close, contentDescription = "Tutup", tint = colors.textMuted, modifier = Modifier.size(15.dp))
                }
            }
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text("Pengingat", style = txt.small.copy(fontWeight = FontWeight.SemiBold), color = colors.textMuted)
                FieldBox(text, { text = it }, "Minum air putih")
            }
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                Text("Waktu", style = txt.small.copy(fontWeight = FontWeight.SemiBold), color = colors.textMuted)
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier
                        .clip(RoundedCornerShape(14.dp))
                        .background(colors.surface2)
                        .padding(horizontal = 14.dp, vertical = 10.dp),
                ) {
                    Text("Hari ini, 17:00", style = txt.small.copy(fontWeight = FontWeight.SemiBold), color = colors.text)
                }
            }
            Column(verticalArrangement = Arrangement.spacedBy(9.dp)) {
                Text("Ulangi", style = txt.small.copy(fontWeight = FontWeight.SemiBold), color = colors.textMuted)
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    listOf("Sekali", "Harian", "Mingguan").forEachIndexed { index, label ->
                        TaskKuChipLike(label, selected = repeat == index) { repeat = index }
                    }
                }
            }
            Row(
                verticalAlignment = Alignment.CenterVertically,
                modifier = Modifier.fillMaxWidth(),
            ) {
                Text("Notifikasi pengingat", style = txt.body, color = colors.text, modifier = Modifier.weight(1f))
                Switch(
                    checked = notif,
                    onCheckedChange = { notif = it },
                    colors = SwitchDefaults.colors(
                        checkedTrackColor = colors.primary,
                        checkedThumbColor = Color.White,
                        uncheckedTrackColor = colors.border,
                        uncheckedThumbColor = Color.White,
                    ),
                )
            }
            PrimaryButton("Atur Pengingat", modifier = Modifier.fillMaxWidth()) {
                if (text.isNotBlank()) {
                    // Pengingat cepat disimpan sebagai tugas ber-pengingat (v1: satu-waktu, hari ini)
                    TaskRepository.add(
                        Task(
                            id = 0,
                            title = text,
                            category = Categories.Pribadi,
                            priority = Priorities.Sedang,
                            time = "17:00",
                            section = "Hari Ini",
                            reminder = notif,
                        ),
                    )
                }
                onDismiss()
            }
        }
    }
}

@Composable
private fun TaskKuChipLike(label: String, selected: Boolean, onClick: () -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Box(
        contentAlignment = Alignment.Center,
        modifier = Modifier
            .clip(RoundedCornerShape(999.dp))
            .background(if (selected) colors.primary else colors.surface)
            .clickable(onClick = onClick)
            .padding(horizontal = 16.dp, vertical = 8.dp),
    ) {
        Text(
            label,
            style = txt.small.copy(
                fontWeight = if (selected) FontWeight.SemiBold else FontWeight.Normal,
            ),
            color = if (selected) colors.primaryFg else colors.textMuted,
        )
    }
}
