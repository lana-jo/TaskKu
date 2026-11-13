group = "com.taskku"

plugins {
    alias(libs.plugins.androidApplication)
    alias(libs.plugins.composeMultiplatform)
    alias(libs.plugins.composeCompiler)
}

android {
    namespace = "com.taskku.app"
    compileSdk = libs.versions.androidCompileSdk.get().toInt()

    defaultConfig {
        applicationId = "com.taskku.app"
        minSdk = libs.versions.androidMinSdk.get().toInt()
        targetSdk = libs.versions.androidTargetSdk.get().toInt()
        versionCode = 1
        versionName = "1.0.0"
    }

    // Signing pakai debug keystore milik user (~/.android/debug.keystore) agar APK
    // bisa diinstall untuk pengujian pribadi. Ganti dengan release keystore sendiri
    // sebelum distribusi publik. Kredensial tidak di-commit: hanya baca file lokal.
    signingConfigs {
        create("testing") {
            storeFile = file("${System.getProperty("user.home")}/.android/debug.keystore")
            storePassword = "android"
            keyAlias = "androiddebugkey"
            keyPassword = "android"
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    buildTypes {
        getByName("release") {
            signingConfig = signingConfigs.getByName("testing")
        }
    }
}

dependencies {
    implementation(project(":composeApp"))
    implementation(libs.androidx.activityCompose)
}
