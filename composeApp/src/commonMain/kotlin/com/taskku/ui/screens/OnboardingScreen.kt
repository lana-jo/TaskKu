package com.taskku.ui.screens

import androidx.compose.foundation.background
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
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Check
import androidx.compose.material.icons.rounded.EmojiEvents
import androidx.compose.material.icons.rounded.TaskAlt
import androidx.compose.material.icons.rounded.WbSunny
import androidx.compose.material3.Icon
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
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.UserSession
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.FieldBox
import com.taskku.ui.PrimaryButton

/**
 * Onboarding lokal: pengguna memasukkan nama, disimpan ke tabel settings.
 * Tidak ada server — "Keluar" menghapus nama dan kembali ke sini.
 */
@Composable
fun OnboardingScreen(onDone: (String) -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    var name by remember { mutableStateOf("") }
    var error by remember { mutableStateOf<String?>(null) }

    fun submit() {
        val trimmed = name.trim()
        if (trimmed.isEmpty()) {
            error = "Nama tidak boleh kosong"
            return
        }
        UserSession.signIn(trimmed)
        onDone(trimmed)
    }

    Box(Modifier.fillMaxSize().background(colors.gradient)) {
        Column(
            verticalArrangement = Arrangement.Center,
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 32.dp),
        ) {
            Box(
                contentAlignment = Alignment.Center,
                modifier = Modifier
                    .size(72.dp)
                    .clip(RoundedCornerShape(22.dp))
                    .background(Color.White.copy(alpha = 0.18f)),
            ) {
                Icon(Icons.Rounded.Check, contentDescription = null, tint = Color.White, modifier = Modifier.size(38.dp))
            }
            Spacer(Modifier.height(22.dp))
            Text("TaskKu", style = txt.display.copy(fontSize = 32.sp), color = Color.White)
            Spacer(Modifier.height(8.dp))
            Text(
                "Satu tempat untuk semua tugas\nhari-mu. Mulailah dengan namamu.",
                style = txt.body,
                color = Color.White.copy(alpha = 0.8f),
            )
            Spacer(Modifier.height(28.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(12.dp), modifier = Modifier.fillMaxWidth()) {
                Feature(Icons.Rounded.WbSunny, "Rencanakan\nhari ini", Modifier.weight(1f))
                Feature(Icons.Rounded.TaskAlt, "Selesaikan\ntugas", Modifier.weight(1f))
                Feature(Icons.Rounded.EmojiEvents, "Raih\nstreak", Modifier.weight(1f))
            }
            Spacer(Modifier.height(34.dp))
            FieldBox(
                value = name,
                onValueChange = {
                    name = it
                    error = null
                },
                placeholder = "Siapa namamu?",
            )
            error?.let {
                Text(
                    it,
                    style = txt.small.copy(fontSize = 12.sp),
                    color = Color(0xFFFFD66B),
                    modifier = Modifier.padding(start = 4.dp, top = 8.dp),
                )
            }
            Spacer(Modifier.height(18.dp))
            PrimaryButton(
                label = "Mulai",
                modifier = Modifier.fillMaxWidth(),
            ) { submit() }
        }
    }
}

@Composable
private fun Feature(icon: androidx.compose.ui.graphics.vector.ImageVector, label: String, modifier: Modifier = Modifier) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(8.dp),
        modifier = modifier
            .clip(RoundedCornerShape(16.dp))
            .background(Color.White.copy(alpha = 0.14f))
            .padding(vertical = 18.dp),
    ) {
        Icon(icon, contentDescription = null, tint = Color.White, modifier = Modifier.size(22.dp))
        Text(
            label,
            style = LocalTaskKuText.current.small.copy(fontSize = 11.5.sp),
            color = Color.White.copy(alpha = 0.85f),
            textAlign = androidx.compose.ui.text.style.TextAlign.Center,
        )
    }
}
