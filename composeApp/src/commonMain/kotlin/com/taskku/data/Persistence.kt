package com.taskku.data

import app.cash.sqldelight.db.SqlDriver
import com.taskku.db.TaskDb

/**
 * Membuat driver SQLite per-platform:
 * - desktop : JdbcSqliteDriver → ~/.taskku/taskku.db
 * - android : AndroidSqliteDriver → database internal aplikasi
 * - iOS     : NativeSqliteDriver → dokumen aplikasi
 * - wasmJs  : null (belum ada driver web) → repository jatuh ke mode in-memory
 */
expect fun createTaskDbDriver(): SqlDriver?

/** Satu instance TaskDb untuk seluruh aplikasi; null berarti platform tanpa storage. */
internal object TaskDbHolder {
    val db: TaskDb? by lazy {
        try {
            createTaskDbDriver()?.let { TaskDb(it) }
        } catch (e: Exception) {
            // DB korup / disk penuh / init gagal → degradasi in-memory, jangan crash.
            e.printStackTrace()
            null
        }
    }
}

/** Pengaturan aplikasi yang tersimpan permanen (tabel settings). */
object AppSettings {
    private val queries get() = TaskDbHolder.db?.taskQueries

    /** null = ikut tema sistem; true/false = override manual dari layar Profil. */
    var darkOverride: Boolean? = loadDarkOverride()
        private set

    private fun loadDarkOverride(): Boolean? =
        when (queries?.selectSetting("darkTheme")?.executeAsOneOrNull()) {
            "true" -> true
            "false" -> false
            else -> null
        }

    fun setDarkOverride(value: Boolean?) {
        darkOverride = value
        queries?.putSetting("darkTheme", value?.toString() ?: "auto")
    }
}
