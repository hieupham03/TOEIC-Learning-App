package vn.toeiclearning.alpha

import android.graphics.Color
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.SystemBarStyle
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import vn.toeiclearning.alpha.study.StudyApp
import vn.toeiclearning.alpha.ui.AlphaApp
import vn.toeiclearning.alpha.ui.AlphaTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge(
            statusBarStyle = SystemBarStyle.light(Color.TRANSPARENT, Color.TRANSPARENT),
            navigationBarStyle = SystemBarStyle.light(Color.WHITE, Color.BLACK),
        )
        setContent { AlphaTheme { if (BuildConfig.LOCAL_STUDY) StudyApp() else AlphaApp() } }
    }
}
