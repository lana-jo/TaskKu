package com.taskku.data

import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.snapshots.SnapshotStateList
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import kotlinx.datetime.DatePeriod
import kotlinx.datetime.LocalDate
import kotlinx.datetime.plus

data class Category(val label: String, val color: Color, val soft: Color)

data class Priority(val label: String, val color: Color)

data class Subtask(val title: String, val isDone: Boolean = false)

data class Task(
    val id: Int,
    val title: String,
    val category: Category,
    val priority: Priority,
    val time: String,
    val section: String,
    val isDone: Boolean = false,
    val description: String? = null,
    val subtasks: List<Subtask> = emptyList(),
    val reminder: Boolean = false,
    /** Tanggal tugas dalam format ISO yyyy-MM-dd (untuk kalender). */
    val date: LocalDate = today(),
)

// ARGB Long untuk menyimpan warna ke database
internal fun argbOf(color: Color): Long = color.toArgb().toLong() and 0xFFFFFFFFL
internal fun colorOf(argb: Long): Color = Color(argb)

// Boolean ↔ INTEGER 0/1 (kolom skema tidak memakai `AS Boolean`)
internal fun flagOf(value: Boolean): Long = if (value) 1L else 0L
internal fun flagValue(flag: Long): Boolean = flag != 0L

// Warna kategori & prioritas statis (sesuai desain — tidak ikut mode gelap)
object Categories {
    val Pekerjaan = Category("Pekerjaan", Color(0xFF5B54F0), Color(0xFFECEBFE))
    val Pribadi = Category("Pribadi", Color(0xFF0E9F6E), Color(0xFFE5F6EF))
    val Belanja = Category("Belanja", Color(0xFFDC8A0E), Color(0xFFFDF2E1))
    val Kesehatan = Category("Kesehatan", Color(0xFFE5484D), Color(0xFFFDEBEB))
    val palette = listOf(
        Color(0xFF5B54F0), Color(0xFF0E9F6E), Color(0xFFDC8A0E),
        Color(0xFFE5484D), Color(0xFF0E7490),
    )

    private val default = listOf(Pekerjaan, Pribadi, Belanja, Kesehatan)

    private val _all = mutableStateListOf<Category>()
    val all: List<Category> get() {
        ensureLoaded()
        return _all
    }

    private var loaded = false

    internal fun ensureLoaded() {
        if (loaded) return
        val queries = TaskDbHolder.db?.taskQueries
        if (queries == null) {
            _all.addAll(default)
        } else {
            if (queries.selectCategories().executeAsList().isEmpty()) {
                default.forEach { queries.insertCategory(it.label, argbOf(it.color)) }
            }
            queries.selectCategories().executeAsList().forEach { row ->
                _all.add(Category(row.label, colorOf(row.color), colorOf(row.color).copy(alpha = 0.14f)))
            }
        }
        loaded = true
    }

    fun add(label: String, color: Color): Category {
        _all.firstOrNull { it.label.equals(label, ignoreCase = true) }?.let { return it }
        val category = Category(label.trim(), color, color.copy(alpha = 0.14f))
        _all.add(category)
        TaskDbHolder.db?.taskQueries?.insertCategory(category.label, argbOf(category.color))
        return category
    }
}

object Priorities {
    val Tinggi = Priority("Tinggi", Color(0xFFE5484D))
    val Sedang = Priority("Sedang", Color(0xFFF79009))
    val Rendah = Priority("Rendah", Color(0xFF12B76A))
    val all = listOf(Tinggi, Sedang, Rendah)
}

object TaskRepository {
    val sections = listOf("Hari Ini", "Besok")

    private val queries get() = TaskDbHolder.db?.taskQueries

    private val _tasks: SnapshotStateList<Task> = mutableStateListOf()
    val tasks: SnapshotStateList<Task> = _tasks

    private var nextId = 1

    // Data awal; dipakai sebagai seeder saat database baru pertama kali dibuat.
    // Tanggal seed relatif terhadap hari ini, jadi section selalu konsisten.
    private val seedTasks: List<Task>
        get() {
            val tomorrow = today().plus(DatePeriod(days = 1))
            return listOf(
                Task(
                    id = 1, title = "Kirim laporan mingguan", category = Categories.Pekerjaan,
                    priority = Priorities.Rendah, time = "08:00", section = "Hari Ini", isDone = true,
                    description = "Rekap progres pekerjaan minggu ini untuk dibagikan ke tim.",
                ),
                Task(
                    id = 2, title = "Rapat sprint dengan tim desain", category = Categories.Pekerjaan,
                    priority = Priorities.Tinggi, time = "09:00", section = "Hari Ini",
                    description = "Menyiapkan materi sprint review: progres desain, umpan balik pengguna, dan rencana iterasi berikutnya.",
                    subtasks = listOf(
                        Subtask("Siapkan deck terbaru", isDone = true),
                        Subtask("Review umpan balik desain"),
                        Subtask("Kirim undangan rapat"),
                    ),
                    reminder = true,
                ),
                Task(
                    id = 3, title = "Belanja bulanan di pasar", category = Categories.Belanja,
                    priority = Priorities.Sedang, time = "16:00", section = "Hari Ini",
                ),
                Task(
                    id = 4, title = "Kontrol dokter gigi", category = Categories.Kesehatan,
                    priority = Priorities.Tinggi, time = "08:30", section = "Besok", date = tomorrow,
                ),
                Task(
                    id = 5, title = "Olahraga pagi: lari 5 km", category = Categories.Pribadi,
                    priority = Priorities.Rendah, time = "06:00", section = "Besok", date = tomorrow,
                ),
            )
        }

    init {
        Categories.ensureLoaded()
        val queries = queries
        if (queries == null) {
            // Platform tanpa storage (wasmJs): perilaku lama, in-memory.
            _tasks.addAll(seedTasks)
        } else if (queries.countTasks().executeAsOne() == 0L) {
            seedTasks.forEach { add(it) }
        } else {
            reload()
        }
        nextId = (_tasks.maxOfOrNull { it.id } ?: 0) + 1
    }

    fun byId(id: Int): Task? = _tasks.firstOrNull { it.id == id }

    fun add(task: Task) {
        val withId = task.copy(id = nextId++)
        persist(withId)
        _tasks.add(withId)
    }

    fun update(task: Task) {
        val index = _tasks.indexOfFirst { it.id == task.id }
        if (index >= 0) {
            _tasks[index] = task
            persist(task)
        }
    }

    fun delete(id: Int) {
        _tasks.removeAll { it.id == id }
        val db = TaskDbHolder.db ?: return
        db.transaction {
            db.taskQueries.deleteSubtasksOfTask(id.toLong())
            db.taskQueries.deleteTask(id.toLong())
        }
    }

    fun toggleDone(id: Int) {
        val index = _tasks.indexOfFirst { it.id == id }
        if (index < 0) return
        val updated = _tasks[index].copy(isDone = !_tasks[index].isDone)
        _tasks[index] = updated
        queries?.toggleTaskDone(flagOf(updated.isDone), id.toLong())
    }

    fun toggleSubtask(taskId: Int, subtaskIndex: Int) {
        val index = _tasks.indexOfFirst { it.id == taskId }
        if (index < 0) return
        val task = _tasks[index]
        val subs = task.subtasks.toMutableList()
        if (subtaskIndex !in subs.indices) return
        subs[subtaskIndex] = subs[subtaskIndex].copy(isDone = !subs[subtaskIndex].isDone)
        _tasks[index] = task.copy(subtasks = subs)
        queries?.toggleSubtaskDone(flagOf(subs[subtaskIndex].isDone), taskId.toLong(), subtaskIndex.toLong())
    }

    /** Tulis satu task lengkap dengan subtask-nya ke database, atomik. */
    private fun persist(task: Task) {
        val db = TaskDbHolder.db ?: return
        db.transaction {
            db.taskQueries.insertTask(
                task.id.toLong(), task.title, task.category.label, task.priority.label,
                task.time, task.section, flagOf(task.isDone), task.description,
                flagOf(task.reminder), task.date.toString(),
            )
            db.taskQueries.deleteSubtasksOfTask(task.id.toLong())
            task.subtasks.forEachIndexed { i, sub ->
                db.taskQueries.insertSubtask(task.id.toLong(), i.toLong(), sub.title, flagOf(sub.isDone))
            }
        }
    }

    /** Muat ulang seluruh task dari database (hanya dipakai saat inisialisasi). */
    private fun reload() {
        val q = queries ?: return
        val subsByTask = q.selectSubtasks().executeAsList()
            .groupBy({ it.taskId }, { Subtask(it.title, flagValue(it.isDone)) })
        val loaded = q.selectTasks().executeAsList().map { row ->
            Task(
                id = row.id.toInt(),
                title = row.title,
                category = Categories.all.firstOrNull { it.label == row.categoryLabel }
                    ?: Category(row.categoryLabel, Color(0xFF667085), Color(0xFF667085).copy(alpha = 0.14f)),
                priority = Priorities.all.firstOrNull { it.label == row.priorityLabel } ?: Priorities.Sedang,
                time = row.time,
                section = row.section,
                isDone = flagValue(row.isDone),
                description = row.description,
                subtasks = subsByTask[row.id].orEmpty(),
                reminder = flagValue(row.reminder),
                date = runCatching { LocalDate.parse(row.date) }.getOrDefault(today()),
            )
        }
        _tasks.clear()
        _tasks.addAll(loaded)
    }
}
