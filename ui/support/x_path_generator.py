__author__ = 'Ragu.Sekaran'


class XPathGenerator(object):
    # xPath methods generate xPath based on lable
    def single_input(self, label):
        """
        Param: Label name
        Return Xpath for the single line input field
        """
        return "//td[contains(@class,'labelCol')]//label[text()='" + label + "']/following::input[1]"

    def multi_input(self, label):
        """s
        Param: Label name
        Return Xpath for the multiple line input field
        """
        return "//td[contains(@class,'labelCol')]//label[text()='" + label + "']/following::textarea[1]"

    def single_select(self, label):
        """
        Param: Label name
        Return Xpath for the select input field
        """
        return "//td[contains(@class,'labelCol')]//label[text()='" + label + "']/following::select[1]"

    def select_option(self, label, value):
        """
        Param: Label name, option value
        Return Xpath for the select option field
        """
        return "//td[contains(@class,'labelCol')]//label[text()='" + label + "']/following::select[1]/option[text()='" + value + "']"

    def look_up(self, label):
        """
        Param: Label name
        Return Xpath for the look up input field
        """
        return "//td[contains(@class,'labelCol')]//label[text()='" + label + "']/following::input[7]"

    def single_field(self, label):
        """
        Param: Label name
        Return Xpath for the single line input field
        """
        return "//td[text()='" + label + "']/following::td[1]"

    def single_field_with_help_icon(self, label):
        """
        Param: Label name
        Return Xpath for the single line input field
        """
        return "//td/span[text()='" + label + "']/following::td[1]"

    def continue_on_record_type_page(self):
        return "//td[@id='bottomButtonRow']/input[@name='save']"

    def cancel_on_record_type_page(self):
        return "//td[@id='bottomButtonRow']/input[@name='cancel']"

    def customized_button(self, name):
        return "//input[@value='" + name + "']"

    def button_on_section_standard(self, sectionName, buttonName, position=None):
        '''
        sectionName should be as "Campaign Edit" or "Campaign Detail", based on current page
        '''
        p = "top"
        if position is not None:
            p = position
        return "//div//h2[text()='" + sectionName + "']/following::td[@id='" + p + "ButtonRow']/input[@name='" + buttonName + "']"

    def button_on_section_standard_by_name(self, sectionName, buttonName, position="top"):
        return self.button_section_standard(sectionName, buttonName, position)

    def save_on_section_standard_top(self, sectionName):
        return self.button_on_section_standard(sectionName, "save")

    def save_new_on_section_standard_top(self, sectionName):
        return self.button_on_section_standard(sectionName, "save_new")

    def cancel_on_section_standard_top(self, sectionName):
        return self.button_on_section_standard(sectionName, "cancel")

    def edit_on_section_standard_top(self, sectionName):
        return self.button_on_section_standard(sectionName, "edit")

    def share_on_section_standard_top(self, sectionName):
        return self.button_on_section_standard(sectionName, "share", "top")

    def activate_on_section_standard_top(self, sectionName):
        return self.button_on_section_standard(sectionName, "activate", "top")

    def deactivate_on_section_standard_top(self, sectionName):
        return self.button_on_section_standard(sectionName, "deactivate", "top")

    def save_on_section_standard_bottom(self, sectionName):
        return self.button_on_section_standard(sectionName, "save", "bottom")

    def save_new_on_section_standard_bottom(self, sectionName):
        return self.button_on_section_standard(sectionName, "save_new", "bottom")

    def cancel_on_section_standard_bottom(self, sectionName):
        return self.button_on_section_standard(sectionName, "cancel", "bottom")

    def edit_on_section_standard_bottom(self, sectionName):
        return self.button_on_section_standard(sectionName, "edit", "bottom")

    def share_on_section_standard_bottom(self, sectionName):
        return self.button_on_section_standard(sectionName, "share", "bottom")

    def activate_on_section_standard_bottom(self, sectionName):
        return self.button_on_section_standard(sectionName, "activate", "bottom")

    def deactivate_on_section_standard_bottom(self, sectionName):
        return self.button_on_section_standard(sectionName, "deactivate", "bottom")

    def iframe(self, iframeClass):
        return "//iframe[contains(@class,'" + iframeClass + "')]"

    def iframe_by_title(self, iframeTitle):
        return "//iframe[@title='" + iframeTitle + "']"

    def button_by_text(self, text):
        return "//button[text()='" + text + "']"

    def group_calendar_block(self):
        return "//div[contains(@class,'scheduler_default_event')][0]"

    # Exception
    def message_on_top(self):
        # regard that there is only one error div in page
        return "//div[@class='pbError']"

    def message_follows_fields(self):
        return "//div[@class='errorMsg']"

    def message_follows_field(self, label):
        return "//td[contains(@class,'labelCol')]//label[text()='" + label + "']/following::div[@class='errorMsg'][1]"

    def insufficient_privileges(self):
        return "//span[text()='Insufficient Privileges']"
