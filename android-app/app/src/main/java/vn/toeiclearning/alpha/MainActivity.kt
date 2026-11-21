package vn.toeiclearning.alpha

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import vn.toeiclearning.alpha.ui.AlphaApp
import vn.toeiclearning.alpha.ui.AlphaTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { AlphaTheme { AlphaApp() } }
    }
}
