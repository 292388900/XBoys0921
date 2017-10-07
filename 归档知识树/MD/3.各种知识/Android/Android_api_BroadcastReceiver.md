#BroadcastReceiver

直接子类：
AppWidgetProvider
DeviceAdminReceiver
MediaButtonReceiver
RestrictionsReceiver
WakefulBroadcastReceiver

sendBroadcast(Intent)
Context.registerReceiver()

#Nested classes
	class	BroadcastReceiver.PendingResult
	State for a result that is pending for a broadcast receiver. 

#Public methods
	final void	abortBroadcast()
	Sets the flag indicating that this receiver should abort the current broadcast; only works with broadcasts sent through Context.sendOrderedBroadcast.
	final void	clearAbortBroadcast()
	Clears the flag indicating that this receiver should abort the current broadcast.
	final boolean	getAbortBroadcast()
	Returns the flag indicating whether or not this receiver should abort the current broadcast.
	final boolean	getDebugUnregister()
	Return the last value given to setDebugUnregister(boolean).
	final int	getResultCode()
	Retrieve the current result code, as set by the previous receiver.
	final String	getResultData()
	Retrieve the current result data, as set by the previous receiver.
	final Bundle	getResultExtras(boolean makeMap)
	Retrieve the current result extra data, as set by the previous receiver.
	final BroadcastReceiver.PendingResult	goAsync()
	This can be called by an application in onReceive(Context, Intent) to allow it to keep the broadcast active after returning from that function.
	final boolean	isInitialStickyBroadcast()
	Returns true if the receiver is currently processing the initial value of a sticky broadcast -- that is, the value that was last broadcast and is currently held in the sticky cache, so this is not directly the result of a broadcast right now.
	final boolean	isOrderedBroadcast()
	Returns true if the receiver is currently processing an ordered broadcast.
	abstract void	onReceive(Context context, Intent intent)
	This method is called when the BroadcastReceiver is receiving an Intent broadcast.
	IBinder	peekService(Context myContext, Intent service)
	Provide a binder to an already-bound service.
	final void	setDebugUnregister(boolean debug)
	Control inclusion of debugging help for mismatched calls to Context.registerReceiver().
	final void	setOrderedHint(boolean isOrdered)
	For internal use, sets the hint about whether this BroadcastReceiver is running in ordered mode.
	final void	setResult(int code, String data, Bundle extras)
	Change all of the result data returned from this broadcasts; only works with broadcasts sent through Context.sendOrderedBroadcast.
	final void	setResultCode(int code)
	Change the current result code of this broadcast; only works with broadcasts sent through Context.sendOrderedBroadcast.
	final void	setResultData(String data)
	Change the current result data of this broadcast; only works with broadcasts sent through Context.sendOrderedBroadcast.
	final void	setResultExtras(Bundle extras)
	Change the current result extras of this broadcast; only works with broadcasts sent through Context.sendOrderedBroadcast.