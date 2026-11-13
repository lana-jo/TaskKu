package com.taskku.ui.screens

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
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
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.rounded.Notifications
import androidx.compose.material.icons.rounded.ChevronRight
import androidx.compose.material.icons.rounded.DarkMode
import androidx.compose.material.icons.rounded.Logout
import androidx.compose.material.icons.rounded.MoreVert
import androidx.compose.material.icons.rounded.Tune
import androidx.compose.material.icons.rounded.Star
import androidx.compose.material3.Icon
import androidx.compose.material3.Surface
import androidx.compose.material3.Switch
import androidx.compose.material3.SwitchDefaults
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
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.data.UserSession
import com.taskku.theme.LocalTaskKuColors
import com.taskku.theme.TaskKuShapes
import com.taskku.theme.LocalTaskKuText
import com.taskku.ui.DockBar
import com.taskku.ui.OutlineButton
import com.taskku.ui.PrimaryButton

@Composable
fun ProfileScreen(
    tab: String,
    onTabChange: (String) -> Unit,
    darkOverride: Boolean?,
    onDarkOverrideChange: (Boolean?) -> Unit,
    onLogout: () -> Unit = {},
) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    var notifOn by remember { mutableStateOf(true) }
    var confirmLogout by remember { mutableStateOf(false) }
    val userName = com.taskku.data.UserSession.userName ?: "Pengguna"
    val initials = userName.split(" ").mapNotNull { it.firstOrNull() }.take(2).joinToString("")

    Box(Modifier.fillMaxSize().background(colors.bg)) {
        Column(
            verticalArrangement = Arrangement.spacedBy(14.dp),
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(start = 24.dp, top = 8.dp, end = 24.dp, bottom = 112.dp),
        ) {
            Text("Profil", style = txt.section.copy(fontSize = 19.sp), color = colors.text)
            Surface(shape = TaskKuShapes.hero, color = Color.Transparent, modifier = Modifier.fillMaxWidth()) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(14.dp),
                    modifier = Modifier
                        .background(colors.gradient)
                        .padding(20.dp),
                ) {
                    Box(
                        contentAlignment = Alignment.Center,
                        modifier = Modifier
                            .size(60.dp)
                            .clip(CircleShape)
                            .background(Color.White.copy(alpha = 0.18f)),
                    ) {
                        Text(initials, style = txt.section.copy(fontSize = 20.sp), color = Color.White)
                    }
                    Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
                        Text(userName, style = txt.section.copy(fontSize = 17.sp), color = Color.White)
                        Text("rian.pratama@mail.com", style = txt.small.copy(fontSize = 12.sp), color = Color.White.copy(alpha = 0.7f))
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(5.dp),
                            modifier = Modifier
                                .clip(RoundedCornerShape(999.dp))
                                .background(Color.White.copy(alpha = 0.18f))
                                .padding(horizontal = 11.dp, vertical = 5.dp),
                        ) {
                            Icon(Icons.Rounded.Star, contentDescription = null, tint = Color(0xFFFFD66B), modifier = Modifier.size(12.dp))
                            Text("PAKET PRO", style = txt.micro.copy(fontSize = 9.5.sp), color = Color.White)
                        }
                    }
                }
            }
            Row(horizontalArrangement = Arrangement.spacedBy(10.dp), modifier = Modifier.fillMaxWidth()) {
                StatTile("128", "SELESAI", Modifier.weight(1f))
                StatTile("12", "HARI STREAK", Modifier.weight(1f))
                StatTile("87", "SKOR FOKUS", Modifier.weight(1f))
            }
            Text("Pengaturan", style = txt.section, color = colors.text)
            Surface(shape = TaskKuShapes.card, color = colors.surface, shadowElevation = 4.dp) {
                Column {
                    SettingRow("Notifikasi", Icons.Rounded.Notifications) {
                        Switch(
                            checked = notifOn,
                            onCheckedChange = { notifOn = it },
                            colors = SwitchDefaults.colors(
                                checkedTrackColor = colors.primary,
                                checkedThumbColor = Color.White,
                                uncheckedTrackColor = colors.border,
                                uncheckedThumbColor = Color.White,
                            ),
                        )
                    }
                    SettingDivider()
                    SettingRow("Tema Gelap", Icons.Rounded.DarkMode) {
                        Switch(
                            checked = darkOverride == true,
                            onCheckedChange = { onDarkOverrideChange(if (it) true else null) },
                            colors = SwitchDefaults.colors(
                                checkedTrackColor = colors.primary,
                                checkedThumbColor = Color.White,
                                uncheckedTrackColor = colors.border,
                                uncheckedThumbColor = Color.White,
                            ),
                        )
                    }
                    SettingDivider()
                    SettingRow("Sinkronisasi", Icons.Rounded.Tune) {
                        Icon(Icons.Rounded.ChevronRight, contentDescription = null, tint = colors.textMuted, modifier = Modifier.size(16.dp))
                    }
                    SettingDivider()
                    SettingRow("Bantuan & Masukan", Icons.Rounded.MoreVert) {
                        Icon(Icons.Rounded.ChevronRight, contentDescription = null, tint = colors.textMuted, modifier = Modifier.size(16.dp))
                    }
                }
            }
            OutlineButton(
                label = "Keluar",
                icon = Icons.Rounded.Logout,
                onClick = { confirmLogout = true },
                modifier = Modifier.fillMaxWidth(),
                strokeColor = colors.danger,
                textColor = colors.danger,
            )
        }
        if (confirmLogout) {
            // Scrim + dialog konfirmasi keluar
            Box(
                Modifier
                    .fillMaxSize()
                    .background(Color.Black.copy(alpha = 0.4f))
                    .clickable { confirmLogout = false },
            )
            Surface(
                shape = RoundedCornerShape(20.dp),
                color = colors.surface,
                shadowElevation = 16.dp,
                modifier = Modifier
                    .align(Alignment.Center)
                    .padding(horizontal = 40.dp)
                    .fillMaxWidth(),
            ) {
                Column(
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.spacedBy(10.dp),
                    modifier = Modifier.padding(24.dp),
                ) {
                    Text("Keluar dari TaskKu?", style = txt.section, color = colors.text)
                    Text(
                        "Tugasmu tetap tersimpan di perangkat ini.",
                        style = txt.small,
                        color = colors.textMuted,
                    )
                    Spacer(Modifier.height(6.dp))
                    Row(horizontalArrangement = Arrangement.spacedBy(10.dp), modifier = Modifier.fillMaxWidth()) {
                        OutlineButton(
                            label = "Batal",
                            onClick = { confirmLogout = false },
                            modifier = Modifier.weight(1f),
                            height = 46.dp,
                        )
                        com.taskku.ui.PrimaryButton(
                            label = "Keluar",
                            onClick = {
                                confirmLogout = false
                                onLogout()
                            },
                            modifier = Modifier.weight(1f),
                            height = 46.dp,
                        )
                    }
                }
            }
        }
        DockBar(
            active = tab,
            onSelect = onTabChange,
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .padding(start = 16.dp, end = 16.dp, bottom = 14.dp),
        )
    }
}

@Composable
private fun StatTile(value: String, label: String, modifier: Modifier = Modifier) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Surface(shape = TaskKuShapes.card, color = colors.surface, shadowElevation = 4.dp, modifier = modifier) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(5.dp),
            modifier = Modifier.padding(vertical = 14.dp).fillMaxWidth(),
        ) {
            Text(value, style = txt.value.copy(fontSize = 19.sp), color = colors.primary)
            Text(label, style = txt.micro.copy(fontSize = 9.sp), color = colors.textMuted)
        }
    }
}

@Composable
private fun SettingRow(label: String, icon: ImageVector, trailing: @Composable () -> Unit) {
    val colors = LocalTaskKuColors.current
    val txt = LocalTaskKuText.current
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier
            .fillMaxWidth()
            .height(54.dp)
            .clickable { }
            .padding(horizontal = 16.dp),
    ) {
        Box(
            contentAlignment = Alignment.Center,
            modifier = Modifier
                .size(32.dp)
                .clip(RoundedCornerShape(11.dp))
                .background(colors.surface2),
        ) {
            Icon(icon, contentDescription = null, tint = colors.textMuted, modifier = Modifier.size(16.dp))
        }
        Spacer(Modifier.width(12.dp))
        Text(label, style = txt.body, color = colors.text, modifier = Modifier.weight(1f))
        trailing()
    }
}

@Composable
private fun SettingDivider() {
    val colors = LocalTaskKuColors.current
    Box(
        Modifier
            .fillMaxWidth()
            .height(1.dp)
            .background(colors.border),
    )
}
