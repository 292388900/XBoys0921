#ContentProvider

多应用之间

直接子类：

	DocumentsProvider  
	FileProvider  
	MockContentProvider  
	SearchRecentSuggestionsProvider  
#
	onCreate() which is called to initialize the provider
	query(Uri, String[], Bundle, CancellationSignal) which returns data to the caller
	insert(Uri, ContentValues) which inserts new data into the content provider
	update(Uri, ContentValues, String, String[]) which updates existing data in the content provider
	delete(Uri, String, String[]) which deletes data from the content provider

#Public methods
	ContentProviderResult[]	applyBatch(ArrayList<ContentProviderOperation> operations)
	Override this to handle requests to perform a batch of operations, or the default implementation will iterate over the operations and call apply(ContentProvider, ContentProviderResult[], int) on each of them.

	void	attachInfo(Context context, ProviderInfo info)
	After being instantiated, this is called to tell the content provider about itself.

	int	bulkInsert(Uri uri, ContentValues[] values)
	Override this to handle requests to insert a set of new rows, or the default implementation will iterate over the values and call insert(Uri, ContentValues) on each of them.

	Bundle	call(String method, String arg, Bundle extras)
	Call a provider-defined method.

	Uri	canonicalize(Uri url)
	Implement this to support canonicalization of URIs that refer to your content provider.

	abstract int	delete(Uri uri, String selection, String[] selectionArgs)
	Implement this to handle requests to delete one or more rows.

	void	dump(FileDescriptor fd, PrintWriter writer, String[] args)
	Print the Provider's state into the given stream.
	final String	getCallingPackage()
	Return the package name of the caller that initiated the request being processed on the current thread.

	final Context	getContext()
	Retrieves the Context this provider is running in.

	final PathPermission[]	getPathPermissions()
	Return the path-based permissions required for read and/or write access to this content provider.

	final String	getReadPermission()
	Return the name of the permission required for read-only access to this content provider.

	String[]	getStreamTypes(Uri uri, String mimeTypeFilter)
	Called by a client to determine the types of data streams that this content provider supports for the given URI.

	abstract String	getType(Uri uri)
	Implement this to handle requests for the MIME type of the data at the given URI.

	final String	getWritePermission()
	Return the name of the permission required for read/write access to this content provider.

	abstract Uri	insert(Uri uri, ContentValues values)
	Implement this to handle requests to insert a new row.

	void	onConfigurationChanged(Configuration newConfig)
	Called by the system when the device configuration changes while your component is running. This method is always called on the application main thread, and must not perform lengthy operations.

	abstract boolean	onCreate()
	Implement this to initialize your content provider on startup.

	void	onLowMemory()
	This is called when the overall system is running low on memory, and actively running processes should trim their memory usage. This method is always called on the application main thread, and must not perform lengthy operations.

	void	onTrimMemory(int level)
	Called when the operating system has determined that it is a good time for a process to trim unneeded memory from its process.

	AssetFileDescriptor	openAssetFile(Uri uri, String mode, CancellationSignal signal)
	This is like openFile(Uri, String), but can be implemented by providers that need to be able to return sub-sections of files, often assets inside of their .apk.

	AssetFileDescriptor	openAssetFile(Uri uri, String mode)
	This is like openFile(Uri, String), but can be implemented by providers that need to be able to return sub-sections of files, often assets inside of their .apk.

	ParcelFileDescriptor	openFile(Uri uri, String mode, CancellationSignal signal)
	Override this to handle requests to open a file blob.

	ParcelFileDescriptor	openFile(Uri uri, String mode)
	Override this to handle requests to open a file blob.

	<T> ParcelFileDescriptor	openPipeHelper(Uri uri, String mimeType, Bundle opts, T args, PipeDataWriter<T> func)
	A helper function for implementing openTypedAssetFile(Uri, String, Bundle), for creating a data pipe and background thread allowing you to stream generated data back to the client.

	AssetFileDescriptor	openTypedAssetFile(Uri uri, String mimeTypeFilter, Bundle opts)
	Called by a client to open a read-only stream containing data of a particular MIME type.
	AssetFileDescriptor	openTypedAssetFile(Uri uri, String mimeTypeFilter, Bundle opts, CancellationSignal signal)
	Called by a client to open a read-only stream containing data of a particular MIME type.

	Cursor	query(Uri uri, String[] projection, Bundle queryArgs, CancellationSignal cancellationSignal)
	Implement this to handle query requests where the arguments are packed into a Bundle.

	Cursor	query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder, CancellationSignal cancellationSignal)
	Implement this to handle query requests from clients with support for cancellation.

	abstract Cursor	query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder)
	Implement this to handle query requests from clients.

	boolean	refresh(Uri uri, Bundle args, CancellationSignal cancellationSignal)
	Implement this to support refresh of content identified by uri.

	void	shutdown()
	Implement this to shut down the ContentProvider instance.

	Uri	uncanonicalize(Uri url)
	Remove canonicalization from canonical URIs previously returned by canonicalize(Uri).

	abstract int	update(Uri uri, ContentValues values, String selection, String[] selectionArgs)
	Implement this to handle requests to update one or more rows.