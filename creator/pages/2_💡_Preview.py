from loguru import logger
from modules.comfyflow import Comfyflow

import streamlit as st
import modules.page as page
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page
from modules import get_comfy_client, get_sqlite_instance
from modules.sqlitehelper import AppStatus


logger.info("Loading preview page")
page.page_init()

with st.container():
    with page.stylable_button_container():
        header_row = row([0.85, 0.15], vertical_align="top")
        header_row.title("💡 Preview and check app")
        back_button = header_row.button("Back Workspace", help="Back to your workspace", key='preview_back_workspace')
        if back_button:
            switch_page("Workspace")

    apps = get_sqlite_instance().get_all_apps()
    app_name_map = {app.name: app for app in apps}
    app_opts = list(app_name_map.keys())
    if len(app_opts) == 0:
        st.warning("Please create a new app first.")
        st.stop()
    else:
        st.selectbox("My Apps", options=app_opts, key='preview_select_app', help="Select a app to preview.")
        
        preview_app = st.session_state['preview_select_app']
        if preview_app:
            logger.info(f"preview app: {preview_app}")
            
            app = app_name_map[preview_app]
            status = app.status
            api_data = app.api_conf
            app_data = app.app_conf
            comfyflow = Comfyflow(comfy_client=get_comfy_client(), api_data=api_data, app_data=app_data)
            comfyflow.create_ui()
            if status == AppStatus.CREATED.value:
                if f"{preview_app}_previewed" in st.session_state:
                    previewed = st.session_state[f"{preview_app}_previewed"]
                    if previewed:
                        st.success(f"Preview app {preview_app} success, back your workspace and start the app.")
                        get_sqlite_instance().update_app_preview(preview_app)
                        logger.info(f"update preview status for app: {preview_app}")
                        st.stop()
                    else:
                        st.warning(f"Preview app {preview_app} failed.")
                    

                        