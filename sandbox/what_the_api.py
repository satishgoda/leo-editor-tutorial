@language python

@g.IdleTime
def idle_print(incoming=None):
    g.es(incoming)
    g.es("Nice....")

#g.app.idleTimeManager.add_callback(idle_print)

g.es(dir(g.app))

['UnitTestGui', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'allow_delayed_see', 'already_open_files', 'atAutoNames', 'atFileNames', 'atPathInBodyWarning', 'batchMode', 'checkForOpenFile', 'check_files_timer', 'closeLeoWindow', 'cmd', 'commandInterruptFlag', 'commandName', 'commanders', 'computeSignon', 'config', 'count', 'createCursesGui', 'createDefaultGui', 'createNullGuiWithScript', 'createQtGui', 'createWxGui', 'db', 'debug', 'debugSwitch', 'debug_app', 'debug_widgets', 'define_delegate_language_dict', 'define_extension_dict', 'define_global_constants', 'define_language_delims_dict', 'define_language_extension_dict', 'delegate_language_dict', 'destroyAllOpenWithFiles', 'destroyWindow', 'diff', 'disableSave', 'disable_redraw', 'drag_source', 'dragging', 'enablePlugins', 'extension_dict', 'extensionsDir', 'externalFilesController', 'extra_extension_dict', 'finishQuit', 'forceShutdown', 'forgetOpenFile', 'globalConfigDir', 'globalKillBuffer', 'globalOpenDir', 'globalRegisters', 'gui', 'guiArgName', 'homeDir', 'homeLeoDir', 'hookError', 'hookFunction', 'idleTimeDelay', 'idle_imported', 'idle_timer', 'idle_timer_enabled', 'idle_timers', 'inBridge', 'inScript', 'initComplete', 'init_at_auto_names', 'init_at_file_names', 'initing', 'ipk', 'ipython_inited', 'isExternalUnitTest', 'killed', 'language_delims_dict', 'language_extension_dict', 'leoDir', 'leoID', 'loadDir', 'loadManager', 'lockLog', 'log', 'logInited', 'logIsLocked', 'logWaiting', 'lossage', 'machineDir', 'menuWarningsGiven', 'newCommander', 'nodeIndices', 'nullGui', 'nullLog', 'numberOfUntitledWindows', 'onQuit', 'openWithTable', 'openingSettingsFile', 'paste_c', 'permanentScriptDict', 'pluginsController', 'positions', 'preReadFlag', 'printWaiting', 'prolog_namespace_string', 'prolog_postfix_string', 'prolog_prefix_string', 'qt_use_tabs', 'quitting', 'realMenuNameDict', 'recentFilesManager', 'rememberOpenFile', 'restore_session', 'reverting', 'runAlreadyOpenDialog', 'runningAllUnitTests', 'save_session', 'scanErrors', 'scriptDict', 'scriptResult', 'searchDict', 'selectLeoWindow', 'sessionManager', 'setGlobalDb', 'setLeoID', 'setLog', 'signon', 'signon1', 'signon2', 'signon_printed', 'silentMode', 'spellDict', 'start_fullscreen', 'start_maximized', 'start_minimized', 'statsDict', 'stickynotes', 'structure_errors', 'suppressImportChecks', 'syntax_error_files', 'testDir', 'trace_open_with', 'trace_plugins', 'trace_shutdown', 'translateToUpperCase', 'unicodeErrorGiven', 'unitTestDict', 'unitTestMenusDict', 'unitTesting', 'unlockLog', 'useIpython', 'use_psyco', 'use_splash_screen', 'validate_outline', 'windowList', 'writeWaitingLog', 'write_Leo_file_string']

g.es(g.app.leoDir)

g.es(g.app.idle_timers)
g.es(g.app.idle_timer_enabled)

@g.IdleTime
def idle_print(incoming=None):
    g.es(incoming)
    g.es("Nice....")

g.app.idle_timers.append(idle_print)
