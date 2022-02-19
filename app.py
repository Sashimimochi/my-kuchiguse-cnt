from modules.multiapp import MultiApp

from pages.text_app import main as t_main
from pages.stt_app import main as s_main

if __name__ == '__main__':
    mpa = MultiApp()
    mpa.add_app("テキストからカウント", t_main)
    mpa.add_app("音声からカウント", s_main)
    mpa.run()
