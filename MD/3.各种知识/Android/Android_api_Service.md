#Service

java.lang.Object  
   ↳	android.content.Context  
 	   ↳	android.content.ContextWrapper  
 	 	   ↳	android.app.Service  
直接子类
	AbstractInputMethodService	AbstractInputMethodService provides a abstract base class for input methods. 

	AccessibilityService	Accessibility services should only be used to assist users with disabilities in using Android devices and apps.
 
	AutofillService	Top-level service of the current autofill service for a given user. 

	CallScreeningService	This service can be implemented by the default dialer (see getDefaultDialerPackage()) to allow or disallow incoming calls before they are shown to a user. 

	CameraPrewarmService	Extend this class to implement a camera prewarm service. 
	CarrierMessagingService	A service that receives calls from the system when new SMS and MMS are sent or received. 

	CarrierService	A service that exposes carrier-specific functionality to the system. 

	ChooserTargetService	A service that receives calls from the system when the user is asked to choose a target for an intent explicitly by another app. 

	ConditionProviderService	A service that provides conditions about boolean state. 

	ConnectionService	An abstract service that should be implemented by any apps which either:
	Can make phone calls (VoIP or otherwise) and want those calls to be integrated into the built-in phone app. 

	CustomTabsService	Abstract service class for implementing Custom Tabs related functionality. 

	DeviceAdminService	Base class for a service that device owner/profile owners can optionally have.
 
	DreamService	Extend this class to implement a custom dream (available to the user as a "Daydream"). 

	HostApduService	
	HostApduService is a convenience Service class that can be extended to emulate an NFC card inside an Android service component. 

	HostNfcFService	
	HostNfcFService is a convenience Service class that can be extended to emulate an NFC-F card inside an Android service component. 

	InCallService	This service is implemented by any app that wishes to provide the user-interface for managing phone calls. 

	IntentService	IntentService is a base class for Services that handle asynchronous requests (expressed as Intents) on demand. 

	JobService	
	Entry point for the callback from the JobScheduler. 

	MediaBrowserService	Base class for media browser services. 

	MediaBrowserServiceCompat	Base class for media browse services. 

	MediaRouteProviderService	Base class for media route provider services. 

	MidiDeviceService	A service that implements a virtual MIDI device. 

	NotificationCompatSideChannelService	Abstract service to receive side channel notifications sent from NotificationManagerCompat. 

	NotificationListenerService	A service that receives calls from the system when new notifications are posted or removed, or their ranking changed. 

	OffHostApduService	
	OffHostApduService is a convenience Service class that can be extended to describe one or more NFC applications that are residing off-host, for example on an embedded secure element or a UICC. 
	PostMessageService	A service to receive postMessage related communication from a Custom Tabs provider. 

	PrintService	
	This is the base class for implementing print services. 

	RecognitionService	This class provides a base class for recognition service implementations. 

	RemoteViewsService	The service to be connected to for a remote adapter to request RemoteViews. 

	SettingInjectorService	Dynamically specifies the enabled status of a preference injected into the list of app settings displayed by the system settings app
	For use only by apps that are included in the system image, for preferences that affect multiple apps. 

	SpellCheckerService	SpellCheckerService provides an abstract base class for a spell checker. 
	TextToSpeechService	Abstract base class for TTS engine implementations. 

	TileService	A TileService provides the user a tile that can be added to Quick Settings. 

	TvInputService	The TvInputService class represents a TV input or source such as HDMI or built-in tuner which provides pass-through video or broadcast TV programs. 

	VisualVoicemailService	This service is implemented by dialer apps that wishes to handle OMTP or similar visual voicemails. 

	VoiceInteractionService	Top-level service of the current global voice interactor, which is providing support for hotwording, the back-end of a VoiceInteractor, etc. 

	VoiceInteractionSessionService	An active voice interaction session, initiated by a VoiceInteractionService. 

	VpnService	VpnService is a base class for applications to extend and build their own VPN solutions. 

	VrListenerService	A service that is bound from the system while running in virtual reality (VR) mode. 

	WallpaperService	A wallpaper service is responsible for showing a live wallpaper behind applications that would like to sit on top of it. 
间接子类  
	InputMethodService

Topics covered here:

	What is a Service?
	Service Lifecycle
	Permissions
	Process Lifecycle
	Local Service Sample
	Remote Messenger Service Sample

#服务
Context.startService()
Context.bindService()

#Constants
	int	START_CONTINUATION_MASK
	Bits returned by onStartCommand(Intent, int, int) describing how to continue the service if it is killed.
	int	START_FLAG_REDELIVERY
	This flag is set in onStartCommand(Intent, int, int) if the Intent is a re-delivery of a previously delivered intent, because the service had previously returned START_REDELIVER_INTENT but had been killed before calling stopSelf(int) for that Intent.
	int	START_FLAG_RETRY
	This flag is set in onStartCommand(Intent, int, int) if the Intent is a retry because the original attempt never got to or returned from onStartCommand(Intent, int, int).
	int	START_NOT_STICKY
	Constant to return from onStartCommand(Intent, int, int): if this service's process is killed while it is started (after returning from onStartCommand(Intent, int, int)), and there are no new start intents to deliver to it, then take the service out of the started state and don't recreate until a future explicit call to Context.startService(Intent).
	int	START_REDELIVER_INTENT
	Constant to return from onStartCommand(Intent, int, int): if this service's process is killed while it is started (after returning from onStartCommand(Intent, int, int)), then it will be scheduled for a restart and the last delivered Intent re-delivered to it again via onStartCommand(Intent, int, int).
	int	START_STICKY
	Constant to return from onStartCommand(Intent, int, int): if this service's process is killed while it is started (after returning from onStartCommand(Intent, int, int)), then leave it in the started state but don't retain this delivered intent.
	int	START_STICKY_COMPATIBILITY
	Constant to return from onStartCommand(Intent, int, int): compatibility version of START_STICKY that does not guarantee that onStartCommand(Intent, int, int) will be called again after being killed.
	int	STOP_FOREGROUND_DETACH
	Flag for stopForeground(int): if set, the notification previously provided to startForeground(int, Notification) will be detached from the service.
	int	STOP_FOREGROUND_REMOVE
	Flag for stopForeground(int): if set, the notification previously provided to startForeground(int, Notification) will be removed.

#public methods
	final Application	getApplication()
	Return the application that owns this service.
	abstract IBinder	onBind(Intent intent)
	Return the communication channel									 to the service.
	void	onConfigurationChanged(Configuration newConfig)
	Called by the system when the device configuration changes while your component is running.
	void	onCreate()
	Called by the system when the service is first created.
	void	onDestroy()
	Called by the system to notify a Service that it is no longer used and is being removed.
	void	onLowMemory()
	This is called when the overall system is running low on memory, and actively running processes should trim their memory usage.
	void	onRebind(Intent intent)
	Called when new clients have connected to the service, after it had previously been notified that all had disconnected in its onUnbind(Intent).
	void	onStart(Intent intent, int startId)
	This method was deprecated in API level 5. Implement onStartCommand(Intent, int, int) instead.
	int	onStartCommand(Intent intent, int flags, int startId)
	Called by the system every time a client explicitly starts the service by calling startService(Intent), providing the arguments it supplied and a unique integer token representing the start request.
	void	onTaskRemoved(Intent rootIntent)
	This is called if the service is currently running and the user has removed a task that comes from the service's application.
	void	onTrimMemory(int level)
	Called when the operating system has determined that it is a good time for a process to trim unneeded memory from its process.
	boolean	onUnbind(Intent intent)
	Called when all clients have disconnected from a particular interface published by the service.
	final void	startForeground(int id, Notification notification)
	Make this service run in the foreground, supplying the ongoing notification to be shown to the user while in this state.
	final void	stopForeground(int flags)
	Remove this service from foreground state, allowing it to be killed if more memory is needed.
	final void	stopForeground(boolean removeNotification)
	Synonym for stopForeground(int).
	final void	stopSelf()
	Stop the service, if it was previously started.
	final void	stopSelf(int startId)
	Old version of stopSelfResult(int) that doesn't return a result.
	final boolean	stopSelfResult(int startId)
	Stop the service if the most recent time it was started was startId.