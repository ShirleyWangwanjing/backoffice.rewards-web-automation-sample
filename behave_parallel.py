from multiprocessing import Pool, Process, Manager
from subprocess import call, Popen, PIPE
import argparse
import os
from utils import logger


class BehaveParallel(object):

    def __init__(self):
        self.basic_cmd = 'python -m behave --logging-level INFO --no-capture -f allure_behave.formatter:AllureFormatter -o artifacts/allure --junit --junit-directory artifacts/junit '
        self.mobile_key_map = Manager().dict()

    def _get_mobile_key(self, pid):
        for k, v in self.mobile_key_map.items():
            if v == pid:
                return k
        return ''

    def _set_mobile_key(self, pid):
        for k, v in self.mobile_key_map.items():
            if v == "":
                v = pid
                self.mobile_key_map[k] = v
                return k
        return ''

    def _generate_mobile_key(self, pid):
        key = self._get_mobile_key(pid)
        if key == '':
            key = self._set_mobile_key(pid)
        return key

    @staticmethod
    def _parse_arguments():
        parser = argparse.ArgumentParser('Running in parallel mode.')
        parser.add_argument('--processes', '-p', type=int, help='Maximum number of processes. Default = 4', default=4)
        parser.add_argument('--tag', '-t', help='Please specify behave tags to run', default='')
        parser.add_argument('--env', '-o', help='Please specify testing environment to run', default='TEST')
        parser.add_argument('--mobile', '-m', help='Please specify if is mobile test', default=False)
        return parser.parse_args()

    def _run_mobile_feature(self, feature):
        pid = str(Process.pid)
        key = self._generate_mobile_key(pid)
        logger.info("pid=" + pid + "...key=" + key)
        # TBC
        #return feature, status  ...............need return

    def _run_common_feature(self, feature):
        tag = self._parse_arguments().tag
        env = self._parse_arguments().env
        if tag != '' and tag != 'Null':
            cmd = self.basic_cmd + ' -i {feature_file} -t ~@sequential -t {tag}'.format(feature_file=feature,
                                                                                        tag=tag)
        else:
            cmd = self.basic_cmd + ' -i {feature_file} -t ~@sequential'.format(feature_file=feature)
        if env != '' and env != 'Null':
            cmd = cmd + " -k -D browser=chrome -D env=" + env

        logger.info("start execute: " + cmd)

        r = call(cmd, shell=True)
        status = 'Passed' if r == 0 else 'Failed'
        logger.info("Execute completed: {cmd}, status:{status}".format(cmd=cmd, status=status))
        return feature, status

    def _run_parallel_feature(self, feature):
        mobile_test = BehaveParallel._parse_arguments().mobile
        if mobile_test:
            return self._run_mobile_feature(feature)
        else:
            tag = self._parse_arguments().tag
            env = self._parse_arguments().env
            if tag != '' and tag != 'Null':
                cmd = self.basic_cmd + ' -i {feature_file} -t ~@sequential -t {tag}'.format(feature_file=feature,
                                                                                            tag=tag)
            else:
                cmd = self.basic_cmd + ' -i {feature_file} -t ~@sequential'.format(feature_file=feature)
            if env != '' and env != 'Null':
                cmd = cmd + " -k -D browser=chrome -D env=" + env

            logger.info("start execute: " + cmd)

            r = call(cmd, shell=True)
            status = 'Passed' if r == 0 else 'Failed'
            logger.info("Execute completed: {cmd}, status:{status}".format(cmd=cmd, status=status))
            return feature, status

    def _run_sequential_feature(self):
        logger.info('start run test in sequential.')
        tag = BehaveParallel._parse_arguments().tag
        env = BehaveParallel._parse_arguments().env
        cmd = ''
        if tag != '' and tag != 'Null':
            cmd = self.basic_cmd + ' -t sequential -t {tag}'.format(tag=tag)
        else:
            cmd = self.basic_cmd + ' -t sequential'
        if env != '' and env != 'Null':
            cmd = cmd + " -k -D browser=chrome -D env=" + env
        logger.info(cmd)
        r = call(cmd, shell=True)
        status = 'Passed' if r == 0 else 'Failed'
        return status

    def _get_feature_files(self):
        file_list = list()
        current_file_path = os.path.dirname(os.path.abspath(__file__))
        for root, dirs, files in os.walk(current_file_path):
            for file in files:
                if '.feature' in file:
                    file_list.append({os.path.join(root, file): file})
        return file_list

    def _if_tag_in_feature(self, feature_file):
        tag = BehaveParallel._parse_arguments().tag
        if tag == '' or tag == 'null':
            return True
        with open(feature_file, 'r') as foo:
            for line in foo.readlines():
                if "@" not in tag:
                    tag = "@"+tag
                if tag in line:
                    return True
        return False

    def _get_executable_feature_files(self):
        all_feature_files = self._get_feature_files()
        executable_feature_files = list()
        for file_dict in all_feature_files:
            file_path = ''
            file_name = ''
            for k, v in file_dict.items():
                file_path = k
                file_name = v
            if self._if_tag_in_feature(file_path):
                executable_feature_files.append(file_name)
        return executable_feature_files

    def behave_parallel(self):
        self.mobile_key_map["gw0"] = ""
        self.mobile_key_map["gw1"] = ""

        args = self._parse_arguments()
        pool = Pool(args.processes)

        features = self._get_executable_feature_files()

        logger.info("get all features: " + str(features))
        parallel_test_results = pool.map(self._run_parallel_feature, features)
        logger.info("*******************************************************************************************")
        logger.info("Parallel test result: " + str(parallel_test_results))
        logger.info("*******************************************************************************************")
        sequential_test_result = self._run_sequential_feature()
        logger.info("*******************************************************************************************")
        logger.info("Sequential test result: " + sequential_test_result)
        logger.info("*******************************************************************************************")
        for feature_test_result in parallel_test_results:
            if "Failed" in feature_test_result:
                return "Failed"
        if sequential_test_result == "Failed":
            return "Failed"
        return "Succeed"


if __name__ == '__main__':
    behave_parallel = BehaveParallel()
    test_result = behave_parallel.behave_parallel()
    if test_result == "Failed":
        logger.info("*******************************************************************************************")
        logger.info("Test failed. Please check detail log.")
        logger.info("*******************************************************************************************")
        raise Exception("Test Fail failed. Please check detail log")
    else:
        logger.info("*******************************************************************************************")
        logger.info("All test passed")
        logger.info("*******************************************************************************************")
