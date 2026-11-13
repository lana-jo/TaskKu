package com.taskku.data

/** Urutan tampilan di layar daftar tugas (pencarian & filter). */
enum class TaskSort(val label: String) {
    Tanggal("Tanggal"),
    Prioritas("Prioritas"),
    Judul("Judul"),
}

private val priorityRank = Priorities.all.withIndex().associate { (index, p) -> p.label to index }

/**
 * Terapkan pencarian (case-insensitive pada judul), filter kategori, dan
 * pengurutan — logika murni, dipisah dari UI supaya bisa diuji.
 */
fun List<Task>.search(query: String, category: String?, sort: TaskSort): List<Task> {
    val base = filter { task ->
        (query.isBlank() || task.title.contains(query, ignoreCase = true)) &&
            (category == null || task.category.label == category)
    }
    return when (sort) {
        TaskSort.Tanggal -> base.sortedWith(compareBy({ it.date }, { it.time }))
        TaskSort.Prioritas -> base.sortedBy { priorityRank[it.priority.label] ?: Int.MAX_VALUE }
        TaskSort.Judul -> base.sortedWith(compareBy { it.title.lowercase() })
    }
}
