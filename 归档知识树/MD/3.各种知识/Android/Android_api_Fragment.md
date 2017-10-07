#Fragment

java.lang.Object  
   ↳	android.app.Fragment  
直接子类：

		BrandedFragment
		DialogFragment
		GuidedStepFragment
		HeadersFragment
		LeanbackPreferenceDialogFragment
		LeanbackSettingsFragment
		ListFragment
		OnboardingFragment
		PlaybackFragment
		PreferenceFragment
		RowsFragment
		SearchFragment
		WebViewFragment

间接子类：

		BaseFragment
		BaseLeanbackPreferenceFragment
		BrowseFragment
		DetailsFragment
		EditTextPreferenceDialogFragment
		ErrorFragment
		LeanbackListPreferenceDialogFragment
		LeanbackPreferenceFragment
		ListPreferenceDialogFragment
		MultiSelectListPreferenceDialogFragment
		PlaybackOverlayFragment
		PreferenceDialogFragment
		VerticalGridFragment
		VideoFragment
 Activity.getFragmentManager() Fragment.getFragmentManager()

Topics covered here:

	Older Platforms
	Lifecycle
	Layout
	Back Stack
#
	The core series of lifecycle methods that are called to bring a fragment up to resumed state (interacting with the user) are:
	
	onAttach(Activity) called once the fragment is associated with its activity.
	onCreate(Bundle) called to do initial creation of the fragment.
	onCreateView(LayoutInflater, ViewGroup, Bundle) creates and returns the view hierarchy associated with the fragment.
	onActivityCreated(Bundle) tells the fragment that its activity has completed its own Activity.onCreate().
	onViewStateRestored(Bundle) tells the fragment that all of the saved state of its view hierarchy has been restored.
	onStart() makes the fragment visible to the user (based on its containing activity being started).
	onResume() makes the fragment begin interacting with the user (based on its containing activity being resumed).
	As a fragment is no longer being used, it goes through a reverse series of callbacks:
	
	onPause() fragment is no longer interacting with the user either because its activity is being paused or a fragment operation is modifying it in the activity.
	onStop() fragment is no longer visible to the user either because its activity is being stopped or a fragment operation is modifying it in the activity.
	onDestroyView() allows the fragment to clean up resources associated with its View.
	onDestroy() called to do final cleanup of the fragment's state.
	onDetach() called immediately prior to the fragment no longer being associated with its activity.



#Nested classes

	class	Fragment.InstantiationException
	Thrown by instantiate(Context, String, Bundle) when there is an instantiation failure. 
	class	Fragment.SavedState
	State information that has been retrieved from a fragment instance through FragmentManager.saveFragmentInstanceState.

#XML attributes
	android:fragmentAllowEnterTransitionOverlap	Sets whether the enter and exit transitions should overlap when transitioning forward. 
	android:fragmentAllowReturnTransitionOverlap	Sets whether the enter and exit transitions should overlap when transitioning because of popping the back stack. 
	android:fragmentEnterTransition	The Transition that will be used to move Views into the initial scene. 
	android:fragmentExitTransition	The Transition that will be used to move Views out of the scene when the fragment is removed, hidden, or detached when not popping the back stack. 
	android:fragmentReenterTransition	The Transition that will be used to move Views in to the scene when returning due to popping a back stack. 
	android:fragmentSharedElementEnterTransition	The Transition that will be used for shared elements transferred into the content Scene. 
	android:fragmentSharedElementReturnTransition	The Transition that will be used for shared elements transferred back during a pop of the back stack.  

#Public methods

	void	dump(String prefix, FileDescriptor fd, PrintWriter writer, String[] args)
	Print the Fragments's state into the given stream.
	final boolean	equals(Object o)
	Subclasses can not override equals().
	final Activity	getActivity()
	Return the Activity this fragment is currently associated with.
	boolean	getAllowEnterTransitionOverlap()
	Returns whether the the exit transition and enter transition overlap or not.
	boolean	getAllowReturnTransitionOverlap()
	Returns whether the the return transition and reenter transition overlap or not.
	final Bundle	getArguments()
	Return the arguments supplied to setArguments(Bundle), if any.
	final FragmentManager	getChildFragmentManager()
	Return a private FragmentManager for placing and managing Fragments inside of this Fragment.
	Context	getContext()
	Return the Context this fragment is currently associated with.
	Transition	getEnterTransition()
	Returns the Transition that will be used to move Views into the initial scene.
	Transition	getExitTransition()
	Returns the Transition that will be used to move Views out of the scene when the fragment is removed, hidden, or detached when not popping the back stack.
	final FragmentManager	getFragmentManager()
	Return the FragmentManager for interacting with fragments associated with this fragment's activity.
	final Object	getHost()
	Return the host object of this fragment.
	final int	getId()
	Return the identifier this fragment is known by.
	final LayoutInflater	getLayoutInflater()
	Returns the cached LayoutInflater used to inflate Views of this Fragment.
	LoaderManager	getLoaderManager()
	Return the LoaderManager for this fragment, creating it if needed.
	final Fragment	getParentFragment()
	Returns the parent Fragment containing this Fragment.
	Transition	getReenterTransition()
	Returns the Transition that will be used to move Views in to the scene when returning due to popping a back stack.
	final Resources	getResources()
	Return getActivity().getResources().
	final boolean	getRetainInstance()
	Transition	getReturnTransition()
	Returns the Transition that will be used to move Views out of the scene when the Fragment is preparing to be removed, hidden, or detached because of popping the back stack.
	Transition	getSharedElementEnterTransition()
	Returns the Transition that will be used for shared elements transferred into the content Scene.
	Transition	getSharedElementReturnTransition()
	Return the Transition that will be used for shared elements transferred back during a pop of the back stack.
	final String	getString(int resId, Object... formatArgs)
	Return a localized formatted string from the application's package's default string table, substituting the format arguments as defined in Formatter and format(String, Object...).
	final String	getString(int resId)
	Return a localized string from the application's package's default string table.
	final String	getTag()
	Get the tag name of the fragment, if specified.
	final Fragment	getTargetFragment()
	Return the target fragment set by setTargetFragment(Fragment, int).
	final int	getTargetRequestCode()
	Return the target request code set by setTargetFragment(Fragment, int).
	final CharSequence	getText(int resId)
	Return a localized, styled CharSequence from the application's package's default string table.
	boolean	getUserVisibleHint()
	View	getView()
	Get the root view for the fragment's layout (the one returned by onCreateView(LayoutInflater, ViewGroup, Bundle)), if provided.
	final int	hashCode()
	Subclasses can not override hashCode().
	static Fragment	instantiate(Context context, String fname)
	Like instantiate(Context, String, Bundle) but with a null argument Bundle.
	static Fragment	instantiate(Context context, String fname, Bundle args)
	Create a new instance of a Fragment with the given class name.
	final boolean	isAdded()
	Return true if the fragment is currently added to its activity.
	final boolean	isDetached()
	Return true if the fragment has been explicitly detached from the UI.
	final boolean	isHidden()
	Return true if the fragment has been hidden.
	final boolean	isInLayout()
	Return true if the layout is included as part of an activity view hierarchy via the <fragment> tag.
	final boolean	isRemoving()
	Return true if this fragment is currently being removed from its activity.
	final boolean	isResumed()
	Return true if the fragment is in the resumed state.
	final boolean	isStateSaved()
	Returns true if this fragment is added and its state has already been saved by its host.
	final boolean	isVisible()
	Return true if the fragment is currently visible to the user.
	void	onActivityCreated(Bundle savedInstanceState)
	Called when the fragment's activity has been created and this fragment's view hierarchy instantiated.
	void	onActivityResult(int requestCode, int resultCode, Intent data)
	Receive the result from a previous call to startActivityForResult(Intent, int).
	void	onAttach(Activity activity)
	This method was deprecated in API level 23. Use onAttach(Context) instead.
	void	onAttach(Context context)
	Called when a fragment is first attached to its context.
	void	onAttachFragment(Fragment childFragment)
	Called when a fragment is attached as a child of this fragment.
	void	onConfigurationChanged(Configuration newConfig)
	Called by the system when the device configuration changes while your component is running.
	boolean	onContextItemSelected(MenuItem item)
	This hook is called whenever an item in a context menu is selected.
	void	onCreate(Bundle savedInstanceState)
	Called to do initial creation of a fragment.
	Animator	onCreateAnimator(int transit, boolean enter, int nextAnim)
	Called when a fragment loads an animation.
	void	onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo)
	Called when a context menu for the view is about to be shown.
	void	onCreateOptionsMenu(Menu menu, MenuInflater inflater)
	Initialize the contents of the Activity's standard options menu.
	View	onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState)
	Called to have the fragment instantiate its user interface view.
	void	onDestroy()
	Called when the fragment is no longer in use.
	void	onDestroyOptionsMenu()
	Called when this fragment's option menu items are no longer being included in the overall options menu.
	void	onDestroyView()
	Called when the view previously created by onCreateView(LayoutInflater, ViewGroup, Bundle) has been detached from the fragment.
	void	onDetach()
	Called when the fragment is no longer attached to its activity.
	LayoutInflater	onGetLayoutInflater(Bundle savedInstanceState)
	Returns the LayoutInflater used to inflate Views of this Fragment.
	void	onHiddenChanged(boolean hidden)
	Called when the hidden state (as returned by isHidden() of the fragment has changed.
	void	onInflate(AttributeSet attrs, Bundle savedInstanceState)
	This method was deprecated in API level 12. Use onInflate(Context, AttributeSet, Bundle) instead.
	void	onInflate(Activity activity, AttributeSet attrs, Bundle savedInstanceState)
	This method was deprecated in API level 23. Use onInflate(Context, AttributeSet, Bundle) instead.
	void	onInflate(Context context, AttributeSet attrs, Bundle savedInstanceState)
	Called when a fragment is being created as part of a view layout inflation, typically from setting the content view of an activity.
	void	onLowMemory()
	This is called when the overall system is running low on memory, and actively running processes should trim their memory usage.
	void	onMultiWindowModeChanged(boolean isInMultiWindowMode)
	This method was deprecated in API level O. Use onMultiWindowModeChanged(boolean, Configuration) instead.
	void	onMultiWindowModeChanged(boolean isInMultiWindowMode, Configuration newConfig)
	Called when the Fragment's activity changes from fullscreen mode to multi-window mode and visa-versa.
	boolean	onOptionsItemSelected(MenuItem item)
	This hook is called whenever an item in your options menu is selected.
	void	onOptionsMenuClosed(Menu menu)
	This hook is called whenever the options menu is being closed (either by the user canceling the menu with the back/menu button, or when an item is selected).
	void	onPause()
	Called when the Fragment is no longer resumed.
	void	onPictureInPictureModeChanged(boolean isInPictureInPictureMode, Configuration newConfig)
	Called by the system when the activity changes to and from picture-in-picture mode.
	void	onPictureInPictureModeChanged(boolean isInPictureInPictureMode)
	This method was deprecated in API level O. Use onPictureInPictureModeChanged(boolean, Configuration) instead.
	void	onPrepareOptionsMenu(Menu menu)
	Prepare the Screen's standard options menu to be displayed.
	void	onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults)
	Callback for the result from requesting permissions.
	void	onResume()
	Called when the fragment is visible to the user and actively running.
	void	onSaveInstanceState(Bundle outState)
	Called to ask the fragment to save its current dynamic state, so it can later be reconstructed in a new instance of its process is restarted.
	void	onStart()
	Called when the Fragment is visible to the user.
	void	onStop()
	Called when the Fragment is no longer started.
	void	onTrimMemory(int level)
	Called when the operating system has determined that it is a good time for a process to trim unneeded memory from its process.
	void	onViewCreated(View view, Bundle savedInstanceState)
	Called immediately after onCreateView(LayoutInflater, ViewGroup, Bundle) has returned, but before any saved state has been restored in to the view.
	void	onViewStateRestored(Bundle savedInstanceState)
	Called when all saved state has been restored into the view hierarchy of the fragment.
	void	postponeEnterTransition()
	Postpone the entering Fragment transition until startPostponedEnterTransition() or executePendingTransactions() has been called.
	void	registerForContextMenu(View view)
	Registers a context menu to be shown for the given view (multiple views can show the context menu).
	final void	requestPermissions(String[] permissions, int requestCode)
	Requests permissions to be granted to this application.
	void	setAllowEnterTransitionOverlap(boolean allow)
	Sets whether the the exit transition and enter transition overlap or not.
	void	setAllowReturnTransitionOverlap(boolean allow)
	Sets whether the the return transition and reenter transition overlap or not.
	void	setArguments(Bundle args)
	Supply the construction arguments for this fragment.
	void	setEnterSharedElementCallback(SharedElementCallback callback)
	When custom transitions are used with Fragments, the enter transition callback is called when this Fragment is attached or detached when not popping the back stack.
	void	setEnterTransition(Transition transition)
	Sets the Transition that will be used to move Views into the initial scene.
	void	setExitSharedElementCallback(SharedElementCallback callback)
	When custom transitions are used with Fragments, the exit transition callback is called when this Fragment is attached or detached when popping the back stack.
	void	setExitTransition(Transition transition)
	Sets the Transition that will be used to move Views out of the scene when the fragment is removed, hidden, or detached when not popping the back stack.
	void	setHasOptionsMenu(boolean hasMenu)
	Report that this fragment would like to participate in populating the options menu by receiving a call to onCreateOptionsMenu(Menu, MenuInflater) and related methods.
	void	setInitialSavedState(Fragment.SavedState state)
	Set the initial saved state that this Fragment should restore itself from when first being constructed, as returned by FragmentManager.saveFragmentInstanceState.
	void	setMenuVisibility(boolean menuVisible)
	Set a hint for whether this fragment's menu should be visible.
	void	setReenterTransition(Transition transition)
	Sets the Transition that will be used to move Views in to the scene when returning due to popping a back stack.
	void	setRetainInstance(boolean retain)
	Control whether a fragment instance is retained across Activity re-creation (such as from a configuration change).
	void	setReturnTransition(Transition transition)
	Sets the Transition that will be used to move Views out of the scene when the Fragment is preparing to be removed, hidden, or detached because of popping the back stack.
	void	setSharedElementEnterTransition(Transition transition)
	Sets the Transition that will be used for shared elements transferred into the content Scene.
	void	setSharedElementReturnTransition(Transition transition)
	Sets the Transition that will be used for shared elements transferred back during a pop of the back stack.
	void	setTargetFragment(Fragment fragment, int requestCode)
	Optional target for this fragment.
	void	setUserVisibleHint(boolean isVisibleToUser)
	Set a hint to the system about whether this fragment's UI is currently visible to the user.
	boolean	shouldShowRequestPermissionRationale(String permission)
	Gets whether you should show UI with rationale for requesting a permission.
	void	startActivity(Intent intent)
	Call startActivity(Intent) from the fragment's containing Activity.
	void	startActivity(Intent intent, Bundle options)
	Call startActivity(Intent, Bundle) from the fragment's containing Activity.
	void	startActivityForResult(Intent intent, int requestCode)
	Call startActivityForResult(Intent, int) from the fragment's containing Activity.
	void	startActivityForResult(Intent intent, int requestCode, Bundle options)
	Call startActivityForResult(Intent, int, Bundle) from the fragment's containing Activity.
	void	startIntentSenderForResult(IntentSender intent, int requestCode, Intent fillInIntent, int flagsMask, int flagsValues, int extraFlags, Bundle options)
	Call startIntentSenderForResult(IntentSender, int, Intent, int, int, int, Bundle) from the fragment's containing Activity.
	void	startPostponedEnterTransition()
	Begin postponed transitions after postponeEnterTransition() was called.
	String	toString()
	Returns a string representation of the object.
	void	unregisterForContextMenu(View view)
	Prevents a context menu to be shown for the given view.