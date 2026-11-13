package com.taskku.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.Immutable
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.taskku.composeapp.generated.resources.Res
import com.taskku.composeapp.generated.resources.plus_jakarta_sans_400
import com.taskku.composeapp.generated.resources.plus_jakarta_sans_500
import com.taskku.composeapp.generated.resources.plus_jakarta_sans_600
import com.taskku.composeapp.generated.resources.plus_jakarta_sans_700
import org.jetbrains.compose.resources.Font

// Palet dari design system TaskKu (koleksi variabel "Warna", mode Terang/Gelap)
@Immutable
data class TaskKuColors(
    val bg: Color,
    val surface: Color,
    val surface2: Color,
    val text: Color,
    val textMuted: Color,
    val border: Color,
    val primary: Color,
    val primarySoft: Color,
    val primaryFg: Color,
    val success: Color,
    val warning: Color,
    val danger: Color,
) {
    val gradient: Brush = Brush.linearGradient(listOf(Color(0xFF6C5CE7), Color(0xFF9F7AEA)))
}

val LightColors = TaskKuColors(
    bg = Color(0xFFF4F4F9),
    surface = Color(0xFFFFFFFF),
    surface2 = Color(0xFFF0F0F6),
    text = Color(0xFF131319),
    textMuted = Color(0xFF74748A),
    border = Color(0xFFE7E7EF),
    primary = Color(0xFF5B54F0),
    primarySoft = Color(0xFFECEBFE),
    primaryFg = Color(0xFFFFFFFF),
    success = Color(0xFF12B76A),
    warning = Color(0xFFF79009),
    danger = Color(0xFFE5484D),
)

val DarkColors = TaskKuColors(
    bg = Color(0xFF0F0F15),
    surface = Color(0xFF1C1C24),
    surface2 = Color(0xFF27272F),
    text = Color(0xFFF5F5FA),
    textMuted = Color(0xFF9C9CB1),
    border = Color(0xFF2B2B36),
    primary = Color(0xFF9089FF),
    primarySoft = Color(0xFF2C2A55),
    primaryFg = Color(0xFFFFFFFF),
    success = Color(0xFF34D399),
    warning = Color(0xFFFBBF24),
    danger = Color(0xFFF87171),
)

val LocalTaskKuColors = staticCompositionLocalOf { LightColors }

object TaskKuShapes {
    val card = RoundedCornerShape(20.dp)
    val hero = RoundedCornerShape(26.dp)
    val sheet = RoundedCornerShape(topStart = 30.dp, topEnd = 30.dp)
    val button = RoundedCornerShape(999.dp)
    val field = RoundedCornerShape(16.dp)
}

@Immutable
data class TaskKuTextSet(
    val display: TextStyle,
    val judul: TextStyle,
    val section: TextStyle,
    val body: TextStyle,
    val bodyMedium: TextStyle,
    val small: TextStyle,
    val micro: TextStyle,
    val value: TextStyle,
)

private fun defaultTextSet(): TaskKuTextSet {
    val family = FontFamily.Default
    return TaskKuTextSet(
        display = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 28.sp, lineHeight = 36.sp, letterSpacing = (-0.56).sp),
        judul = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 22.sp, lineHeight = 29.sp, letterSpacing = (-0.33).sp),
        section = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 16.5.sp, lineHeight = 23.sp, letterSpacing = (-0.17).sp),
        body = TextStyle(fontFamily = family, fontWeight = FontWeight.Normal, fontSize = 14.5.sp, lineHeight = 22.sp),
        bodyMedium = TextStyle(fontFamily = family, fontWeight = FontWeight.Medium, fontSize = 15.sp, lineHeight = 20.sp),
        small = TextStyle(fontFamily = family, fontWeight = FontWeight.Normal, fontSize = 13.sp, lineHeight = 19.sp),
        micro = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 10.sp, lineHeight = 12.sp, letterSpacing = 0.8.sp),
        value = TextStyle(fontFamily = family, fontWeight = FontWeight.Bold, fontSize = 19.sp, letterSpacing = (-0.19).sp),
    )
}

val LocalTaskKuText = staticCompositionLocalOf { defaultTextSet() }

@Composable
private fun jakartaTextSet(): TaskKuTextSet {
    val family = FontFamily(
        Font(Res.font.plus_jakarta_sans_400, FontWeight.Normal),
        Font(Res.font.plus_jakarta_sans_500, FontWeight.Medium),
        Font(Res.font.plus_jakarta_sans_600, FontWeight.SemiBold),
        Font(Res.font.plus_jakarta_sans_700, FontWeight.Bold),
    )
    return TaskKuTextSet(
        display = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 28.sp, lineHeight = 36.sp, letterSpacing = (-0.56).sp),
        judul = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 22.sp, lineHeight = 29.sp, letterSpacing = (-0.33).sp),
        section = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 16.5.sp, lineHeight = 23.sp, letterSpacing = (-0.17).sp),
        body = TextStyle(fontFamily = family, fontWeight = FontWeight.Normal, fontSize = 14.5.sp, lineHeight = 22.sp),
        bodyMedium = TextStyle(fontFamily = family, fontWeight = FontWeight.Medium, fontSize = 15.sp, lineHeight = 20.sp),
        small = TextStyle(fontFamily = family, fontWeight = FontWeight.Normal, fontSize = 13.sp, lineHeight = 19.sp),
        micro = TextStyle(fontFamily = family, fontWeight = FontWeight.SemiBold, fontSize = 10.sp, lineHeight = 12.sp, letterSpacing = 0.8.sp),
        value = TextStyle(fontFamily = family, fontWeight = FontWeight.Bold, fontSize = 19.sp, letterSpacing = (-0.19).sp),
    )
}

@Composable
fun TaskKuTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit,
) {
    val colors = if (darkTheme) DarkColors else LightColors
    CompositionLocalProvider(
        LocalTaskKuColors provides colors,
        LocalTaskKuText provides jakartaTextSet(),
    ) {
        MaterialTheme(
            colorScheme = if (darkTheme) darkColorScheme() else lightColorScheme(),
            content = content,
        )
    }
}
