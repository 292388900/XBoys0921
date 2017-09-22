#PendingIntent
要处理延迟的Intent  
一个Intent的描述，以及将要表现的行动。  

+ getActivity(Context, int, Intent, int)  
+ getActivities(Context, int, Intent[], int)
+ getBroadcast(Context, int, Intent, int)
+ getService(Context, int, Intent, int)

Intent和PendingIntent的区别：  
1. Intent是立即使用的，而PendingIntent可以等到事件发生后触发，PendingIntent可以cancel  
2. Intent在程序结束后即终止，而PendingIntent在程序结束后依然有效  
3. PendingIntent自带Context，而Intent需要在某个Context内运行  
4. Intent在原task中运行，PendingIntent在新的task中运行 




#Nested classes
	class	PendingIntent.CanceledException
	Exception thrown when trying to send through a PendingIntent that has been canceled or is otherwise no longer able to execute the request.
 
	interface	PendingIntent.OnFinished
	Callback interface for discovering when a send operation has completed. 
#Constants
	int	FLAG_CANCEL_CURRENT
	Flag indicating that if the described PendingIntent already exists, the current one should be canceled before generating a new one.
	int	FLAG_IMMUTABLE
	Flag indicating that the created PendingIntent should be immutable.
	int	FLAG_NO_CREATE
	Flag indicating that if the described PendingIntent does not already exist, then simply return null instead of creating it.
	int	FLAG_ONE_SHOT
	Flag indicating that this PendingIntent can be used only once.
	int	FLAG_UPDATE_CURRENT
	Flag indicating that if the described PendingIntent already exists, then keep it but replace its extra data with what is in this new Intent. 
#公有方法
	void	cancel()
	Cancel a currently active PendingIntent.

	int	describeContents()
	Describe the kinds of special objects contained in this Parcelable instance's marshaled representation.

	boolean	equals(Object otherObj)
	Comparison operator on two PendingIntent objects, such that true is returned then they both represent the same operation from the same package.

	static PendingIntent	getActivities(Context context, int requestCode, Intent[] intents, int flags, Bundle options)
	Like getActivity(Context, int, Intent, int), but allows an array of Intents to be supplied.

	static PendingIntent	getActivities(Context context, int requestCode, Intent[] intents, int flags)
	Like getActivity(Context, int, Intent, int), but allows an array of Intents to be supplied.

	static PendingIntent	getActivity(Context context, int requestCode, Intent intent, int flags)
	Retrieve a PendingIntent that will start a new activity, like calling Context.startActivity(Intent).

	static PendingIntent	getActivity(Context context, int requestCode, Intent intent, int flags, Bundle options)
	Retrieve a PendingIntent that will start a new activity, like calling Context.startActivity(Intent).

	static PendingIntent	getBroadcast(Context context, int requestCode, Intent intent, int flags)
	Retrieve a PendingIntent that will perform a broadcast, like calling Context.sendBroadcast().

	String	getCreatorPackage()
	Return the package name of the application that created this PendingIntent, that is the identity under which you will actually be sending the Intent.

	int	getCreatorUid()
	Return the uid of the application that created this PendingIntent, that is the identity under which you will actually be sending the Intent.

	UserHandle	getCreatorUserHandle()
	Return the user handle of the application that created this PendingIntent, that is the user under which you will actually be sending the Intent.

	static PendingIntent	getForegroundService(Context context, int requestCode, Intent intent, int flags)
	Retrieve a PendingIntent that will start a foreground service, like calling Context.startForegroundService().

	IntentSender	getIntentSender()
	Retrieve a IntentSender object that wraps the existing sender of the PendingIntent
	static PendingIntent	getService(Context context, int requestCode, Intent intent, int flags)
	Retrieve a PendingIntent that will start a service, like calling Context.startService().

	String	getTargetPackage()
	This method was deprecated in API level 17. Renamed to getCreatorPackage().

	int	hashCode()
	Returns a hash code value for the object.

	static PendingIntent	readPendingIntentOrNullFromParcel(Parcel in)
	Convenience function for reading either a Messenger or null pointer from a Parcel.

	void	send(Context context, int code, Intent intent, PendingIntent.OnFinished onFinished, Handler handler, String requiredPermission, Bundle options)
	Perform the operation associated with this PendingIntent, allowing the caller to specify information about the Intent to use and be notified when the send has completed.

	void	send()
	Perform the operation associated with this PendingIntent.

	void	send(Context context, int code, Intent intent, PendingIntent.OnFinished onFinished, Handler handler)
	Perform the operation associated with this PendingIntent, allowing the caller to specify information about the Intent to use and be notified when the send has completed.

	void	send(Context context, int code, Intent intent, PendingIntent.OnFinished onFinished, Handler handler, String requiredPermission)
	Perform the operation associated with this PendingIntent, allowing the caller to specify information about the Intent to use and be notified when the send has completed.

	void	send(int code, PendingIntent.OnFinished onFinished, Handler handler)
	Perform the operation associated with this PendingIntent, allowing the caller to be notified when the send has completed.

	void	send(Context context, int code, Intent intent)
	Perform the operation associated with this PendingIntent, allowing the caller to specify information about the Intent to use.

	void	send(int code)
	Perform the operation associated with this PendingIntent.

	String	toString()
	Returns a string representation of the object.
	static void	writePendingIntentOrNullToParcel(PendingIntent sender, Parcel out)
	Convenience function for writing either a PendingIntent or null pointer to a Parcel.

	void	writeToParcel(Parcel out, int flags)
	Flatten this object in to a Parcel.、
#变量
														public static final Creator<PendingIntent>	CREATOR