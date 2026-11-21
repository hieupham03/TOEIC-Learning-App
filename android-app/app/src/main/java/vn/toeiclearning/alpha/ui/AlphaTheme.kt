package vn.toeiclearning.alpha.ui

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Typography
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

object AlphaTokens {
    val Primary = Color(0xFF0B736A)
    val Ink = Color(0xFF0F172A)
    val Secondary = Color(0xFF475569)
    val Background = Color(0xFFF8FAF9)
    val Surface = Color(0xFFFFFFFF)
    val Muted = Color(0xFFEDF4F1)
    val Outline = Color(0xFFC4D0CB)
    val Warning = Color(0xFF8C4C10)
    val WarningBackground = Color(0xFFFFF4E5)
    val Error = Color(0xFFB42318)
}

private val colors = lightColorScheme(
    primary = AlphaTokens.Primary,
    onPrimary = AlphaTokens.Surface,
    background = AlphaTokens.Background,
    onBackground = AlphaTokens.Ink,
    surface = AlphaTokens.Surface,
    onSurface = AlphaTokens.Ink,
    surfaceVariant = AlphaTokens.Muted,
    onSurfaceVariant = AlphaTokens.Secondary,
    outline = AlphaTokens.Outline,
    error = AlphaTokens.Error,
)

private val typography = Typography(
    headlineMedium = TextStyle(
        fontFamily = FontFamily.SansSerif, fontSize = 26.sp,
        lineHeight = 33.sp, fontWeight = FontWeight.Bold,
    ),
    titleLarge = TextStyle(
        fontFamily = FontFamily.SansSerif, fontSize = 22.sp,
        lineHeight = 30.sp, fontWeight = FontWeight.SemiBold,
    ),
    titleMedium = TextStyle(
        fontFamily = FontFamily.SansSerif, fontSize = 18.sp,
        lineHeight = 25.sp, fontWeight = FontWeight.SemiBold,
    ),
    bodyLarge = TextStyle(
        fontFamily = FontFamily.SansSerif, fontSize = 16.sp,
        lineHeight = 24.sp,
    ),
    bodyMedium = TextStyle(
        fontFamily = FontFamily.SansSerif, fontSize = 14.sp,
        lineHeight = 21.sp,
    ),
    labelLarge = TextStyle(
        fontFamily = FontFamily.SansSerif, fontSize = 16.sp,
        lineHeight = 22.sp, fontWeight = FontWeight.Medium,
    ),
)

@Composable
fun AlphaTheme(content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = colors, typography = typography, content = content)
}
