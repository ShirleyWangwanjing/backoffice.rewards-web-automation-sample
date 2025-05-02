
from utils.sql_database_manager import SqlDatabaseManager
import requests
import json
from utils import logger

class ClearCampaign(object):

    def clear_data_via_sql_file(self, path, database_manager):
        sqls = self.get_sqls_from_file(path)
        for sql in sqls:
            database_manager.execute_update_sql(sql)

        database_manager.commit_database()

    def get_sqls_from_file(self, path):
        sqls = []
        with open(path, encoding='utf-8', mode='r') as f:
            sql_list = f.read().split(";")
            for sql in sql_list:
                sql = sql.strip()
                if not sql.startswith('--'):
                    sqls.append(sql)

        return sqls

    # def clear_Refresh_redis_cache(self):
    #     test_url = "https://rewards-campaigns.internal.iherbtest.io/api/Campaign/RefreshCache"
    #     logger.info("test RefreshCache api:" + test_url)
    #     json_headers = {'content-type': "application/json"}
    #     reponse = requests.get(url=test_url, headers=json_headers,)
    #     print(reponse.status_code)



# if __name__ == '__main__':
#     test = ClearCampaign()
#     test.clear_Refresh_redis_cache()
