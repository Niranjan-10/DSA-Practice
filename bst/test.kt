    
    /*
    <queries>
        <intent>
            <action android:name="android.media.action.IMAGE_CAPTURE" />
        </intent>
    </queries>

    */




    @TargetApi(30)
    private fun Context.checkBackgroundLocationPermissionAPI30(backgroundLocationRequestCode: Int) {
        if (checkSinglePermission(Manifest.permission.ACCESS_FINE_LOCATION)) return
                requestPermissions(arrayOf(Manifest.permission.ACCESS_FINE_LOCATION), backgroundLocationRequestCode)
    }

     if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.R){
            checkBackgroundLocationPermissionAPI30(REQUEST_PERMISSIONS)
        }


         private fun Context.checkSinglePermission(permission: String) : Boolean {
        return ContextCompat.checkSelfPermission(this, permission) == PackageManager.PERMISSION_GRANTED
    }

//dart
    locationPermission = await Permission.locationAlways.isGranted;
