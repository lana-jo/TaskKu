package com.taskku.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Add
import androidx.compose.material.icons.automirrored.rounded.Logout
import androidx.compose.material.icons.rounded.BarChart
import androidx.compose.material.icons.rounded.CalendarMonth
import androidx.compose.material.icons.rounded.Check
import androidx.compose.material.icons.rounded.Flag
import androidx.compose.material.icons.rounded.ChevronRight
import androidx.compose.material.icons.rounded.Home
import androidx.compose.material.icons.rounded.Person
import androidx.compose.material3.Icon
import androidx.compose.material3.Surface
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
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.startOfWeek
import com.taskku.data.today
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.TaskKuShapes
import com.taskku.theme.LocalTaskKuText

private val sideNavItems = listOf(
    "Beranda" to Icons.Rounded.Home,
    "Tugas" to Icons.Rounded.Flag,
    "Kalender" to Icons.Rounded.CalendarMonth,
    "Statistik" to Icons.Rounded.BarChart,
)

/**
 * Sidebar desktop (>= 1024px): logo, 3 menu, daftar proyek/kategori,
 * progres mingguan, spacer, tanpa baris user (Profil & Keluar ada di
 * dropdown avatar pada header — aturan responsive desain).
 */
@Composable
fun SideNav(
    active: String,
    onSelect: (String) -> Unit,
    modifier: Modifier = Modifier,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Surface(
        color = colors.surface,
        modifier = modifier.width(272.dp).fillMaxHeight(),
    ) {
        Column(
            modifier = Modifier
                .padding(24.dp)
                .fillMaxHeight(),
        ) {
            Row(
                verticalAlignment = Alignment.CenterVertically,
                modifier = Modifier.padding(bottom = 14.dp),
            ) {
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(42.dp)
                        .clip(RoundedCornerShape(14.dp))
                        .background(colors.gradient),
                ) {
                    Icon(Icons.Rounded.Check, contentDescription = null, tint = Color.White, modifier = Modifier.size(22.dp))
                }
                Spacer(Modifier.width(11.dp))
                Text("TaskKu", style = txt.judul.copy(fontSize = 21.sp), color = colors.text)
            }
            sideNavItems.forEach { (label, icon) ->
                val isActive = label == active
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(12.dp),
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(46.dp)
                        .clip(RoundedCornerShape(14.dp))
                        .background(if (isActive) colors.primarySoft else Color.Transparent)
                        .clickable { onSelect(label) }
                        .padding(horizontal = 14.dp),
                ) {
                    Icon(
                        icon,
                        contentDescription = label,
                        tint = if (isActive) colors.primary else colors.textMuted,
                        modifier = Modifier.size(19.dp),
                    )
                    Text(
                        label,
                        style = txt.body.copy(
                            fontSize = 14.5.sp,
                            fontWeight = if (isActive) FontWeight.SemiBold else FontWeight.Normal,
                        ),
                        color = if (isActive) colors.primary else colors.text,
                    )
                }
            }
            Text(
                "KATEGORI",
                style = txt.micro,
                color = colors.textMuted,
                modifier = Modifier.padding(start = 14.dp, top = 18.dp, bottom = 6.dp),
            )
            com.taskku.data.Categories.all.forEach { cat ->
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(10.dp),
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(40.dp)
                        .clip(RoundedCornerShape(12.dp))
                        .clickable { }
                        .padding(horizontal = 14.dp),
                ) {
                    Box(Modifier.size(9.dp).clip(androidx.compose.foundation.shape.CircleShape).background(cat.color))
                    Text(cat.label, style = txt.body.copy(fontSize = 13.5.sp), color = colors.text, modifier = Modifier.weight(1f))
                    val count = com.taskku.data.TaskRepository.tasks.count { it.category.label == cat.label }
                    if (count > 0) {
                        Box(
                            modifier = Modifier
                                .clip(RoundedCornerShape(999.dp))
                                .background(colors.surface2)
                                .padding(horizontal = 8.dp, vertical = 2.dp),
                        ) {
                            Text("$count", style = txt.small.copy(fontSize = 11.sp, fontWeight = FontWeight.SemiBold), color = colors.textMuted)
                        }
                    }
                }
            }
            Spacer(Modifier.weight(1f))
            // Kartu progres mingguan: selesai vs total tugas minggu berjalan (live dari repo).
            val today = com.taskku.data.today()
            val weekStart = today.startOfWeek()
            val weekTasks = com.taskku.data.TaskRepository.tasks.filter { it.date >= weekStart }
            val weekDone = weekTasks.count { it.isDone }
            val weekPct = if (weekTasks.isEmpty()) 0f else weekDone.toFloat() / weekTasks.size
            Column(
                verticalArrangement = Arrangement.spacedBy(8.dp),
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(16.dp))
                    .background(colors.surface2)
                    .padding(16.dp),
            ) {
                Text("PROGRES MINGGU INI", style = txt.micro, color = colors.textMuted)
                Text("$weekDone dari ${weekTasks.size} tugas", style = txt.section, color = colors.text)
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(6.dp)
                        .clip(RoundedCornerShape(999.dp))
                        .background(colors.border),
                ) {
                    Box(
                        Modifier
                            .fillMaxWidth(weekPct)
                            .height(6.dp)
                            .clip(RoundedCornerShape(999.dp))
                            .background(colors.primary),
                    )
                }
            }
        }
    }
}

/**
 * Header desktop: judul + pencarian + bell + avatar dengan dropdown
 * (Lihat Profil / Keluar) — sesuai aturan: di desktop, Profil & Keluar
 * berada di dropdown avatar, bukan di navigasi.
 */
@Composable
fun DesktopHeader(
    title: String,
    subtitle: String,
    onProfile: () -> Unit,
    onLogout: () -> Unit,
    onAdd: () -> Unit,
    modifier: Modifier = Modifier,
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    var dropdownOpen by remember { mutableStateOf(false) }
    Box(modifier.fillMaxWidth()) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Column(modifier = Modifier.weight(1f)) {
                Text(title, style = txt.display.copy(fontSize = 27.sp), color = colors.text)
                Spacer(Modifier.height(5.dp))
                Text(subtitle, style = txt.small.copy(fontSize = 13.5.sp), color = colors.textMuted)
            }
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(10.dp),
            ) {
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(58.dp)
                        .clip(TaskKuShapes.button)
                        .background(colors.primary)
                        .clickable(onClick = onAdd),
                ) {
                    Icon(Icons.Rounded.Add, contentDescription = "Tugas baru", tint = colors.primaryFg, modifier = Modifier.size(22.dp))
                }
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier
                        .size(46.dp)
                        .clip(androidx.compose.foundation.shape.CircleShape)
                        .background(colors.gradient)
                        .clickable { dropdownOpen = !dropdownOpen },
                ) {
                    Text("R", style = txt.section, color = Color.White)
                }
                Icon(
                    Icons.Rounded.ChevronRight,
                    contentDescription = if (dropdownOpen) "Tutup menu" else "Buka menu",
                    tint = colors.textMuted,
                    modifier = Modifier
                        .size(14.dp)
                        .clickable { dropdownOpen = !dropdownOpen },
                )
            }
        }
        if (dropdownOpen) {
            // Scrim tak terlihat untuk menutup dropdown saat klik di luar
            Box(
                Modifier
                    .matchParentSize()
                    .clickable { dropdownOpen = false },
            )
            Surface(
                shape = RoundedCornerShape(16.dp),
                color = colors.surface,
                shadowElevation = 16.dp,
                modifier = Modifier
                    .align(Alignment.TopEnd)
                    .padding(top = 64.dp)
                    .width(264.dp),
            ) {
                Column(modifier = Modifier.padding(10.dp)) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(10.dp),
                        modifier = Modifier.padding(8.dp).padding(bottom = 12.dp),
                    ) {
                        Box(
                            contentAlignment = Alignment.Center,
                            modifier = Modifier
                                .size(40.dp)
                                .clip(androidx.compose.foundation.shape.CircleShape)
                                .background(colors.gradient),
                        ) {
                            Text(
                                (com.taskku.data.UserSession.userName ?: "?").take(1).uppercase(),
                                style = txt.bodyMedium,
                                color = Color.White,
                            )
                        }
                        Column {
                            Text(
                                com.taskku.data.UserSession.userName ?: "Pengguna",
                                style = txt.bodyMedium.copy(fontSize = 13.5.sp),
                                color = colors.text,
                            )
                            Text(
                                "pengguna@taskku",
                                style = txt.small.copy(fontSize = 10.5.sp),
                                color = colors.textMuted,
                            )
                        }
                    }
                    Box(Modifier.fillMaxWidth().height(1.dp).background(colors.border))
                    DropdownItem(Icons.Rounded.Person, "Lihat Profil", colors.text) {
                        dropdownOpen = false
                        onProfile()
                    }
                    DropdownItem(Icons.AutoMirrored.Rounded.Logout, "Keluar", colors.danger, semibold = true) {
                        dropdownOpen = false
                        onLogout()
                    }
                }
            }
        }
    }
}

@Composable
private fun DropdownItem(icon: ImageVector, label: String, tint: Color, semibold: Boolean = false, onClick: () -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Row(
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(10.dp),
        modifier = Modifier
            .fillMaxWidth()
            .height(40.dp)
            .clip(RoundedCornerShape(10.dp))
            .clickable(onClick = onClick)
            .padding(horizontal = 10.dp),
    ) {
        Icon(icon, contentDescription = null, tint = tint, modifier = Modifier.size(16.dp))
        Text(
            label,
            style = txt.body.copy(
                fontSize = 13.5.sp,
                fontWeight = if (semibold) FontWeight.SemiBold else FontWeight.Normal,
            ),
            color = tint,
        )
    }
}
