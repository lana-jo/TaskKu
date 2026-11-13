package com.taskku.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
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
import androidx.compose.foundation.text.BasicTextField
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Add
import androidx.compose.material.icons.rounded.BarChart
import androidx.compose.material.icons.rounded.CalendarMonth
import androidx.compose.material.icons.rounded.Check
import androidx.compose.material.icons.rounded.Flag
import androidx.compose.material.icons.rounded.Home
import androidx.compose.material.icons.rounded.Person
import androidx.compose.material.icons.rounded.Schedule
import androidx.compose.material.icons.rounded.Bolt
import androidx.compose.material3.Icon
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.rotate
import androidx.compose.ui.draw.drawBehind
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.Categories
import com.taskku.data.Task
import com.taskku.data.TaskRepository
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.TaskKuShapes
import com.taskku.theme.LocalTaskKuText

@Composable
fun MicroLabel(text: String, modifier: Modifier = Modifier) {
    val txt = LocalTaskKuText.current
    Text(
        text.uppercase(),
        style = txt.micro,
        color = LocalTaskKuColors.current.textMuted,
        modifier = modifier,
    )
}

@Composable
fun TaskKuChip(label: String, selected: Boolean = false, onClick: (() -> Unit)? = null) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier
            .clip(RoundedCornerShape(999.dp))
            .background(if (selected) colors.primary else colors.surface)
            .border(
                width = if (selected) 0.dp else 1.dp,
                color = if (selected) Color.Transparent else colors.border,
                shape = RoundedCornerShape(999.dp),
            )
            .clickable(enabled = onClick != null) { onClick?.invoke() }
            .padding(horizontal = 16.dp, vertical = 8.dp),
    ) {
        Text(
            label,
            style = if (selected) txt.small.copy(
                fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold
            ) else txt.small,
            color = if (selected) colors.primaryFg else colors.textMuted,
        )
    }
}

@Composable
fun PrimaryButton(
    label: String,
    modifier: Modifier = Modifier,
    height: Dp = 54.dp,
    enabled: Boolean = true,
    onClick: () -> Unit,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    // MD3: content padding horizontal 24dp, state disabled = konten 38% di
    // atas container 12% (gradient diganti warna flat saat disabled).
    Box(
        contentAlignment = Alignment.Center,
        modifier = modifier
            .height(height)
            .clip(TaskKuShapes.button)
            .then(
                if (enabled) Modifier.background(colors.gradient)
                else Modifier.background(colors.text.copy(alpha = 0.12f))
            )
            .clickable(enabled = enabled, onClick = onClick)
            .padding(horizontal = 24.dp),
    ) {
        Text(
            label,
            style = txt.bodyMedium.copy(fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold),
            color = if (enabled) colors.primaryFg else colors.text.copy(alpha = 0.38f),
            letterSpacing = (-0.15).sp,
            textAlign = androidx.compose.ui.text.style.TextAlign.Center,
        )
    }
}

@Composable
fun OutlineButton(
    label: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    height: Dp = 54.dp,
    strokeColor: Color = LocalTaskKuColors.current.border,
    textColor: Color = LocalTaskKuColors.current.text,
    icon: ImageVector? = null,
    iconTint: Color = textColor,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Row(
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.Center,
        modifier = modifier
            .height(height)
            .clip(TaskKuShapes.button)
            .background(colors.surface)
            .border(1.dp, strokeColor, TaskKuShapes.button)
            .clickable(onClick = onClick),
    ) {
        if (icon != null) {
            Icon(icon, contentDescription = null, tint = iconTint, modifier = Modifier.size(17.dp))
            Spacer(Modifier.width(8.dp))
        }
        Text(
            label,
            style = txt.bodyMedium.copy(fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold),
            color = textColor,
        )
    }
}

@Composable
fun TaskCard(task: Task, onClick: () -> Unit, onToggle: () -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Surface(
        shape = TaskKuShapes.card,
        color = colors.surface,
        shadowElevation = 4.dp,
        modifier = Modifier
            .fillMaxWidth()
            .clickable(onClick = onClick),
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            modifier = Modifier.padding(horizontal = 16.dp, vertical = 13.dp),
        ) {
            Box(
                contentAlignment = Alignment.Center,
                modifier = Modifier
                    .size(24.dp)
                    .clip(CircleShape)
                    .background(if (task.isDone) colors.success else Color.Transparent)
                    .border(
                        width = if (task.isDone) 0.dp else 2.dp,
                        color = if (task.isDone) Color.Transparent else colors.border,
                        shape = CircleShape,
                    )
                    .clickable(onClick = onToggle),
            ) {
                if (task.isDone) {
                    Icon(
                        Icons.Rounded.Check,
                        contentDescription = null,
                        tint = Color.White,
                        modifier = Modifier.size(13.dp),
                    )
                }
            }
            Spacer(Modifier.width(13.dp))
            Column(Modifier.weight(1f)) {
                Text(
                    task.title,
                    style = if (task.isDone) txt.body else txt.bodyMedium,
                    color = if (task.isDone) colors.textMuted else colors.text,
                    textDecoration = if (task.isDone) TextDecoration.LineThrough else null,
                )
                Spacer(Modifier.height(6.dp))
                Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(5.dp),
                        modifier = Modifier
                            .clip(RoundedCornerShape(999.dp))
                            .background(task.category.soft)
                            .padding(horizontal = 10.dp, vertical = 4.dp),
                    ) {
                        Box(Modifier.size(5.dp).clip(CircleShape).background(task.category.color))
                        Text(
                            task.category.label,
                            style = txt.small.copy(
                                fontSize = 11.sp,
                                fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold,
                            ),
                            color = task.category.color,
                        )
                    }
                    Icon(
                        Icons.Rounded.Schedule,
                        contentDescription = null,
                        tint = colors.textMuted,
                        modifier = Modifier.size(12.5.dp),
                    )
                    Text(task.time, style = txt.small.copy(fontSize = 11.5.sp), color = colors.textMuted)
                }
            }
            Spacer(Modifier.width(13.dp))
            Icon(
                Icons.Rounded.Flag,
                contentDescription = "Prioritas ${task.priority.label}",
                tint = task.priority.color,
                modifier = Modifier.size(15.dp),
            )
        }
    }
}

@Composable
fun HeroCard(modifier: Modifier = Modifier) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val white = Color.White
    Surface(
        shape = TaskKuShapes.hero,
        color = Color.Transparent,
        modifier = modifier.fillMaxWidth(),
    ) {
        Column(
            verticalArrangement = Arrangement.spacedBy(14.dp),
            modifier = Modifier
                .background(colors.gradient)
                .padding(20.dp),
        ) {
            Row(verticalAlignment = Alignment.Top) {
                Column(Modifier.weight(1f)) {
                    val name = com.taskku.data.UserSession.userName
                    Text(
                        "Selamat pagi, ${name ?: "Pengguna"} 👋",
                        style = txt.section.copy(fontSize = 20.sp),
                        color = white,
                    )
                    Spacer(Modifier.height(5.dp))
                    Text(com.taskku.data.todayLabel(), style = txt.small.copy(fontSize = 12.5.sp), color = white.copy(alpha = 0.7f))
                }
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(44.dp)
                        .clip(CircleShape)
                        .background(Color.White.copy(alpha = 0.18f)),
                ) {
                    Text(
                        (com.taskku.data.UserSession.userName ?: "?").take(1).uppercase(),
                        style = txt.section,
                        color = white,
                    )
                }
            }
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp),
                    modifier = Modifier
                        .clip(RoundedCornerShape(999.dp))
                        .background(Color.White.copy(alpha = 0.17f))
                        .padding(horizontal = 12.dp, vertical = 7.dp),
                ) {
                    Icon(Icons.Rounded.Bolt, contentDescription = null, tint = Color(0xFFFFD66B), modifier = Modifier.size(13.dp))
                    Text("12 hari streak", style = txt.small.copy(fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold, fontSize = 11.5.sp), color = white)
                }
                Row(
                    modifier = Modifier
                        .clip(RoundedCornerShape(999.dp))
                        .background(Color.White.copy(alpha = 0.17f))
                        .padding(horizontal = 12.dp, vertical = 7.dp),
                ) {
                    Text(
                        "${TaskRepository.tasks.count { !it.isDone }} tugas aktif",
                        style = txt.small.copy(fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold, fontSize = 11.5.sp),
                        color = white,
                    )
                }
            }
        }
    }
}

@Composable
fun Ring(pct: Int, size: Dp, modifier: Modifier = Modifier, labelSize: androidx.compose.ui.unit.TextUnit = 13.sp) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Box(contentAlignment = Alignment.Center, modifier = modifier.size(size)) {
        CanvasPlaceholder(size, pct, colors.primary, colors.border)
        Text("$pct%", style = txt.bodyMedium.copy(fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold, fontSize = labelSize), color = colors.text)
    }
}

@androidx.compose.runtime.Composable
private fun CanvasPlaceholder(size: Dp, pct: Int, progressColor: Color, trackColor: Color) {
    androidx.compose.foundation.Canvas(modifier = Modifier.size(size)) {
        val stroke = this.size.minDimension * 0.13f
        val inset = stroke / 2
        drawArc(
            color = trackColor,
            startAngle = 0f,
            sweepAngle = 360f,
            useCenter = false,
            topLeft = Offset(inset, inset),
            size = androidx.compose.ui.geometry.Size(this.size.width - stroke, this.size.height - stroke),
            style = Stroke(width = stroke, cap = StrokeCap.Butt),
        )
        drawArc(
            color = progressColor,
            startAngle = -90f,
            sweepAngle = 360f * pct / 100f,
            useCenter = false,
            topLeft = Offset(inset, inset),
            size = androidx.compose.ui.geometry.Size(this.size.width - stroke, this.size.height - stroke),
            style = Stroke(width = stroke, cap = StrokeCap.Round),
        )
    }
}

@Composable
fun ProgressCard(pct: Int, done: Int, total: Int, note: String, modifier: Modifier = Modifier) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Surface(shape = TaskKuShapes.card, color = colors.surface, shadowElevation = 4.dp, modifier = modifier.fillMaxWidth()) {
        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.padding(horizontal = 18.dp, vertical = 16.dp)) {
            Ring(pct, 62.dp)
            Spacer(Modifier.width(16.dp))
            Column {
                MicroLabel("Progres hari ini")
                Spacer(Modifier.height(4.dp))
                Text("$done dari $total selesai", style = txt.section, color = colors.text)
                Spacer(Modifier.height(2.dp))
                Text(note, style = txt.small.copy(fontSize = 11.5.sp), color = colors.textMuted)
            }
        }
    }
}

private val dockItems = listOf(
    "Beranda" to Icons.Rounded.Home,
    "Tugas" to Icons.Rounded.Flag,
    "Kalender" to Icons.Rounded.CalendarMonth,
    "Statistik" to Icons.Rounded.BarChart,
    "Profil" to Icons.Rounded.Person,
)

@Composable
fun DockBar(active: String, onSelect: (String) -> Unit, modifier: Modifier = Modifier) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Surface(
        shape = RoundedCornerShape(999.dp),
        color = colors.surface,
        shadowElevation = 16.dp,
        modifier = modifier.fillMaxWidth().height(64.dp),
    ) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween,
            modifier = Modifier.padding(horizontal = 10.dp),
        ) {
            dockItems.forEach { (label, icon) ->
                val isActive = label == active
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(6.dp),
                    modifier = Modifier
                        .clip(RoundedCornerShape(999.dp))
                        .background(if (isActive) colors.primarySoft else Color.Transparent)
                        .clickable { onSelect(label) }
                        .padding(horizontal = if (isActive) 14.dp else 6.dp, vertical = 10.dp),
                ) {
                    Icon(
                        icon,
                        contentDescription = label,
                        tint = if (isActive) colors.primary else colors.textMuted,
                        modifier = Modifier.size(20.dp),
                    )
                    Text(
                        label,
                        style = txt.small.copy(
                            fontSize = 11.sp,
                            fontWeight = if (isActive) androidx.compose.ui.text.font.FontWeight.SemiBold else androidx.compose.ui.text.font.FontWeight.Normal,
                        ),
                        color = if (isActive) colors.primary else colors.textMuted,
                    )
                }
            }
        }
    }
}

@Composable
fun FabButton(
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    icon: ImageVector = Icons.Rounded.Add,
    rotation: Float = 0f,
) {
    val colors = LocalTaskKuColors.current
    Box(
        contentAlignment = Alignment.Center,
        modifier = modifier
            .size(58.dp)
            .shadow(20.dp, CircleShape, spotColor = Color(0xFF5B54F0), ambientColor = Color(0x335B54F0))
            .clip(CircleShape)
            .background(colors.gradient)
            .clickable(onClick = onClick),
    ) {
        Icon(
            icon,
            contentDescription = "Tugas baru",
            tint = Color.White,
            modifier = Modifier.size(26.dp).rotate(rotation),
        )
    }
}

@Composable
fun SectionHeader(title: String, count: Int, modifier: Modifier = Modifier, action: String? = null, onAction: (() -> Unit)? = null) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Row(verticalAlignment = Alignment.CenterVertically, modifier = modifier.fillMaxWidth()) {
        Text(title, style = txt.section, color = colors.text)
        Spacer(Modifier.width(8.dp))
        Box(
            modifier = Modifier
                .clip(RoundedCornerShape(999.dp))
                .background(colors.surface2)
                .padding(horizontal = 9.dp, vertical = 3.dp),
        ) {
            Text("$count", style = txt.small.copy(fontSize = 11.sp, fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold), color = colors.textMuted)
        }
        Spacer(Modifier.weight(1f))
        if (action != null && onAction != null) {
            Text(action, style = txt.small.copy(fontWeight = androidx.compose.ui.text.font.FontWeight.SemiBold), color = colors.primary, modifier = Modifier.clickable(onClick = onAction))
        }
    }
}

@Composable
fun FieldBox(
    value: String,
    onValueChange: (String) -> Unit,
    placeholder: String,
    modifier: Modifier = Modifier,
    height: Dp = 56.dp,
    leading: (@Composable () -> Unit)? = null,
    trailing: (@Composable () -> Unit)? = null,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = modifier
            .height(height)
            .clip(TaskKuShapes.field)
            .background(colors.surface2)
            .padding(horizontal = 18.dp),
    ) {
        if (leading != null) {
            leading()
            Spacer(Modifier.width(12.dp))
        }
        Box(Modifier.weight(1f)) {
            if (value.isEmpty()) {
                Text(placeholder, style = txt.body, color = colors.textMuted)
            }
            BasicTextField(
                value = value,
                onValueChange = onValueChange,
                textStyle = txt.body.copy(color = colors.text),
                singleLine = height <= 56.dp,
                modifier = Modifier.fillMaxWidth(),
            )
        }
        if (trailing != null) {
            Spacer(Modifier.width(8.dp))
            trailing()
        }
    }
}

