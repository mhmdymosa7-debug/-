[app]

# (str) Title of your application
title = الحاسبة الذكية

# (str) Package name
package.name = smartcalculator
package.domain = org.arabic

# (str) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# ركز هنا على متطلبات بايثون الأساسية لتشغيل الواجهة والحسابات
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (str) Supported architectures (أحدث المعماريات المطلوبة من جوجل بلاي)
android.archs = arm64-v8a, armeabi-v7a

# (str) Target version of Android
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# صيغة المخرجات النهائية لتكون جاهزة للمتجر (AAB)
android.release_artifact = aab

# الإصدارات البرمجية
version.code = 1
version.string = 1.0.0

[buildozer]
log_level = 2
warn_on_root = 1
