package com.taskku.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.taskku.App
import com.taskku.data.AndroidDatabase

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Driver SQLite (TaskKu) butuh context — wajib sebelum App() dirender.
        AndroidDatabase.appContext = applicationContext
        setContent {
            App()
        }
    }
}
