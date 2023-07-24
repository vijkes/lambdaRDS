
# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys

REGION = 'us-east-1'

rds_host  = "database-3.cadnqqtfeepu.us-east-1.rds.amazonaws.com"
name = "admin"
password = "India1234qwer"
db_name = "vk"

def save_events(event):
    """
    This function fetches content from mysql RDS instance
    """
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into Orders (OId, Name, OrderNo, TrackNo) values( %s, '%s', '%s', '%s')""" % (event['OId'], event['Name'], event['OrderNo'], event['TrackNo']))
        cur.execute("""select * from Orders""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print "Data from RDS..."
        print result

def main(event, context):
    save_events(event)
        


# event = {
#   "id": 777,
#   "name": "appychip"
# }
# context = ""
# main(event, context)

