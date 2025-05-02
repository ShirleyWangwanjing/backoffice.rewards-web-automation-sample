class FileUtils(object):

    @staticmethod
    def amend_file(file_path_name, content_list):
        with open(file_path_name, "a") as file:
            for row in content_list:
                file.write(str(row)+" "+"\n")