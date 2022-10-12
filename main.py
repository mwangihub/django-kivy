from kivymd.app import MDApp

from Screens.RootScreen.root_screen import RootScreen


class MeditationAppLiveApp(MDApp):
    def build(self):
        self.load_all_kv_files(self.directory)
        return RootScreen()


if __name__ == '__main__':
    MeditationAppLiveApp().run()
