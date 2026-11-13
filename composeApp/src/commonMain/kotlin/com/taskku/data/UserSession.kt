package com.taskku.data

/**
 * Sesi pengguna lokal: nama disimpan di tabel settings, tanpa backend.
 * null = belum onboarding → aplikasi membuka layar selamat datang.
 */
object UserSession {
    private val queries get() = TaskDbHolder.db?.taskQueries

    /** null = belum ada pengguna (belum onboarding). */
    var userName: String? = loadUserName()
        private set

    private fun loadUserName(): String? =
        queries?.selectSetting("userName")?.executeAsOneOrNull()?.takeIf { it.isNotBlank() }

    /** Simpan nama setelah onboarding (atau ubah dari Profil). */
    fun signIn(name: String) {
        val cleaned = name.trim()
        require(cleaned.isNotEmpty()) { "Nama tidak boleh kosong" }
        userName = cleaned
        queries?.putSetting("userName", cleaned)
    }

    /** Keluar: hapus nama → aplikasi kembali ke onboarding. Tugas tetap tersimpan. */
    fun signOut() {
        userName = null
        queries?.putSetting("userName", "")
    }
}
