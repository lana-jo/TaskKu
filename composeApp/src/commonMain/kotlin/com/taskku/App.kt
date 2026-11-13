package com.taskku

import androidx.compose.foundation.background
import androidx.compose.foundation.isSystemInDarkTheme
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
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
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
import androidx.compose.ui.layout.onSizeChanged
import androidx.compose.ui.unit.dp
import com.taskku.data.AppSettings
import com.taskku.data.Task
import com.taskku.data.TaskRepository
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.LocalTaskKuText
import com.taskku.theme.TaskKuTheme
import com.taskku.ui.DesktopHeader
import com.taskku.ui.SideNav
import com.taskku.ui.TaskCard
import com.taskku.ui.screens.AddTaskSheet
import com.taskku.ui.screens.CategorySheet
import com.taskku.ui.screens.FabSpeedDial
import com.taskku.ui.screens.ReminderSheet
import com.taskku.ui.screens.CalendarScreen
import com.taskku.ui.screens.ProfileScreen
import com.taskku.ui.screens.StatisticsScreen
import com.taskku.ui.screens.HomeScreen
import com.taskku.ui.screens.TaskDetailScreen

sealed interface Screen {
    data object Home : Screen
    data class Detail(val taskId: Int) : Screen
}

/** Aturan breakpoint TaskKu (sesuai halaman Responsive di desain FigCraft). */
data class ResponsiveLayout(
    /** >= 1024: sidebar 3 item + kanban; Profil & Keluar di dropdown header. */
    val isDesktop: Boolean,
    /** >= 720: daftar tugas 2 kolom (tablet), di bawah itu 1 kolom. */
    val twoColumns: Boolean,
)

/**
 * < 600 ponsel (1 kolom, bottom nav) · 600–1023 tablet (bottom nav,
 * 2 kolom mulai 720) · >= 1024 desktop (sidebar + kanban).
 */
fun responsiveLayoutOf(widthPx: Int, density: Float): ResponsiveLayout {
    val w = widthPx / density
    return ResponsiveLayout(isDesktop = w >= 1024, twoColumns = w >= 720)
}

@Composable
fun App() {
    // Persisten (tabel settings): null = ikut tema sistem.
    var darkOverride by remember { mutableStateOf(AppSettings.darkOverride) }
    TaskKuTheme(darkTheme = darkOverride ?: isSystemInDarkTheme()) {
        AppContent(darkOverride) {
            darkOverride = it
            AppSettings.setDarkOverride(it)
        }
    }
}

@Composable
private fun AppContent(darkOverride: Boolean?, onDarkOverrideChange: (Boolean?) -> Unit) {
    val density = androidx.compose.ui.platform.LocalDensity.current
    var widthPx by remember { mutableStateOf(0) }
    Box(
        Modifier
            .fillMaxSize()
            .onSizeChanged { widthPx = it.width },
    ) {
        if (widthPx > 0) {
            val layout = responsiveLayoutOf(widthPx, density.density)
            if (layout.isDesktop) DesktopApp() else MobileApp(layout, darkOverride, onDarkOverrideChange)
        }
    }
}

@Composable
private fun MobileApp(layout: ResponsiveLayout, darkOverride: Boolean?, onDarkOverrideChange: (Boolean?) -> Unit) {
    var screen by remember { mutableStateOf<Screen>(Screen.Home) }
    var showSheet by remember { mutableStateOf(false) }
    var editing by remember { mutableStateOf<Task?>(null) }
    var tab by remember { mutableStateOf("Beranda") }
    var speedDial by remember { mutableStateOf(false) }
    var showCategorySheet by remember { mutableStateOf(false) }
    var showReminderSheet by remember { mutableStateOf(false) }

    fun openSpeedDial() {
        editing = null
        speedDial = true
    }

    when (val current = screen) {
        Screen.Home -> HomeScreen(
            tab = tab,
            twoColumns = layout.twoColumns,
            onTabChange = { tab = it },
            onOpenTask = { screen = Screen.Detail(it) },
            onAdd = { openSpeedDial() },
        )
        is Screen.Detail -> TaskDetailScreen(
            taskId = current.taskId,
            onBack = { screen = Screen.Home },
            onEdit = { task ->
                editing = task
                showSheet = true
            },
        )
    }

    when (tab) {
        "Kalender" -> CalendarScreen(
            tab = tab,
            onTabChange = { tab = it },
            onAdd = { openSpeedDial() },
            onOpenTask = { screen = Screen.Detail(it) },
        )
        "Statistik" -> StatisticsScreen(
            tab = tab,
            onTabChange = { tab = it },
            onAdd = { openSpeedDial() },
        )
        "Profil" -> ProfileScreen(
            tab = tab,
            onTabChange = { tab = it },
            darkOverride = darkOverride,
            onDarkOverrideChange = onDarkOverrideChange,
        )
    }

    AddTaskSheet(
        visible = showSheet,
        editing = editing,
        onDismiss = {
            showSheet = false
            editing = null
        },
    )
    CategorySheet(
        visible = showCategorySheet,
        onDismiss = { showCategorySheet = false },
    )
    ReminderSheet(
        visible = showReminderSheet,
        onDismiss = { showReminderSheet = false },
    )
    FabSpeedDial(
        expanded = speedDial,
        onDismiss = { speedDial = false },
        onAction = { action ->
            speedDial = false
            when (action) {
                "Tugas Baru" -> {
                    editing = null
                    showSheet = true
                }
                "Kategori Baru" -> showCategorySheet = true
                "Pengingat" -> showReminderSheet = true
            }
        },
    )
}

@Composable
private fun DesktopApp() {
    var screen by remember { mutableStateOf<Screen>(Screen.Home) }
    var showSheet by remember { mutableStateOf(false) }
    var editing by remember { mutableStateOf<Task?>(null) }
    var tab by remember { mutableStateOf("Beranda") }
    var speedDial by remember { mutableStateOf(false) }
    var showCategorySheet by remember { mutableStateOf(false) }
    var showReminderSheet by remember { mutableStateOf(false) }

    fun openSpeedDial() {
        editing = null
        speedDial = true
    }

    val colors = LocalTaskKuColors.current
    Row(
        modifier = Modifier
            .fillMaxSize()
            .background(colors.bg),
    ) {
        SideNav(active = tab, onSelect = { tab = it })
        Column(
            modifier = Modifier
                .weight(1f)
                .padding(30.dp),
        ) {
            DesktopHeader(
                title = when (tab) {
                    "Kalender" -> "Kalender"
                    "Statistik" -> "Statistik"
                    "Profil" -> "Profil"
                    else -> "Hari Ini"
                },
                subtitle = "Jumat, 13 November 2026 — 5 tugas aktif (demo)",
                onProfile = { tab = "Profil" },
                onLogout = { /* menyusul bersama alur auth */ },
                onAdd = { openSpeedDial() },
            )
            Spacer(Modifier.height(22.dp))
            Box(Modifier.weight(1f)) {
                when (tab) {
                    "Kalender" -> CalendarScreen(
                        tab = tab,
                        onTabChange = { tab = it },
                        onAdd = { openSpeedDial() },
                        onOpenTask = { screen = Screen.Detail(it) },
                    )
                    "Statistik" -> StatisticsScreen(
                        tab = tab,
                        onTabChange = { tab = it },
                        onAdd = { openSpeedDial() },
                    )
                    "Profil" -> ProfileScreen(
                        tab = tab,
                        onTabChange = { tab = it },
                        darkOverride = null,
                        onDarkOverrideChange = { },
                    )
                    else -> when (val current = screen) {
                        is Screen.Detail -> TaskDetailScreen(
                            taskId = current.taskId,
                            onBack = { screen = Screen.Home },
                            onEdit = { task ->
                                editing = task
                                showSheet = true
                            },
                        )
                        else -> DesktopKanban { screen = Screen.Detail(it) }
                    }
                }
            }
        }
    }

    AddTaskSheet(
        visible = showSheet,
        editing = editing,
        onDismiss = {
            showSheet = false
            editing = null
        },
    )
    CategorySheet(visible = showCategorySheet, onDismiss = { showCategorySheet = false })
    ReminderSheet(visible = showReminderSheet, onDismiss = { showReminderSheet = false })
    FabSpeedDial(
        expanded = speedDial,
        onDismiss = { speedDial = false },
        onAction = { action ->
            speedDial = false
            when (action) {
                "Tugas Baru" -> {
                    editing = null
                    showSheet = true
                }
                "Kategori Baru" -> showCategorySheet = true
                "Pengingat" -> showReminderSheet = true
            }
        },
    )
}

@Composable
private fun DesktopKanban(onOpenTask: (Int) -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    val columns = listOf(
        Triple("Hari Ini", Color(0xFF5B54F0), TaskRepository.tasks.filter { it.section == "Hari Ini" && !it.isDone }),
        Triple("Terjadwal", Color(0xFFF79009), TaskRepository.tasks.filter { it.section == "Besok" }),
        Triple("Selesai", Color(0xFF12B76A), TaskRepository.tasks.filter { it.isDone }),
    )
    Row(
        horizontalArrangement = Arrangement.spacedBy(14.dp),
        modifier = Modifier.fillMaxSize(),
    ) {
        columns.forEach { (title, accent, tasks) ->
            Surface(
                shape = RoundedCornerShape(20.dp),
                color = colors.surface2,
                modifier = Modifier.weight(1f),
            ) {
                Column(
                    verticalArrangement = Arrangement.spacedBy(10.dp),
                    modifier = Modifier.padding(12.dp),
                ) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                        modifier = Modifier.padding(start = 4.dp, top = 8.dp, end = 8.dp, bottom = 8.dp),
                    ) {
                        Box(
                            modifier = Modifier
                                .size(10.dp)
                                .clip(CircleShape)
                                .background(accent),
                        )
                        Text(title, style = txt.section)
                        Spacer(Modifier.weight(1f))
                        Text("${tasks.size}", style = txt.small)
                    }
                    LazyColumn(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        items(tasks) { task ->
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
    }
}
