package app.repchat.dentium

import android.Manifest
import android.app.*
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.content.ServiceConnection
import android.content.pm.PackageManager
import android.icu.text.SimpleDateFormat
import android.os.Build
import android.os.IBinder
import android.provider.Settings
import android.util.Log
import android.widget.Toast
import androidx.annotation.NonNull
import androidx.annotation.RequiresApi
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.google.firebase.Timestamp
import com.noransoft.rep_chat.AlarmReceiver
import com.noransoft.rep_chat.LocationService
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import java.util.*
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.Query
import kotlinx.coroutines.*


class MainActivity : FlutterActivity() {
    private val CHANNEL = "samples.flutter.dev/battery"
    private var permission: Boolean = false

    private lateinit var alarmManager: AlarmManager

    var mService: LocationService? = null
    var mBound = false


    @RequiresApi(Build.VERSION_CODES.O)
    override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
//
        checkIsServiceOn()
        alarmManager = getSystemService(Context.ALARM_SERVICE) as AlarmManager
        createNotificationChannel()

        MethodChannel(
            flutterEngine.dartExecutor.binaryMessenger,
            CHANNEL
        ).setMethodCallHandler { call, result ->
            if (call.method == "getBatteryLevel") {
                fn_permission()
                val prefs =
                    context?.getSharedPreferences("FlutterSharedPreferences", Context.MODE_PRIVATE)
                val isAlarmOn = prefs.getBoolean("flutter." + "is alarm on", false)
                Log.d("MAIn ACTIVITY", "=========================>$isAlarmOn")
                if (permission) {
                    setAlarm()
                    val serviceIntent = Intent(this, LocationService::class.java)
                    serviceIntent.putExtra("inputExtra", "passing any text")
                    ContextCompat.startForegroundService(this, serviceIntent)

                    result.success("success")

//                    GlobalScope.launch {
//                        var forService = Intent(this@MainActivity, LocationService::class.java)
//
//                        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
////                            startForegroundService(forService);
////                            Intent(this, MyBoundService::class.java).also { intent ->
////                                bindService(intent, serviceConnection, Context.BIND_AUTO_CREATE)
////                            }
////                            bindService(forService,mConnection, Context.BIND_AUTO_CREATE)
////                            startService(forService)
//                            startForegroundService(forService)
//
//                        } else {
//                            startService(forService);
////                            bindService(forService,mConnection, Context.BIND_AUTO_CREATE)
//                        }
////                        runOnUiThread{
////                            startForegroundService(forService)
////                        }
//
//
//                    }
                }


            }
            if (call.method == "stopService") {
                val serviceIntent = Intent(this, LocationService::class.java)
                Log.d("Stop Button", "Stop Service button")
//
                stopService(serviceIntent)
                cancelAlarm()
                result.success("success")
            }

            if (call.method == "setSharedPrefValue") {
                val value: Boolean? = call.argument<Boolean>("value")
                val prefs =
                    context.getSharedPreferences("kotlinsharedpreference", Context.MODE_PRIVATE)

                with(prefs.edit()) {
                    if (value != null) {
                        putBoolean("service-enabled", value)
                        apply()
                    }
                }

                result.success(value)
            }

            if (call.method == "getSharedPrefValue") {
                val prefs =
                    context.getSharedPreferences("kotlinsharedpreference", Context.MODE_PRIVATE)
                val prefVal = prefs.getBoolean("service-enabled", false)
                result.success(prefVal)
            }
//            if (call.method == "setAlarm") {
//                cancelAlarm()
//                setAlarm()
//            }
//            if (call.method == "cancelAlarm") {
//                cancelAlarm()
//            }

        }
    }


    @RequiresApi(Build.VERSION_CODES.O)
    private fun checkIsServiceOn() {

        val prefs = context.getSharedPreferences("kotlinsharedpreference", Context.MODE_PRIVATE)
        val prefVal = prefs.getBoolean("service-enabled", false)
        val sharedPreferences =
            getSharedPreferences("FlutterSharedPreferences", Context.MODE_PRIVATE)
        val userId = sharedPreferences?.getString("flutter." + "unique id", "")


        var date: String? = null
        var todayDate = convertTimestampToDate(Timestamp.now())
        var lastModifiedDate: Timestamp? = null
        var internalId: String? = null

        Log.d("MAIN", "$prefVal")


//        FirebaseFirestore.getInstance().collection("in")
//            .document("settings").get().addOnSuccessListener{ doc ->
//            Log.d("MAIN","${doc}")
//        }


        if (prefVal == true) {
            Log.d("MAIN", "Working main case")
            if (!checkIsRunning() && userId != "") {
                FirebaseFirestore.getInstance().collection("out_emp_app")
                    .document(userId.toString())
                    .collection("work_logs")
                    .orderBy("date_time", Query.Direction.DESCENDING).limit(1)
                    .get().addOnSuccessListener { document ->
                        if (document != null) {
                            var data = document.getDocuments()[0].data
                            lastModifiedDate =
                                data!!["last_modified"] as com.google.firebase.Timestamp
                            internalId = data!!["internal_id"] as String
                            var timestamp = data!!["start_time"] as com.google.firebase.Timestamp
                            date = convertTimestampToDate(timestamp)
                            Log.d("MAIN", "$date!!")

                            if (date != null && todayDate != date) {
                                Log.d("MAIN", "Working if case")

                                val serviceIntent = Intent(this, LocationService::class.java)
                                serviceIntent.putExtra("inputExtra", "passing any text")
                                stopService(serviceIntent)

                                with(prefs.edit()) {
                                    putBoolean("service-enabled", false)
                                    apply()
                                }

                                var docData = hashMapOf<String, Any>(
                                    "stop_time" to lastModifiedDate!!
                                )

                                FirebaseFirestore.getInstance().collection("out_emp_app")
                                    .document(userId.toString())
                                    .collection("work_logs")
                                    .document(internalId!!.toString()).update(docData)
                                    .addOnSuccessListener {
                                        Log.d(
                                            "MAIN",
                                            "DocumentSnapshot successfully updated!"
                                        )
                                        Log.d("MAIN", "success")
                                    }
                                    .addOnFailureListener { e ->
                                        Log.w(
                                            "MAIN",
                                            "Error updating document",
                                            e
                                        )
                                    }


                            } else if (date != null && todayDate == date) {
                                val serviceIntent = Intent(this, LocationService::class.java)
                                serviceIntent.putExtra("inputExtra", "passing any text")
                                ContextCompat.startForegroundService(this, serviceIntent)
                                setAlarm()
                                Log.d("MAIN", "Working inside else case")
                            }

                        }

                    }
            }


        }

    }


    @RequiresApi(Build.VERSION_CODES.M)
    fun checkIsRunning(): Boolean {
        var isServiceRunning = false;

        val manager = getSystemService(NotificationManager::class.java)
        for (notification in manager.activeNotifications) {
            if (if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                    notification.notification.channelId == LocationService.CHANNEL_ID
                } else {
                    TODO("VERSION.SDK_INT < O")
                }
            ) {
                isServiceRunning = true;

                break;
            }
        }


        return isServiceRunning
    }

/*
    private fun isServiceRunning(): Boolean {
        val manager: ActivityManager = getSystemService(ACTIVITY_SERVICE) as ActivityManager
        for (service in manager.getRunningServices(Int.MAX_VALUE)) {
            if ("com.noransoft.rep_chat.LocationService" == service.service.className) {
                return true
            }
        }
        return false
    }


 */


    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val name = "RepChat Dentium"
            val description = "Work Log Status"
            val importance = NotificationManager.IMPORTANCE_HIGH
            val channel = NotificationChannel("android", name, importance)
            channel.description = description

            val notificationManager = getSystemService(NotificationManager::class.java)
            notificationManager.createNotificationChannel(channel)
        }
    }


    private fun convertTimestampToDate(timestamp: Timestamp): String {
        val milliseconds = timestamp.seconds * 1000 + timestamp.nanoseconds / 1000000
        val sdf = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            SimpleDateFormat("MM/dd/yyyy")
        } else {
            TODO("VERSION.SDK_INT < N")
        }
        val netDate = Date(milliseconds)

        return sdf.format(netDate).toString()
    }


    private fun setAlarm() {
        var intent = Intent(this, AlarmReceiver::class.java)
        var pendingIntent = PendingIntent.getBroadcast(this, 0, intent, 0)

        val calendar: Calendar = Calendar.getInstance().apply {
            timeInMillis = System.currentTimeMillis()
            set(Calendar.HOUR_OF_DAY, 23)
            set(Calendar.MINUTE, 55)
        }


        /*
         var calendar = Calendar.getInstance()
         calendar.set(Calendar.HOUR_OF_DAY, 23)
         calendar.set(Calendar.MINUTE, 55)
         calendar.set(Calendar.SECOND, 0)
         calendar.set(Calendar.MILLISECOND, 0)

         if (Calendar.getInstance().after(calendar)) {
             calendar.add(Calendar.DAY_OF_MONTH, 1);
         }

         */

        alarmManager.setInexactRepeating(
            AlarmManager.RTC_WAKEUP,
            calendar.timeInMillis,
            AlarmManager.INTERVAL_DAY,
            pendingIntent
        )
    }

    fun cancelAlarm() {
        var intent = Intent(this, AlarmReceiver::class.java)
        var pendingIntent = PendingIntent.getBroadcast(this, 0, intent, 0)

        if (alarmManager == null) {
            alarmManager = getSystemService(Context.ALARM_SERVICE) as AlarmManager
        }

        alarmManager.cancel(pendingIntent)
    }


    companion object {
        private const val REQUEST_PERMISSIONS = 100
        var CHANNEL_ID = "autoStartServiceChannel";
        var CHANNEL_NAME = "Auto Start Service Channel"
    }

    private fun fn_permission() {
        if (ContextCompat.checkSelfPermission(
                applicationContext,
                Manifest.permission.ACCESS_FINE_LOCATION
            ) !== PackageManager.PERMISSION_GRANTED && ContextCompat.checkSelfPermission(
                applicationContext,
                Manifest.permission.ACCESS_FINE_LOCATION
            ) !== PackageManager.PERMISSION_GRANTED
        ) {
            if (ActivityCompat.shouldShowRequestPermissionRationale(
                    this@MainActivity,
                    Manifest.permission.ACCESS_FINE_LOCATION
                ) && ActivityCompat.shouldShowRequestPermissionRationale(
                    this@MainActivity,
                    Manifest.permission.ACCESS_BACKGROUND_LOCATION
                ) && ActivityCompat.shouldShowRequestPermissionRationale(
                    this@MainActivity,
                    Manifest.permission.ACCESS_COARSE_LOCATION
                ) && ActivityCompat.shouldShowRequestPermissionRationale(
                    this@MainActivity,
                    Manifest.permission.FOREGROUND_SERVICE
                )
            ) {
            } else {
                ActivityCompat.requestPermissions(
                    this@MainActivity, arrayOf(
                        Manifest.permission.ACCESS_FINE_LOCATION,
                        Manifest.permission.ACCESS_BACKGROUND_LOCATION,
                        Manifest.permission.ACCESS_COARSE_LOCATION,
                        Manifest.permission.FOREGROUND_SERVICE
                    ),
                    REQUEST_PERMISSIONS
                )
            }
        } else {
            permission = true
        }
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        when (requestCode) {
            REQUEST_PERMISSIONS -> {
                if (grantResults.isNotEmpty() && grantResults[0] === PackageManager.PERMISSION_GRANTED) {
                    permission = true
                } else {
                    Toast.makeText(
                        applicationContext,
                        "Please allow the permission",
                        Toast.LENGTH_LONG
                    ).show()
                }
            }
        }
    }


    private val mConnection: ServiceConnection = object : ServiceConnection {
        override fun onServiceConnected(className: ComponentName, service: IBinder) {
            // This is called when the connection with the service has been
            // established, giving us the service object we can use to
            // interact with the service.  Because we have bound to a explicit
            // service that we know is running in our own process, we can
            // cast its IBinder to a concrete class and directly access it.
            val binder = service as LocationService.LocalBinder

            mService = binder.service
            mBound = true


        }

        override fun onServiceDisconnected(className: ComponentName) {
            // This is called when the connection with the service has been
            // unexpectedly disconnected -- that is, its process crashed.
            // Because it is running in our same process, we should never
            // see this happen.
//            mLocationService = null
//            Toast.makeText(this@Binding, R.string.local_service_disconnected,
//                    Toast.LENGTH_SHORT).show()
            mBound = false
        }
    }


}




