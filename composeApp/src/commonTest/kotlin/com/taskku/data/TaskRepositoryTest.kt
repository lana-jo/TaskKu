package com.taskku.data

import androidx.compose.ui.graphics.Color
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertNotNull
import kotlin.test.assertNull
import kotlin.test.assertTrue

/**
 * Test repository in-memory (platform tanpa driver — sama seperti jalur wasmJs).
 * Menguji logika CRUD, id berurutan, toggle, dan subtask.
 */
class TaskRepositoryTest {

    @Test
    fun tambahTask_mendapatIdBerurutan() {
        val before = TaskRepository.tasks.size
        TaskRepository.add(
            Task(
                id = 0,
                title = "Tugas uji",
                category = Categories.Pekerjaan,
                priority = Priorities.Sedang,
                time = "12:00",
                section = "Hari Ini",
            ),
        )
        val added = TaskRepository.tasks.last()
        assertEquals(before + 1, TaskRepository.tasks.size)
        assertTrue(added.id > 0, "id harus positif, dapat ${added.id}")
    }

    @Test
    fun toggleDone_membalikStatus() {
        val added = TaskRepository.add(
            Task(
                id = 0,
                title = "Toggle test",
                category = Categories.Pribadi,
                priority = Priorities.Rendah,
                time = "13:00",
                section = "Besok",
            ),
        )
        // add() mengembalikan Unit; ambil dari daftar
        val id = TaskRepository.tasks.last().id
        val awal = TaskRepository.byId(id)!!.isDone
        TaskRepository.toggleDone(id)
        assertEquals(!awal, TaskRepository.byId(id)!!.isDone)
        TaskRepository.toggleDone(id)
        assertEquals(awal, TaskRepository.byId(id)!!.isDone)
    }

    @Test
    fun hapusTask_menghilang() {
        TaskRepository.add(
            Task(
                id = 0,
                title = "Akan dihapus",
                category = Categories.Belanja,
                priority = Priorities.Tinggi,
                time = "14:00",
                section = "Hari Ini",
            ),
        )
        val id = TaskRepository.tasks.last().id
        TaskRepository.delete(id)
        assertNull(TaskRepository.byId(id))
    }

    @Test
    fun toggleSubtask_berfungsi() {
        TaskRepository.add(
            Task(
                id = 0,
                title = "Dengan subtask",
                category = Categories.Pekerjaan,
                priority = Priorities.Sedang,
                time = "15:00",
                section = "Hari Ini",
                subtasks = listOf(Subtask("Langkah A"), Subtask("Langkah B")),
            ),
        )
        val id = TaskRepository.tasks.last().id
        TaskRepository.toggleSubtask(id, 0)
        assertTrue(TaskRepository.byId(id)!!.subtasks[0].isDone)
        assertTrue(!TaskRepository.byId(id)!!.subtasks[1].isDone)
    }

    @Test
    fun kategoriAdd_dedupNama() {
        val jumlahSebelum = Categories.all.size
        val existing = Categories.add("pekerjaan", Color.Red) // beda kapital
        assertEquals(jumlahSebelum, Categories.all.size, "kategori duplikat tidak boleh menambah")
        assertEquals("Pekerjaan", existing.label)
    }

    @Test
    fun byId_tidakAda_null() {
        assertNull(TaskRepository.byId(Int.MAX_VALUE))
    }

    @Test
    fun update_mengubahJudul() {
        TaskRepository.add(
            Task(
                id = 0,
                title = "Judul lama",
                category = Categories.Pribadi,
                priority = Priorities.Rendah,
                time = "16:00",
                section = "Besok",
            ),
        )
        val task = TaskRepository.tasks.last()
        TaskRepository.update(task.copy(title = "Judul baru"))
        assertEquals("Judul baru", assertNotNull(TaskRepository.byId(task.id)).title)
    }
}
