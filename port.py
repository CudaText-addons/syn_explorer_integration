import os
import sw as app

APP_NAME = 'SynWrite'
EXT_PROJ = 'synw-proj'
EXT_SESS = 'synw-session'

def msg_warn_func(s):
    app.msg_box(app.MSG_WARN, s)

def msg_error_func(s):
    app.msg_box(app.MSG_ERROR, s)

exe_path = os.path.join(app.app_exe_dir(), 'syn.exe')
dlg_custom = app.dlg_custom
