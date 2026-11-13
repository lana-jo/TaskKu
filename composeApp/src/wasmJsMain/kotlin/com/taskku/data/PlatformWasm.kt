package com.taskku.data

actual fun todayLabel(): String = js(
    "new Date().toLocaleDateString('id-ID', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })"
)
