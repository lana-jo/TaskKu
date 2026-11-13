package com.taskku.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
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
import androidx.compose.material3.Text
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.Categories
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.TaskKuShapes
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.FieldBox
import com.taskku.ui.PrimaryButton

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CategorySheet(
    visible: Boolean,
    onDismiss: () -> Unit,
) {
    if (!visible) return
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)
    var name by remember { mutableStateOf("") }
    var selectedColor by remember { mutableIntStateOf(2) } // amber, sesuai desain

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
                    "Kategori Baru",
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
                Text("Nama kategori", style = txt.small.copy(fontWeight = FontWeight.SemiBold), color = colors.textMuted)
                FieldBox(name, { name = it }, "Nama kategori")
            }
            Column(verticalArrangement = Arrangement.spacedBy(9.dp)) {
                Text("Warna", style = txt.small.copy(fontWeight = FontWeight.SemiBold), color = colors.textMuted)
                Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                    Categories.palette.forEachIndexed { index, hex ->
                        val selected = index == selectedColor
                        if (selected) {
                            Box(
                                contentAlignment = Alignment.Center,
                                modifier = Modifier
                                    .size(36.dp)
                                    .clip(CircleShape)
                                    .background(colors.surface)
                                    .padding(4.dp),
                            ) {
                                Box(Modifier.size(24.dp).clip(CircleShape).background(hex))
                            }
                        } else {
                            Box(
                                modifier = Modifier
                                    .size(28.dp)
                                    .clip(CircleShape)
                                    .background(hex)
                                    .clickable { selectedColor = index },
                            )
                        }
                    }
                }
            }
            Column(verticalArrangement = Arrangement.spacedBy(9.dp)) {
                Text("Pratinjau", style = txt.small.copy(fontWeight = FontWeight.SemiBold), color = colors.textMuted)
                val previewColor = Categories.palette[selectedColor]
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp),
                    modifier = Modifier
                        .clip(RoundedCornerShape(999.dp))
                        .background(previewColor.copy(alpha = 0.14f))
                        .padding(horizontal = 16.dp, vertical = 10.dp),
                ) {
                    Box(Modifier.size(8.dp).clip(CircleShape).background(previewColor))
                    Text(
                        name.ifBlank { "Nama kategori" },
                        style = txt.small.copy(fontSize = 13.5.sp, fontWeight = FontWeight.SemiBold),
                        color = previewColor,
                    )
                }
            }
            PrimaryButton("Simpan Kategori", modifier = Modifier.fillMaxWidth()) {
                if (name.isNotBlank()) {
                    Categories.add(name, Categories.palette[selectedColor])
                }
                onDismiss()
            }
        }
    }
}
