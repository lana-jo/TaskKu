package com.taskku.data

import androidx.compose.ui.graphics.Color
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertNotNull
import kotlin.test.assertNull
import kotlin.test.assertTrue
import kotlinx.datetime.LocalDate

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

class TaskSearchTest {

    private fun task(
        title: String,
        category: Category = Categories.Pekerjaan,
        priority: Priority = Priorities.Sedang,
        time: String = "08:00",
        date: LocalDate = LocalDate(2026, 11, 13),
    ) = Task(
        id = 0, title = title, category = category, priority = priority,
        time = time, section = "Hari Ini", date = date,
    )

    @Test
    fun pencarian_caseInsensitive() {
        val hasil = listOf(task("Rapat sprint"), task("Belanja")).search("rapat", null, TaskSort.Tanggal)
        assertEquals(1, hasil.size)
        assertEquals("Rapat sprint", hasil[0].title)
    }

    @Test
    fun filterKategori_hanyaKategoriTersebut() {
        val hasil = listOf(task("A", category = Categories.Pribadi), task("B")).search("", "Pribadi", TaskSort.Tanggal)
        assertEquals(listOf("A"), hasil.map { it.title })
    }

    @Test
    fun urutTanggal_laluWaktu() {
        val hasil = listOf(
            task("B", time = "09:00", date = LocalDate(2026, 11, 13)),
            task("A", time = "07:00", date = LocalDate(2026, 11, 14)),
            task("C", time = "06:00", date = LocalDate(2026, 11, 13)),
        ).search("", null, TaskSort.Tanggal)
        assertEquals(listOf("C", "B", "A"), hasil.map { it.title })
    }

    @Test
    fun urutPrioritas_tinggiDulu() {
        val hasil = listOf(
            task("Rendah", priority = Priorities.Rendah),
            task("Tinggi", priority = Priorities.Tinggi),
            task("Sedang", priority = Priorities.Sedang),
        ).search("", null, TaskSort.Prioritas)
        assertEquals(listOf("Tinggi", "Sedang", "Rendah"), hasil.map { it.title })
    }

    @Test
    fun urutJudul_abjad() {
        val hasil = listOf(task("cincau"), task("bakso"), task("Apel")).search("", null, TaskSort.Judul)
        assertEquals(listOf("Apel", "bakso", "cincau"), hasil.map { it.title })
    }
}
