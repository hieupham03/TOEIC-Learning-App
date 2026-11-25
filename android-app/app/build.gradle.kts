plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
}

android {
    namespace = "vn.toeiclearning.alpha"
    compileSdk = 36

    defaultConfig {
        applicationId = "vn.toeiclearning.alpha"
        minSdk = 26
        targetSdk = 36
        versionCode = 3
        versionName = "0.2.1-preview"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        buildConfigField("boolean", "LOCAL_LISTENING_PREVIEW", "false")
        buildConfigField("boolean", "LOCAL_STUDY", "false")
    }

    buildTypes {
        release { isMinifyEnabled = false }
        create("localPreview") {
            initWith(getByName("debug"))
            matchingFallbacks += "debug"
            applicationIdSuffix = ".listeningpreview"
            versionNameSuffix = "-lab"
            buildConfigField("boolean", "LOCAL_LISTENING_PREVIEW", "true")
        }
        create("study") {
            initWith(getByName("debug"))
            matchingFallbacks += "debug"
            applicationIdSuffix = ".study"
            versionNameSuffix = "-study"
            buildConfigField("boolean", "LOCAL_STUDY", "true")
        }
    }
    sourceSets.getByName("localPreview").assets.srcDir("../.tooling/fasttrack-handoff/part3-assets")
    val acceptedContent = "../.tooling/two-user-study/content-07/release-assets"
    val listeningContent = "../.tooling/two-user-study/content-08/release-assets"
    val content06 = "../.tooling/two-user-study/content-06/assets"
    val studyAssets = providers.gradleProperty("studyAssetsDir").orElse(
        when {
            file("$listeningContent/study_pack/pack.json").isFile -> listeningContent
            file("$acceptedContent/study_pack/pack.json").isFile -> acceptedContent
            file("$content06/study_pack/pack.json").isFile -> content06
            else -> "../.tooling/two-user-study/content-04/assets"
        }
    )
    sourceSets.getByName("study").assets.srcDir(studyAssets.get())
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
    buildFeatures {
        compose = true
        buildConfig = true
    }
    androidResources { noCompress += listOf("wav", "mp3") }
}

androidComponents {
    onVariants(selector().withBuildType("study")) { variant ->
        variant.outputs.forEach {
            it.versionCode.set(13)
            it.versionName.set("0.3.9-study")
        }
    }
}

dependencies {
    // 2025.06.00 keeps Compose compatible with the approved API 36 / AGP 8.13 Alpha toolchain.
    implementation(platform("androidx.compose:compose-bom:2025.06.00"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.foundation:foundation")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.activity:activity-compose:1.11.0")
    implementation("androidx.core:core-ktx:1.17.0")
    debugImplementation("androidx.compose.ui:ui-tooling")
    testImplementation("junit:junit:4.13.2")
}
