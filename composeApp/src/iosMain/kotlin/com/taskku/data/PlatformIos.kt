package com.taskku.data

import platform.Foundation.NSDate
import platform.Foundation.NSDateFormatter
import platform.Foundation.NSLocale
import platform.Foundation.currentLocale

actual fun todayLabel(): String {
    val formatter = NSDateFormatter().apply {
        dateFormat = "EEEE, dd MMMM yyyy"
        locale = NSLocale.currentLocale
    }
    return formatter.stringFromDate(NSDate())
}
