package com.taskku

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import com.taskku.data.AppSettings
import com.taskku.data.Task
import com.taskku.data.TaskRepository
import androidx.compose.foundation.isSystemInDarkTheme
import com.taskku.theme.TaskKuTheme
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

@Composable
fun App() {
    // Persisten (tabel settings): null = ikut tema sistem.
    var darkOverride by remember { mutableStateOf(AppSettings.darkOverride) }
    TaskKuTheme(darkTheme = darkOverride ?: isSystemInDarkTheme()) {
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
                onDarkOverrideChange = {
                    darkOverride = it
                    AppSettings.setDarkOverride(it)
                },
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
}
