import org.jetbrains.compose.desktop.application.dsl.TargetFormat
import org.jetbrains.kotlin.gradle.dsl.JvmTarget

group = "com.taskku"

plugins {
    alias(libs.plugins.kotlinMultiplatform)
    alias(libs.plugins.composeMultiplatform)
    alias(libs.plugins.composeCompiler)
    alias(libs.plugins.androidKotlinMultiplatformLibrary)
    alias(libs.plugins.sqldelight)
}

sqldelight {
    databases {
        create("TaskDb") {
            packageName.set("com.taskku.db")
            // AS Boolean butuh dialect SQLite 3.25+ (3.18 bawaan rusak)
            dialect("app.cash.sqldelight:sqlite-3-25-dialect:2.4.1")
        }
    }
}

kotlin {
    jvm("desktop")

    // Plugin AGP-KMP mematikan default hierarchy; iOS shared source set
    // (iosMain) butuh template ini agar dibuat.
    applyDefaultHierarchyTemplate()

    wasmJs {
        browser()
        binaries.executable()
    }

    listOf(
        iosArm64(),
        iosSimulatorArm64(),
    ).forEach { iosTarget ->
        iosTarget.binaries.framework {
            baseName = "TaskKu"
            isStatic = true
        }
    }

    // Plugin Android-KMP (AGP 9): konfigurasi target Android di dalam kotlin {},
    // tanpa top-level android extension. Aplikasi Android (MainActivity + manifest)
    // ada di module :androidApp.
    android {
        namespace = "com.taskku.shared"
        compileSdk = libs.versions.androidCompileSdk.get().toInt()
        minSdk = libs.versions.androidMinSdk.get().toInt()

        compilerOptions {
            jvmTarget.set(JvmTarget.JVM_17)
        }
    }

    sourceSets {
        val commonMain by getting {
            // Plugin SQLDelight 2.4.1 tidak otomatis mendaftarkan output ke commonMain
            // saat dipadukan dengan AGP-KMP; daftarkan eksplisit.
            kotlin.srcDir("build/generated/sqldelight/code/TaskDb/commonMain")
            dependencies {
                implementation(compose.runtime)
                implementation(compose.foundation)
                implementation(compose.material3)
                implementation(compose.materialIconsExtended)
                implementation(compose.components.resources)
                implementation(libs.kotlinx.datetime)
                implementation(libs.sqldelight.runtime)
            }
        }
        val commonTest by getting {
            dependencies {
                implementation(kotlin("test"))
            }
        }
        val androidMain by getting {
            dependencies {
                implementation(libs.sqldelight.androidDriver)
            }
        }
        val desktopMain by getting {
            dependencies {
                implementation(compose.desktop.currentOs)
                implementation(libs.sqldelight.sqliteDriver)
            }
        }
        val iosMain by getting {
            dependencies {
                implementation(libs.sqldelight.nativeDriver)
            }
        }
        val wasmJsMain by getting {
            dependencies {
                implementation(compose.ui)
            }
        }
    }
}

compose.desktop.application {
    mainClass = "com.taskku.MainKt"

    nativeDistributions {
        targetFormats(TargetFormat.Deb, TargetFormat.Rpm)
        packageName = "TaskKu"
        packageVersion = "1.0.0"
    }
}
