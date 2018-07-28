import copy


class Widgets:
    def __init__(self):
        self.app = {}
        self.title = ''
        self.branding = ''
        self.view_name = {}
        self.navigation_drawer = []
        self.list_view = []
        self.app_bar = []
        self.app_bar_buttons = []
        self.menu = []
        self.action_bar = []

    def copy(self):
        return copy.deepcopy(self)