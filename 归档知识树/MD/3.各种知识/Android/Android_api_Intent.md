# Intent

**action**: 执行的动作 ACTION_VIEW, ACTION_EDIT, ACTION_MAIN  
**data**: 携带的信息 expressed as a Uri

**category**: action 去执行的附加信息   
**type**:  data的显式类型
**component**： 使用intent的组件显式的名字。   
**extras**：其他任何的额外信息 Bundle

#Intent 解析

显式Intent setComponent(ComponentName) setClass(Context Class)

隐式Intent 系统根据信息匹配Intent的目标
Activity, BroadcastReceiver, or Service

intent resolution mechanism 

<intent-filter> 

registerReceiver(BroadcastReceiver, IntentFilter) 


#标准Activity actions  
 startActivity(Intent)

	ACTION_MAIN
	ACTION_VIEW
	ACTION_ATTACH_DATA
	ACTION_EDIT
	ACTION_PICK
	ACTION_CHOOSER
	ACTION_GET_CONTENT
	ACTION_DIAL
	ACTION_CALL
	ACTION_SEND
	ACTION_SENDTO
	ACTION_ANSWER
	ACTION_INSERT
	ACTION_DELETE
	ACTION_RUN
	ACTION_SYNC
	ACTION_PICK_ACTIVITY
	ACTION_SEARCH
	ACTION_WEB_SEARCH
	ACTION_FACTORY_TEST
#标准Broadcast Actions
registerReceiver(BroadcastReceiver, IntentFilter) or a <receiver> tag in a manifest
	
	ACTION_TIME_CHANGED
	ACTION_TIMEZONE_CHANGED
	ACTION_BOOT_COMPLETED
	ACTION_PACKAGE_ADDED
	ACTION_PACKAGE_CHANGED
	ACTION_PACKAGE_REMOVED
	ACTION_PACKAGE_RESTARTED
	ACTION_PACKAGE_DATA_CLEARED
	ACTION_PACKAGES_SUSPENDED
	ACTION_PACKAGES_UNSUSPENDED
	ACTION_UID_REMOVED
	ACTION_BATTERY_CHANGED
	ACTION_POWER_CONNECTED
	ACTION_POWER_DISCONNECTED
	ACTION_SHUTDOWN
#标准 Categories
 addCategory(String)

	CATEGORY_DEFAULT
	CATEGORY_BROWSABLE
	CATEGORY_TAB
	CATEGORY_ALTERNATIVE
	CATEGORY_SELECTED_ALTERNATIVE
	CATEGORY_LAUNCHER
	CATEGORY_INFO
	CATEGORY_HOME
	CATEGORY_PREFERENCE
	CATEGORY_TEST
	CATEGORY_CAR_DOCK
	CATEGORY_DESK_DOCK
	CATEGORY_LE_DESK_DOCK
	CATEGORY_HE_DESK_DOCK
	CATEGORY_CAR_MODE
	CATEGORY_APP_MARKET
	CATEGORY_VR_HOME
# putExtra(String, Bundle)

	EXTRA_ALARM_COUNT
	EXTRA_BCC
	EXTRA_CC
	EXTRA_CHANGED_COMPONENT_NAME
	EXTRA_DATA_REMOVED
	EXTRA_DOCK_STATE
	EXTRA_DOCK_STATE_HE_DESK
	EXTRA_DOCK_STATE_LE_DESK
	EXTRA_DOCK_STATE_CAR
	EXTRA_DOCK_STATE_DESK
	EXTRA_DOCK_STATE_UNDOCKED
	EXTRA_DONT_KILL_APP
	EXTRA_EMAIL
	EXTRA_INITIAL_INTENTS
	EXTRA_INTENT
	EXTRA_KEY_EVENT
	EXTRA_ORIGINATING_URI
	EXTRA_PHONE_NUMBER
	EXTRA_REFERRER
	EXTRA_REMOTE_INTENT_TOKEN
	EXTRA_REPLACING
	EXTRA_SHORTCUT_ICON
	EXTRA_SHORTCUT_ICON_RESOURCE
	EXTRA_SHORTCUT_INTENT
	EXTRA_STREAM
	EXTRA_SHORTCUT_NAME
	EXTRA_SUBJECT
	EXTRA_TEMPLATE
	EXTRA_TEXT
	EXTRA_TITLE
	EXTRA_UID
#Flags
 setFlags(int) and addFlags(int).  setFlags(int)

#公有构造函数
	Intent()
	Create an empty intent.

	Intent(Intent o)
	Copy constructor.

	Intent(String action)
	Create an intent with a given action.

	Intent(String action, Uri uri)
	Create an intent with a given action and for a given data url.

	Intent(Context packageContext, Class<?> cls)
	Create an intent for a specific component.

	Intent(String action, Uri uri, Context packageContext, Class<?> cls)
	Create an intent for a specific component with a specified action and data.

#公共函数

	Intent	addCategory(String category)
	Add a new category to the intent.

	Intent	addFlags(int flags)
	Add additional flags to the intent (or with existing flags value).

	Object	clone()
	Creates and returns a copy of this object.

	Intent	cloneFilter()
	Make a clone of only the parts of the Intent that are relevant for filter matching: the action, data, type, component, and categories.

	static Intent	createChooser(Intent target, CharSequence title, IntentSender sender)
	Convenience function for creating a ACTION_CHOOSER Intent.

	static Intent	createChooser(Intent target, CharSequence title)
	Convenience function for creating a ACTION_CHOOSER Intent.

	int	describeContents()
	Describe the kinds of special objects contained in this Parcelable instance's marshaled representation.

	int	fillIn(Intent other, int flags)
	Copy the contents of other in to this object, but only where fields are not defined by this object.
	boolean	filterEquals(Intent other)
	Determine if two intents are the same for the purposes of intent resolution (filtering).

	int	filterHashCode()
	Generate hash code that matches semantics of filterEquals().

	String	getAction()
	Retrieve the general action to be performed, such as ACTION_VIEW.

	boolean[]	getBooleanArrayExtra(String name)
	Retrieve extended data from the intent.

	boolean	getBooleanExtra(String name, boolean defaultValue)
	Retrieve extended data from the intent.

	Bundle	getBundleExtra(String name)
	Retrieve extended data from the intent.

	byte[]	getByteArrayExtra(String name)
	Retrieve extended data from the intent.

	byte	getByteExtra(String name, byte defaultValue)
	Retrieve extended data from the intent.

	Set<String>	getCategories()
	Return the set of all categories in the intent.
	char[]	getCharArrayExtra(String name)
	Retrieve extended data from the intent.

	char	getCharExtra(String name, char defaultValue)
	Retrieve extended data from the intent.

	CharSequence[]	getCharSequenceArrayExtra(String name)
	Retrieve extended data from the intent.

	ArrayList<CharSequence>	getCharSequenceArrayListExtra(String name)
	Retrieve extended data from the intent.

	CharSequence	getCharSequenceExtra(String name)
	Retrieve extended data from the intent.

	ClipData	getClipData()
	Return the ClipData associated with this Intent.

	ComponentName	getComponent()
	Retrieve the concrete component associated with the intent.

	Uri	getData()
	Retrieve data this intent is operating on.

	String	getDataString()
	The same as getData(), but returns the URI as an encoded String.

	double[]	getDoubleArrayExtra(String name)
	Retrieve extended data from the intent.

	double	getDoubleExtra(String name, double defaultValue)
	Retrieve extended data from the intent.

	Bundle	getExtras()
	Retrieves a map of extended data from the intent.
	int	getFlags()
	Retrieve any special flags associated with this intent.

	float[]	getFloatArrayExtra(String name)
	Retrieve extended data from the intent.

	float	getFloatExtra(String name, float defaultValue)
	Retrieve extended data from the intent.

	int[]	getIntArrayExtra(String name)
	Retrieve extended data from the intent.

	int	getIntExtra(String name, int defaultValue)
	Retrieve extended data from the intent.

	ArrayList<Integer>	getIntegerArrayListExtra(String name)
	Retrieve extended data from the intent.

	static Intent	getIntent(String uri)
	This method was deprecated in API level 4. Use parseUri(String, int) instead.

	static Intent	getIntentOld(String uri)
	long[]	getLongArrayExtra(String name)
	Retrieve extended data from the intent.

	long	getLongExtra(String name, long defaultValue)
	Retrieve extended data from the intent.

	String	getPackage()
	Retrieve the application package name this Intent is limited to.

	Parcelable[]	getParcelableArrayExtra(String name)
	Retrieve extended data from the intent.

	<T extends Parcelable> ArrayList<T>	getParcelableArrayListExtra(String name)
	Retrieve extended data from the intent.
	<T extends Parcelable> T	getParcelableExtra(String name)
	Retrieve extended data from the intent.

	String	getScheme()
	Return the scheme portion of the intent's data.

	Intent	getSelector()
	Return the specific selector associated with this Intent.

	Serializable	getSerializableExtra(String name)
	Retrieve extended data from the intent.

	short[]	getShortArrayExtra(String name)
	Retrieve extended data from the intent.

	short	getShortExtra(String name, short defaultValue)
	Retrieve extended data from the intent.

	Rect	getSourceBounds()
	Get the bounds of the sender of this intent, in screen coordinates.

	String[]	getStringArrayExtra(String name)
	Retrieve extended data from the intent.

	ArrayList<String>	getStringArrayListExtra(String name)
	Retrieve extended data from the intent.

	String	getStringExtra(String name)
	Retrieve extended data from the intent.

	String	getType()
	Retrieve any explicit MIME type included in the intent.

	boolean	hasCategory(String category)
	Check if a category exists in the intent.

	boolean	hasExtra(String name)
	Returns true if an extra value is associated with the given name.

	boolean	hasFileDescriptors()
	Returns true if the Intent's extras contain a parcelled file descriptor.

	static Intent	makeMainActivity(ComponentName mainActivity)
	Create an intent to launch the main (root) activity of a task.

	static Intent	makeMainSelectorActivity(String selectorAction, String selectorCategory)
	Make an Intent for the main activity of an application, without specifying a specific activity to run but giving a selector to find the activity.

	static Intent	makeRestartActivityTask(ComponentName mainActivity)
	Make an Intent that can be used to re-launch an application's task in its base state.

	static String	normalizeMimeType(String type)
	Normalize a MIME data type.

	static Intent	parseIntent(Resources resources, XmlPullParser parser, AttributeSet attrs)
	Parses the "intent" element (and its children) from XML and instantiates an Intent object.

	static Intent	parseUri(String uri, int flags)
	Create an intent from a URI.

	Intent	putCharSequenceArrayListExtra(String name, ArrayList<CharSequence> value)
	Add extended data to the intent.

	Intent	putExtra(String name, Parcelable value)
	Add extended data to the intent.

	Intent	putExtra(String name, long[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, byte value)
	Add extended data to the intent.

	Intent	putExtra(String name, double[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, CharSequence value)
	Add extended data to the intent.

	Intent	putExtra(String name, boolean[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, int value)
	Add extended data to the intent.

	Intent	putExtra(String name, char[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, byte[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, Parcelable[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, Bundle value)
	Add extended data to the intent.

	Intent	putExtra(String name, CharSequence[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, float[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, double value)
	Add extended data to the intent.

	Intent	putExtra(String name, int[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, String[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, short[] value)
	Add extended data to the intent.

	Intent	putExtra(String name, boolean value)
	Add extended data to the intent.

	Intent	putExtra(String name, String value)
	Add extended data to the intent.

	Intent	putExtra(String name, long value)
	Add extended data to the intent.

	Intent	putExtra(String name, char value)
	Add extended data to the intent.

	Intent	putExtra(String name, Serializable value)
	Add extended data to the intent.

	Intent	putExtra(String name, float value)
	Add extended data to the intent.

	Intent	putExtra(String name, short value)
	Add extended data to the intent.

	Intent	putExtras(Intent src)
	Copy all extras in 'src' in to this intent.
	Intent	putExtras(Bundle extras)
	Add a set of extended data to the intent.

	Intent	putIntegerArrayListExtra(String name, ArrayList<Integer> value)
	Add extended data to the intent.

	Intent	putParcelableArrayListExtra(String name, ArrayList<? extends Parcelable> value)
	Add extended data to the intent.

	Intent	putStringArrayListExtra(String name, ArrayList<String> value)
	Add extended data to the intent.

	void	readFromParcel(Parcel in)
	void	removeCategory(String category)
	Remove a category from an intent.

	void	removeExtra(String name)
	Remove extended data from the intent.

	void	removeFlags(int flags)
	Remove these flags from the intent.

	Intent	replaceExtras(Intent src)
	Completely replace the extras in the Intent with the extras in the given Intent.

	Intent	replaceExtras(Bundle extras)
	Completely replace the extras in the Intent with the given Bundle of extras.

	ComponentName	resolveActivity(PackageManager pm)
	Return the Activity component that should be used to handle this intent.

	ActivityInfo	resolveActivityInfo(PackageManager pm, int flags)
	Resolve the Intent into an ActivityInfo describing the activity that should execute the intent.

	String	resolveType(Context context)
	Return the MIME data type of this intent.

	String	resolveType(ContentResolver resolver)
	Return the MIME data type of this intent.

	String	resolveTypeIfNeeded(ContentResolver resolver)
	Return the MIME data type of this intent, only if it will be needed for intent resolution.

	Intent	setAction(String action)
	Set the general action to be performed.

	Intent	setClass(Context packageContext, Class<?> cls)
	Convenience for calling setComponent(ComponentName) with the name returned by a Class object.

	Intent	setClassName(String packageName, String className)
	Convenience for calling setComponent(ComponentName) with an explicit application package name and class name.

	Intent	setClassName(Context packageContext, String className)
	Convenience for calling setComponent(ComponentName) with an explicit class name.

	void	setClipData(ClipData clip)
	Set a ClipData associated with this Intent.

	Intent	setComponent(ComponentName component)
	(Usually optional) Explicitly set the component to handle the intent.

	Intent	setData(Uri data)
	Set the data this intent is operating on.

	Intent	setDataAndNormalize(Uri data)
	Normalize and set the data this intent is operating on.

	Intent	setDataAndType(Uri data, String type)
	(Usually optional) Set the data for the intent along with an explicit MIME data type.

	Intent	setDataAndTypeAndNormalize(Uri data, String type)
	(Usually optional) Normalize and set both the data Uri and an explicit MIME data type.

	void	setExtrasClassLoader(ClassLoader loader)
	Sets the ClassLoader that will be used when unmarshalling any Parcelable values from the extras of this Intent.

	Intent	setFlags(int flags)
	Set special flags controlling how this intent is handled.

	Intent	setPackage(String packageName)
	(Usually optional) Set an explicit application package name that limits the components this Intent will resolve to.

	void	setSelector(Intent selector)
	Set a selector for this Intent.

	void	setSourceBounds(Rect r)
	Set the bounds of the sender of this intent, in screen coordinates.

	Intent	setType(String type)
	Set an explicit MIME data type.

	Intent	setTypeAndNormalize(String type)
	Normalize and set an explicit MIME data type.

	String	toString()
	Returns a string representation of the object.

	String	toURI()
	This method was deprecated in API level 4. Use toUri(int) instead.

	String	toUri(int flags)
	Convert this Intent into a String holding a URI representation of it.

	void	writeToParcel(Parcel out, int flags)
	Flatten this object in to a Parcel.

#嵌入类
			class	Intent.FilterComparison
			Wrapper class holding an Intent and implementing comparisons on it for the purpose of filtering. 
			class	Intent.ShortcutIconResource
			Represents a shortcut/live folder icon resource. 
#Constants
			String	ACTION_AIRPLANE_MODE_CHANGED
			Broadcast Action: The user has switched the phone into or out of Airplane Mode.
			String	ACTION_ALL_APPS
			Activity Action: List all available applications.
			String	ACTION_ANSWER
			Activity Action: Handle an incoming phone call.
			String	ACTION_APPLICATION_PREFERENCES
			An activity that provides a user interface for adjusting application preferences.
			String	ACTION_APPLICATION_RESTRICTIONS_CHANGED
			Broadcast Action: Sent after application restrictions are changed.
			String	ACTION_APP_ERROR
			Activity Action: The user pressed the "Report" button in the crash/ANR dialog.
			String	ACTION_ASSIST
			Activity Action: Perform assist action.
			String	ACTION_ATTACH_DATA
			Used to indicate that some piece of data should be attached to some other place.
			String	ACTION_BATTERY_CHANGED
			Broadcast Action: This is a sticky broadcast containing the charging state, level, and other information about the battery.
			String	ACTION_BATTERY_LOW
			Broadcast Action: Indicates low battery condition on the device.
			String	ACTION_BATTERY_OKAY
			Broadcast Action: Indicates the battery is now okay after being low.
			String	ACTION_BOOT_COMPLETED
			Broadcast Action: This is broadcast once, after the user has finished booting.
			String	ACTION_BUG_REPORT
			Activity Action: Show activity for reporting a bug.
			String	ACTION_CALL
			Activity Action: Perform a call to someone specified by the data.
			String	ACTION_CALL_BUTTON
			Activity Action: The user pressed the "call" button to go to the dialer or other appropriate UI for placing a call.
			String	ACTION_CAMERA_BUTTON
			Broadcast Action: The "Camera Button" was pressed.
			String	ACTION_CARRIER_SETUP
			Activity Action: Main entry point for carrier setup apps.
			String	ACTION_CHOOSER
			Activity Action: Display an activity chooser, allowing the user to pick what they want to before proceeding.
			String	ACTION_CLEAR_PACKAGE
			Activity Action: Launch application uninstaller.
			String	ACTION_CLOSE_SYSTEM_DIALOGS
			Broadcast Action: This is broadcast when a user action should request a temporary system dialog to dismiss.
			String	ACTION_CONFIGURATION_CHANGED
			Broadcast Action: The current device Configuration (orientation, locale, etc) has changed.
			String	ACTION_CREATE_DOCUMENT
			Activity Action: Allow the user to create a new document.
			String	ACTION_CREATE_SHORTCUT
			Activity Action: Creates a shortcut.
			String	ACTION_DATE_CHANGED
			Broadcast Action: The date has changed.
			String	ACTION_DEFAULT
			A synonym for ACTION_VIEW, the "standard" action that is performed on a piece of data.
			String	ACTION_DEFAULT_SMS_SUBSCRIPTION_CHANGED
			Broadcast Action: The default sms subscription has changed.
			String	ACTION_DEFAULT_SUBSCRIPTION_CHANGED
			Broadcast Action: The default subscription has changed.
			String	ACTION_DELETE
			Activity Action: Delete the given data from its container.
			String	ACTION_DEVICE_STORAGE_LOW
			This constant was deprecated in API level O. if your app targets O or above, this broadcast will no longer be delivered to any BroadcastReceiver defined in your manifest. Instead, apps are strongly encouraged to use the improved getCacheDir() behavior so the system can automatically free up storage when needed.
			String	ACTION_DEVICE_STORAGE_OK
			This constant was deprecated in API level O. if your app targets O or above, this broadcast will no longer be delivered to any BroadcastReceiver defined in your manifest. Instead, apps are strongly encouraged to use the improved getCacheDir() behavior so the system can automatically free up storage when needed.
			String	ACTION_DIAL
			Activity Action: Dial a number as specified by the data.
			String	ACTION_DOCK_EVENT
			Broadcast Action: A sticky broadcast for changes in the physical docking state of the device.
			String	ACTION_DREAMING_STARTED
			Broadcast Action: Sent after the system starts dreaming.
			String	ACTION_DREAMING_STOPPED
			Broadcast Action: Sent after the system stops dreaming.
			String	ACTION_EDIT
			Activity Action: Provide explicit editable access to the given data.
			String	ACTION_EXTERNAL_APPLICATIONS_AVAILABLE
			Broadcast Action: Resources for a set of packages (which were previously unavailable) are currently available since the media on which they exist is available.
			String	ACTION_EXTERNAL_APPLICATIONS_UNAVAILABLE
			Broadcast Action: Resources for a set of packages are currently unavailable since the media on which they exist is unavailable.
			String	ACTION_FACTORY_TEST
			Activity Action: Main entry point for factory tests.
			String	ACTION_GET_CONTENT
			Activity Action: Allow the user to select a particular kind of data and return it.
			String	ACTION_GET_RESTRICTION_ENTRIES
			Broadcast to a specific application to query any supported restrictions to impose on restricted users.
			String	ACTION_GTALK_SERVICE_CONNECTED
			Broadcast Action: A GTalk connection has been established.
			String	ACTION_GTALK_SERVICE_DISCONNECTED
			Broadcast Action: A GTalk connection has been disconnected.
			String	ACTION_HEADSET_PLUG
			Broadcast Action: Wired Headset plugged in or unplugged.
			String	ACTION_INPUT_METHOD_CHANGED
			Broadcast Action: An input method has been changed.
			String	ACTION_INSERT
			Activity Action: Insert an empty item into the given container.
			String	ACTION_INSERT_OR_EDIT
			Activity Action: Pick an existing item, or insert a new item, and then edit it.
			String	ACTION_INSTALL_PACKAGE
			Activity Action: Launch application installer.
			String	ACTION_LOCALE_CHANGED
			Broadcast Action: The current device's locale has changed.
			String	ACTION_LOCKED_BOOT_COMPLETED
			Broadcast Action: This is broadcast once, after the user has finished booting, but while still in the "locked" state.
			String	ACTION_MAIN
			Activity Action: Start as a main entry point, does not expect to receive data.
			String	ACTION_MANAGED_PROFILE_ADDED
			Broadcast sent to the primary user when an associated managed profile is added (the profile was created and is ready to be used).
			String	ACTION_MANAGED_PROFILE_AVAILABLE
			Broadcast sent to the primary user when an associated managed profile has become available.
			String	ACTION_MANAGED_PROFILE_REMOVED
			Broadcast sent to the primary user when an associated managed profile is removed.
			String	ACTION_MANAGED_PROFILE_UNAVAILABLE
			Broadcast sent to the primary user when an associated managed profile has become unavailable.
			String	ACTION_MANAGED_PROFILE_UNLOCKED
			Broadcast sent to the primary user when the credential-encrypted private storage for an associated managed profile is unlocked.
			String	ACTION_MANAGE_NETWORK_USAGE
			Activity Action: Show settings for managing network data usage of a specific application.
			String	ACTION_MANAGE_PACKAGE_STORAGE
			Broadcast Action: Indicates low memory condition notification acknowledged by user and package management should be started.
			String	ACTION_MEDIA_BAD_REMOVAL
			Broadcast Action: External media was removed from SD card slot, but mount point was not unmounted.
			String	ACTION_MEDIA_BUTTON
			Broadcast Action: The "Media Button" was pressed.
			String	ACTION_MEDIA_CHECKING
			Broadcast Action: External media is present, and being disk-checked The path to the mount point for the checking media is contained in the Intent.mData field.
			String	ACTION_MEDIA_EJECT
			Broadcast Action: User has expressed the desire to remove the external storage media.
			String	ACTION_MEDIA_MOUNTED
			Broadcast Action: External media is present and mounted at its mount point.
			String	ACTION_MEDIA_NOFS
			Broadcast Action: External media is present, but is using an incompatible fs (or is blank) The path to the mount point for the checking media is contained in the Intent.mData field.
			String	ACTION_MEDIA_REMOVED
			Broadcast Action: External media has been removed.
			String	ACTION_MEDIA_SCANNER_FINISHED
			Broadcast Action: The media scanner has finished scanning a directory.
			String	ACTION_MEDIA_SCANNER_SCAN_FILE
			Broadcast Action: Request the media scanner to scan a file and add it to the media database.
			String	ACTION_MEDIA_SCANNER_STARTED
			Broadcast Action: The media scanner has started scanning a directory.
			String	ACTION_MEDIA_SHARED
			Broadcast Action: External media is unmounted because it is being shared via USB mass storage.
			String	ACTION_MEDIA_UNMOUNTABLE
			Broadcast Action: External media is present but cannot be mounted.
			String	ACTION_MEDIA_UNMOUNTED
			Broadcast Action: External media is present, but not mounted at its mount point.
			String	ACTION_MY_PACKAGE_REPLACED
			Broadcast Action: A new version of your application has been installed over an existing one.
			String	ACTION_NEW_OUTGOING_CALL
			Broadcast Action: An outgoing call is about to be placed.
			String	ACTION_OPEN_DOCUMENT
			Activity Action: Allow the user to select and return one or more existing documents.
			String	ACTION_OPEN_DOCUMENT_TREE
			Activity Action: Allow the user to pick a directory subtree.
			String	ACTION_PACKAGES_SUSPENDED
			Broadcast Action: Packages have been suspended.
			String	ACTION_PACKAGES_UNSUSPENDED
			Broadcast Action: Packages have been unsuspended.
			String	ACTION_PACKAGE_ADDED
			Broadcast Action: A new application package has been installed on the device.
			String	ACTION_PACKAGE_CHANGED
			Broadcast Action: An existing application package has been changed (for example, a component has been enabled or disabled).
			String	ACTION_PACKAGE_DATA_CLEARED
			Broadcast Action: The user has cleared the data of a package.
			String	ACTION_PACKAGE_FIRST_LAUNCH
			Broadcast Action: Sent to the installer package of an application when that application is first launched (that is the first time it is moved out of the stopped state).
			String	ACTION_PACKAGE_FULLY_REMOVED
			Broadcast Action: An existing application package has been completely removed from the device.
			String	ACTION_PACKAGE_INSTALL
			This constant was deprecated in API level 14. This constant has never been used.
			String	ACTION_PACKAGE_NEEDS_VERIFICATION
			Broadcast Action: Sent to the system package verifier when a package needs to be verified.
			String	ACTION_PACKAGE_REMOVED
			Broadcast Action: An existing application package has been removed from the device.
			String	ACTION_PACKAGE_REPLACED
			Broadcast Action: A new version of an application package has been installed, replacing an existing version that was previously installed.
			String	ACTION_PACKAGE_RESTARTED
			Broadcast Action: The user has restarted a package, and all of its processes have been killed.
			String	ACTION_PACKAGE_VERIFIED
			Broadcast Action: Sent to the system package verifier when a package is verified.
			String	ACTION_PASTE
			Activity Action: Create a new item in the given container, initializing it from the current contents of the clipboard.
			String	ACTION_PICK
			Activity Action: Pick an item from the data, returning what was selected.
			String	ACTION_PICK_ACTIVITY
			Activity Action: Pick an activity given an intent, returning the class selected.
			String	ACTION_POWER_CONNECTED
			Broadcast Action: External power has been connected to the device.
			String	ACTION_POWER_DISCONNECTED
			Broadcast Action: External power has been removed from the device.
			String	ACTION_POWER_USAGE_SUMMARY
			Activity Action: Show power usage information to the user.
			String	ACTION_PROCESS_TEXT
			Activity Action: Process a piece of text.
			String	ACTION_PROVIDER_CHANGED
			Broadcast Action: Some content providers have parts of their namespace where they publish new events or items that the user may be especially interested in.
			String	ACTION_QUICK_CLOCK
			Sent when the user taps on the clock widget in the system's "quick settings" area.
			String	ACTION_QUICK_VIEW
			Activity Action: Quick view the data.
			String	ACTION_REBOOT
			Broadcast Action: Have the device reboot.
			String	ACTION_RUN
			Activity Action: Run the data, whatever that means.
			String	ACTION_SCREEN_OFF
			Broadcast Action: Sent when the device goes to sleep and becomes non-interactive.
			String	ACTION_SCREEN_ON
			Broadcast Action: Sent when the device wakes up and becomes interactive.
			String	ACTION_SEARCH
			Activity Action: Perform a search.
			String	ACTION_SEARCH_LONG_PRESS
			Activity Action: Start action associated with long pressing on the search key.
			String	ACTION_SEND
			Activity Action: Deliver some data to someone else.
			String	ACTION_SENDTO
			Activity Action: Send a message to someone specified by the data.
			String	ACTION_SEND_MULTIPLE
			Activity Action: Deliver multiple data to someone else.
			String	ACTION_SET_WALLPAPER
			Activity Action: Show settings for choosing wallpaper.
			String	ACTION_SHOW_APP_INFO
			Activity Action: Launch an activity showing the app information.
			String	ACTION_SHUTDOWN
			Broadcast Action: Device is shutting down.
			String	ACTION_SYNC
			Activity Action: Perform a data synchronization.
			String	ACTION_SYSTEM_TUTORIAL
			Activity Action: Start the platform-defined tutorial
			
			Input: getStringExtra(SearchManager.QUERY) is the text to search for.
			String	ACTION_TIMEZONE_CHANGED
			Broadcast Action: The timezone has changed.
			String	ACTION_TIME_CHANGED
			Broadcast Action: The time was set.
			String	ACTION_TIME_TICK
			Broadcast Action: The current time has changed.
			String	ACTION_UID_REMOVED
			Broadcast Action: A user ID has been removed from the system.
			String	ACTION_UMS_CONNECTED
			This constant was deprecated in API level 14. replaced by android.os.storage.StorageEventListener
			String	ACTION_UMS_DISCONNECTED
			This constant was deprecated in API level 14. replaced by android.os.storage.StorageEventListener
			String	ACTION_UNINSTALL_PACKAGE
			Activity Action: Launch application uninstaller.
			String	ACTION_USER_BACKGROUND
			Sent when a user switch is happening, causing the process's user to be sent to the background.
			String	ACTION_USER_FOREGROUND
			Sent when a user switch is happening, causing the process's user to be brought to the foreground.
			String	ACTION_USER_INITIALIZE
			Sent the first time a user is starting, to allow system apps to perform one time initialization.
			String	ACTION_USER_PRESENT
			Broadcast Action: Sent when the user is present after device wakes up (e.g when the keyguard is gone).
			String	ACTION_USER_UNLOCKED
			Broadcast Action: Sent when the credential-encrypted private storage has become unlocked for the target user.
			String	ACTION_VIEW
			Activity Action: Display the data to the user.
			String	ACTION_VOICE_COMMAND
			Activity Action: Start Voice Command.
			String	ACTION_WALLPAPER_CHANGED
			This constant was deprecated in API level 16. Modern applications should use WindowManager.LayoutParams.FLAG_SHOW_WALLPAPER to have the wallpaper shown behind their UI, rather than watching for this broadcast and rendering the wallpaper on their own.
			String	ACTION_WEB_SEARCH
			Activity Action: Perform a web search.
			String	CATEGORY_ALTERNATIVE
			Set if the activity should be considered as an alternative action to the data the user is currently viewing.
			String	CATEGORY_APP_BROWSER
			Used with ACTION_MAIN to launch the browser application.
			String	CATEGORY_APP_CALCULATOR
			Used with ACTION_MAIN to launch the calculator application.
			String	CATEGORY_APP_CALENDAR
			Used with ACTION_MAIN to launch the calendar application.
			String	CATEGORY_APP_CONTACTS
			Used with ACTION_MAIN to launch the contacts application.
			String	CATEGORY_APP_EMAIL
			Used with ACTION_MAIN to launch the email application.
			String	CATEGORY_APP_GALLERY
			Used with ACTION_MAIN to launch the gallery application.
			String	CATEGORY_APP_MAPS
			Used with ACTION_MAIN to launch the maps application.
			String	CATEGORY_APP_MARKET
			This activity allows the user to browse and download new applications.
			String	CATEGORY_APP_MESSAGING
			Used with ACTION_MAIN to launch the messaging application.
			String	CATEGORY_APP_MUSIC
			Used with ACTION_MAIN to launch the music application.
			String	CATEGORY_BROWSABLE
			Activities that can be safely invoked from a browser must support this category.
			String	CATEGORY_CAR_DOCK
			An activity to run when device is inserted into a car dock.
			String	CATEGORY_CAR_MODE
			Used to indicate that the activity can be used in a car environment.
			String	CATEGORY_DEFAULT
			Set if the activity should be an option for the default action (center press) to perform on a piece of data.
			String	CATEGORY_DESK_DOCK
			An activity to run when device is inserted into a car dock.
			String	CATEGORY_DEVELOPMENT_PREFERENCE
			This activity is a development preference panel.
			String	CATEGORY_EMBED
			Capable of running inside a parent activity container.
			String	CATEGORY_FRAMEWORK_INSTRUMENTATION_TEST
			To be used as code under test for framework instrumentation tests.
			String	CATEGORY_HE_DESK_DOCK
			An activity to run when device is inserted into a digital (high end) dock.
			String	CATEGORY_HOME
			This is the home activity, that is the first activity that is displayed when the device boots.
			String	CATEGORY_INFO
			Provides information about the package it is in; typically used if a package does not contain a CATEGORY_LAUNCHER to provide a front-door to the user without having to be shown in the all apps list.
			String	CATEGORY_LAUNCHER
			Should be displayed in the top-level launcher.
			String	CATEGORY_LEANBACK_LAUNCHER
			Indicates an activity optimized for Leanback mode, and that should be displayed in the Leanback launcher.
			String	CATEGORY_LE_DESK_DOCK
			An activity to run when device is inserted into a analog (low end) dock.
			String	CATEGORY_MONKEY
			This activity may be exercised by the monkey or other automated test tools.
			String	CATEGORY_OPENABLE
			Used to indicate that an intent only wants URIs that can be opened with openFileDescriptor(Uri, String).
			String	CATEGORY_PREFERENCE
			This activity is a preference panel.
			String	CATEGORY_SAMPLE_CODE
			To be used as a sample code example (not part of the normal user experience).
			String	CATEGORY_SELECTED_ALTERNATIVE
			Set if the activity should be considered as an alternative selection action to the data the user has currently selected.
			String	CATEGORY_TAB
			Intended to be used as a tab inside of a containing TabActivity.
			String	CATEGORY_TEST
			To be used as a test (not part of the normal user experience).
			String	CATEGORY_TYPED_OPENABLE
			Used to indicate that an intent filter can accept files which are not necessarily openable by openFileDescriptor(Uri, String), but at least streamable via openTypedAssetFileDescriptor(Uri, String, Bundle) using one of the stream types exposed via getStreamTypes(Uri, String).
			String	CATEGORY_UNIT_TEST
			To be used as a unit test (run through the Test Harness).
			String	CATEGORY_VOICE
			Categories for activities that can participate in voice interaction.
			String	CATEGORY_VR_HOME
			An activity to use for the launcher when the device is placed in a VR Headset viewer.
			String	EXTRA_ALARM_COUNT
			Used as an int extra field in AlarmManager intents to tell the application being invoked how many pending alarms are being delievered with the intent.
			String	EXTRA_ALLOW_MULTIPLE
			Extra used to indicate that an intent can allow the user to select and return multiple items.
			String	EXTRA_ALLOW_REPLACE
			This constant was deprecated in API level 16. As of JELLY_BEAN, Android will no longer show an interstitial message about updating existing applications so this is no longer needed.
			String	EXTRA_ALTERNATE_INTENTS
			An Intent[] describing additional, alternate choices you would like shown with ACTION_CHOOSER.
			String	EXTRA_ASSIST_CONTEXT
			An optional field on ACTION_ASSIST and containing additional contextual information supplied by the current foreground app at the time of the assist request.
			String	EXTRA_ASSIST_INPUT_DEVICE_ID
			An optional field on ACTION_ASSIST containing the InputDevice id that was used to invoke the assist.
			String	EXTRA_ASSIST_INPUT_HINT_KEYBOARD
			An optional field on ACTION_ASSIST suggesting that the user will likely use a keyboard as the primary input device for assistance.
			String	EXTRA_ASSIST_PACKAGE
			An optional field on ACTION_ASSIST containing the name of the current foreground application package at the time the assist was invoked.
			String	EXTRA_ASSIST_UID
			An optional field on ACTION_ASSIST containing the uid of the current foreground application package at the time the assist was invoked.
			String	EXTRA_BCC
			A String[] holding e-mail addresses that should be blind carbon copied.
			String	EXTRA_BUG_REPORT
			Used as a parcelable extra field in ACTION_APP_ERROR, containing the bug report.
			String	EXTRA_CC
			A String[] holding e-mail addresses that should be carbon copied.
			String	EXTRA_CHANGED_COMPONENT_NAME
			This constant was deprecated in API level 7. See EXTRA_CHANGED_COMPONENT_NAME_LIST; this field will contain only the first name in the list.
			String	EXTRA_CHANGED_COMPONENT_NAME_LIST
			This field is part of ACTION_PACKAGE_CHANGED, and contains a string array of all of the components that have changed.
			String	EXTRA_CHANGED_PACKAGE_LIST
			This field is part of ACTION_EXTERNAL_APPLICATIONS_AVAILABLE, ACTION_EXTERNAL_APPLICATIONS_UNAVAILABLE, ACTION_PACKAGES_SUSPENDED, ACTION_PACKAGES_UNSUSPENDED and contains a string array of all of the components that have changed.
			String	EXTRA_CHANGED_UID_LIST
			This field is part of ACTION_EXTERNAL_APPLICATIONS_AVAILABLE, ACTION_EXTERNAL_APPLICATIONS_UNAVAILABLE and contains an integer array of uids of all of the components that have changed.
			String	EXTRA_CHOOSER_REFINEMENT_INTENT_SENDER
			An IntentSender for an Activity that will be invoked when the user makes a selection from the chooser activity presented by ACTION_CHOOSER.
			String	EXTRA_CHOOSER_TARGETS
			A ChooserTarget[] for ACTION_CHOOSER describing additional high-priority deep-link targets for the chooser to present to the user.
			String	EXTRA_CHOSEN_COMPONENT
			The ComponentName chosen by the user to complete an action.
			String	EXTRA_CHOSEN_COMPONENT_INTENT_SENDER
			An IntentSender that will be notified if a user successfully chooses a target component to handle an action in an ACTION_CHOOSER activity.
			String	EXTRA_CONTENT_ANNOTATIONS
			An ArrayList of String annotations describing content for ACTION_CHOOSER.
			String	EXTRA_DATA_REMOVED
			Used as a boolean extra field in ACTION_PACKAGE_REMOVED intents to indicate whether this represents a full uninstall (removing both the code and its data) or a partial uninstall (leaving its data, implying that this is an update).
			String	EXTRA_DOCK_STATE
			Used as an int extra field in ACTION_DOCK_EVENT intents to request the dock state.
			int	EXTRA_DOCK_STATE_CAR
			Used as an int value for EXTRA_DOCK_STATE to represent that the phone is in a car dock.
			int	EXTRA_DOCK_STATE_DESK
			Used as an int value for EXTRA_DOCK_STATE to represent that the phone is in a desk dock.
			int	EXTRA_DOCK_STATE_HE_DESK
			Used as an int value for EXTRA_DOCK_STATE to represent that the phone is in a digital (high end) dock.
			int	EXTRA_DOCK_STATE_LE_DESK
			Used as an int value for EXTRA_DOCK_STATE to represent that the phone is in a analog (low end) dock.
			int	EXTRA_DOCK_STATE_UNDOCKED
			Used as an int value for EXTRA_DOCK_STATE to represent that the phone is not in any dock.
			String	EXTRA_DONT_KILL_APP
			Used as a boolean extra field in ACTION_PACKAGE_REMOVED or ACTION_PACKAGE_CHANGED intents to override the default action of restarting the application.
			String	EXTRA_EMAIL
			A String[] holding e-mail addresses that should be delivered to.
			String	EXTRA_EXCLUDE_COMPONENTS
			A ComponentName[] describing components that should be filtered out and omitted from a list of components presented to the user.
			String	EXTRA_FROM_STORAGE
			Extra that can be included on activity intents coming from the storage UI when it launches sub-activities to manage various types of storage.
			String	EXTRA_HTML_TEXT
			A constant String that is associated with the Intent, used with ACTION_SEND to supply an alternative to EXTRA_TEXT as HTML formatted text.
			String	EXTRA_INDEX
			Optional index with semantics depending on the intent action.
			String	EXTRA_INITIAL_INTENTS
			A Parcelable[] of Intent or LabeledIntent objects as set with putExtra(String, Parcelable[]) of additional activities to place a the front of the list of choices, when shown to the user with a ACTION_CHOOSER.
			String	EXTRA_INSTALLER_PACKAGE_NAME
			Used as a string extra field with ACTION_INSTALL_PACKAGE to install a package.
			String	EXTRA_INTENT
			An Intent describing the choices you would like shown with ACTION_PICK_ACTIVITY or ACTION_CHOOSER.
			String	EXTRA_KEY_EVENT
			A KeyEvent object containing the event that triggered the creation of the Intent it is in.
			String	EXTRA_LOCAL_ONLY
			Extra used to indicate that an intent should only return data that is on the local device.
			String	EXTRA_MIME_TYPES
			Extra used to communicate a set of acceptable MIME types.
			String	EXTRA_NOT_UNKNOWN_SOURCE
			Used as a boolean extra field with ACTION_INSTALL_PACKAGE to install a package.
			String	EXTRA_ORIGINATING_URI
			Used as a URI extra field with ACTION_INSTALL_PACKAGE and ACTION_VIEW to indicate the URI from which the local APK in the Intent data field originated from.
			String	EXTRA_PACKAGE_NAME
			Intent extra: An app package name.
			String	EXTRA_PHONE_NUMBER
			A String holding the phone number originally entered in ACTION_NEW_OUTGOING_CALL, or the actual number to call in a ACTION_CALL.
			String	EXTRA_PROCESS_TEXT
			The name of the extra used to define the text to be processed, as a CharSequence.
			String	EXTRA_PROCESS_TEXT_READONLY
			The name of the boolean extra used to define if the processed text will be used as read-only.
			String	EXTRA_QUICK_VIEW_FEATURES
			An optional extra of String[] indicating which quick view features should be made available to the user in the quick view UI while handing a ACTION_QUICK_VIEW intent.
			String	EXTRA_QUIET_MODE
			Optional boolean extra indicating whether quiet mode has been switched on or off.
			String	EXTRA_REFERRER
			This extra can be used with any Intent used to launch an activity, supplying information about who is launching that activity.
			String	EXTRA_REFERRER_NAME
			Alternate version of EXTRA_REFERRER that supplies the URI as a String rather than a Uri object.
			String	EXTRA_REMOTE_INTENT_TOKEN
			Used in the extra field in the remote intent.
			String	EXTRA_REPLACEMENT_EXTRAS
			A Bundle forming a mapping of potential target package names to different extras Bundles to add to the default intent extras in EXTRA_INTENT when used with ACTION_CHOOSER.
			String	EXTRA_REPLACING
			Used as a boolean extra field in ACTION_PACKAGE_REMOVED intents to indicate that this is a replacement of the package, so this broadcast will immediately be followed by an add broadcast for a different version of the same package.
			String	EXTRA_RESTRICTIONS_BUNDLE
			Extra sent in the intent to the BroadcastReceiver that handles ACTION_GET_RESTRICTION_ENTRIES.
			String	EXTRA_RESTRICTIONS_INTENT
			Extra used in the response from a BroadcastReceiver that handles ACTION_GET_RESTRICTION_ENTRIES.
			String	EXTRA_RESTRICTIONS_LIST
			Extra used in the response from a BroadcastReceiver that handles ACTION_GET_RESTRICTION_ENTRIES.
			String	EXTRA_RESULT_RECEIVER
			A ResultReceiver used to return data back to the sender.
			String	EXTRA_RETURN_RESULT
			Used as a boolean extra field with ACTION_INSTALL_PACKAGE or ACTION_UNINSTALL_PACKAGE.
			String	EXTRA_SHORTCUT_ICON
			This constant was deprecated in API level O. Replaced with createShortcutResultIntent(ShortcutInfo)
			String	EXTRA_SHORTCUT_ICON_RESOURCE
			This constant was deprecated in API level O. Replaced with createShortcutResultIntent(ShortcutInfo)
			String	EXTRA_SHORTCUT_INTENT
			This constant was deprecated in API level O. Replaced with createShortcutResultIntent(ShortcutInfo)
			String	EXTRA_SHORTCUT_NAME
			This constant was deprecated in API level O. Replaced with createShortcutResultIntent(ShortcutInfo)
			String	EXTRA_SHUTDOWN_USERSPACE_ONLY
			Optional extra for ACTION_SHUTDOWN that allows the sender to qualify that this shutdown is only for the user space of the system, not a complete shutdown.
			String	EXTRA_STREAM
			A content: URI holding a stream of data associated with the Intent, used with ACTION_SEND to supply the data being sent.
			String	EXTRA_SUBJECT
			A constant string holding the desired subject line of a message.
			String	EXTRA_SUBSCRIPTION_INDEX
			Integer extra used with ACTION_DEFAULT_SUBSCRIPTION_CHANGED and ACTION_DEFAULT_SMS_SUBSCRIPTION_CHANGED to indicate the subscription which has changed.
			String	EXTRA_TEMPLATE
			The initial data to place in a newly created record.
			String	EXTRA_TEXT
			A constant CharSequence that is associated with the Intent, used with ACTION_SEND to supply the literal data to be sent.
			String	EXTRA_TITLE
			A CharSequence dialog title to provide to the user when used with a ACTION_CHOOSER.
			String	EXTRA_UID
			Used as an int extra field in ACTION_UID_REMOVED intents to supply the uid the package had been assigned.
			String	EXTRA_USER
			The UserHandle carried with broadcasts intents related to addition and removal of managed profiles - ACTION_MANAGED_PROFILE_ADDED and ACTION_MANAGED_PROFILE_REMOVED.
			int	FILL_IN_ACTION
			Use with fillIn(Intent, int) to allow the current action value to be overwritten, even if it is already set.
			int	FILL_IN_CATEGORIES
			Use with fillIn(Intent, int) to allow the current categories to be overwritten, even if they are already set.
			int	FILL_IN_CLIP_DATA
			Use with fillIn(Intent, int) to allow the current ClipData to be overwritten, even if it is already set.
			int	FILL_IN_COMPONENT
			Use with fillIn(Intent, int) to allow the current component value to be overwritten, even if it is already set.
			int	FILL_IN_DATA
			Use with fillIn(Intent, int) to allow the current data or type value overwritten, even if it is already set.
			int	FILL_IN_PACKAGE
			Use with fillIn(Intent, int) to allow the current package value to be overwritten, even if it is already set.
			int	FILL_IN_SELECTOR
			Use with fillIn(Intent, int) to allow the current selector to be overwritten, even if it is already set.
			int	FILL_IN_SOURCE_BOUNDS
			Use with fillIn(Intent, int) to allow the current bounds rectangle to be overwritten, even if it is already set.
			int	FLAG_ACTIVITY_BROUGHT_TO_FRONT
			This flag is not normally set by application code, but set for you by the system as described in the launchMode documentation for the singleTask mode.
			int	FLAG_ACTIVITY_CLEAR_TASK
			If set in an Intent passed to Context.startActivity(), this flag will cause any existing task that would be associated with the activity to be cleared before the activity is started.
			int	FLAG_ACTIVITY_CLEAR_TOP
			If set, and the activity being launched is already running in the current task, then instead of launching a new instance of that activity, all of the other activities on top of it will be closed and this Intent will be delivered to the (now on top) old activity as a new Intent.
			int	FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET
			This constant was deprecated in API level 21. As of API 21 this performs identically to FLAG_ACTIVITY_NEW_DOCUMENT which should be used instead of this.
			int	FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS
			If set, the new activity is not kept in the list of recently launched activities.
			int	FLAG_ACTIVITY_FORWARD_RESULT
			If set and this intent is being used to launch a new activity from an existing one, then the reply target of the existing activity will be transfered to the new activity.
			int	FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY
			This flag is not normally set by application code, but set for you by the system if this activity is being launched from history (longpress home key).
			int	FLAG_ACTIVITY_LAUNCH_ADJACENT
			This flag is only used in split-screen multi-window mode.
			int	FLAG_ACTIVITY_MULTIPLE_TASK
			This flag is used to create a new task and launch an activity into it.
			int	FLAG_ACTIVITY_NEW_DOCUMENT
			This flag is used to open a document into a new task rooted at the activity launched by this Intent.
			int	FLAG_ACTIVITY_NEW_TASK
			If set, this activity will become the start of a new task on this history stack.
			int	FLAG_ACTIVITY_NO_ANIMATION
			If set in an Intent passed to Context.startActivity(), this flag will prevent the system from applying an activity transition animation to go to the next activity state.
			int	FLAG_ACTIVITY_NO_HISTORY
			If set, the new activity is not kept in the history stack.
			int	FLAG_ACTIVITY_NO_USER_ACTION
			If set, this flag will prevent the normal onUserLeaveHint() callback from occurring on the current frontmost activity before it is paused as the newly-started activity is brought to the front.
			int	FLAG_ACTIVITY_PREVIOUS_IS_TOP
			If set and this intent is being used to launch a new activity from an existing one, the current activity will not be counted as the top activity for deciding whether the new intent should be delivered to the top instead of starting a new one.
			int	FLAG_ACTIVITY_REORDER_TO_FRONT
			If set in an Intent passed to Context.startActivity(), this flag will cause the launched activity to be brought to the front of its task's history stack if it is already running.
			int	FLAG_ACTIVITY_RESET_TASK_IF_NEEDED
			If set, and this activity is either being started in a new task or bringing to the top an existing task, then it will be launched as the front door of the task.
			int	FLAG_ACTIVITY_RETAIN_IN_RECENTS
			By default a document created by FLAG_ACTIVITY_NEW_DOCUMENT will have its entry in recent tasks removed when the user closes it (with back or however else it may finish()).
			int	FLAG_ACTIVITY_SINGLE_TOP
			If set, the activity will not be launched if it is already running at the top of the history stack.
			int	FLAG_ACTIVITY_TASK_ON_HOME
			If set in an Intent passed to Context.startActivity(), this flag will cause a newly launching task to be placed on top of the current home activity task (if there is one).
			int	FLAG_DEBUG_LOG_RESOLUTION
			A flag you can enable for debugging: when set, log messages will be printed during the resolution of this intent to show you what has been found to create the final resolved list.
			int	FLAG_EXCLUDE_STOPPED_PACKAGES
			If set, this intent will not match any components in packages that are currently stopped.
			int	FLAG_FROM_BACKGROUND
			Can be set by the caller to indicate that this Intent is coming from a background operation, not from direct user interaction.
			int	FLAG_GRANT_PERSISTABLE_URI_PERMISSION
			When combined with FLAG_GRANT_READ_URI_PERMISSION and/or FLAG_GRANT_WRITE_URI_PERMISSION, the URI permission grant can be persisted across device reboots until explicitly revoked with revokeUriPermission(Uri, int).
			int	FLAG_GRANT_PREFIX_URI_PERMISSION
			When combined with FLAG_GRANT_READ_URI_PERMISSION and/or FLAG_GRANT_WRITE_URI_PERMISSION, the URI permission grant applies to any URI that is a prefix match against the original granted URI.
			int	FLAG_GRANT_READ_URI_PERMISSION
			If set, the recipient of this Intent will be granted permission to perform read operations on the URI in the Intent's data and any URIs specified in its ClipData.
			int	FLAG_GRANT_WRITE_URI_PERMISSION
			If set, the recipient of this Intent will be granted permission to perform write operations on the URI in the Intent's data and any URIs specified in its ClipData.
			int	FLAG_INCLUDE_STOPPED_PACKAGES
			If set, this intent will always match any components in packages that are currently stopped.
			int	FLAG_RECEIVER_FOREGROUND
			If set, when sending a broadcast the recipient is allowed to run at foreground priority, with a shorter timeout interval.
			int	FLAG_RECEIVER_NO_ABORT
			If this is an ordered broadcast, don't allow receivers to abort the broadcast.
			int	FLAG_RECEIVER_REGISTERED_ONLY
			If set, when sending a broadcast only registered receivers will be called -- no BroadcastReceiver components will be launched.
			int	FLAG_RECEIVER_REPLACE_PENDING
			If set, when sending a broadcast the new broadcast will replace any existing pending broadcast that matches it.
			int	FLAG_RECEIVER_VISIBLE_TO_INSTANT_APPS
			If set, the broadcast will be visible to receivers in Instant Apps.
			String	METADATA_DOCK_HOME
			Boolean that can be supplied as meta-data with a dock activity, to indicate that the dock should take over the home key when it is active.
			int	URI_ALLOW_UNSAFE
			Flag for use with toUri(int) and parseUri(String, int): allow parsing of unsafe information.
			int	URI_ANDROID_APP_SCHEME
			Flag for use with toUri(int) and parseUri(String, int): the URI string always has the "android-app:" scheme.
			int	URI_INTENT_SCHEME
			Flag for use with toUri(int) and parseUri(String, int): the URI string always has the "intent:" scheme.