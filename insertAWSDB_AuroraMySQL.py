import insertUtil as ut
import mysql.connector


#Tạo kết nối với RDS Aurora MySQL và thêm dữ liệu vào
conn = mysql.connector.connect(host='database-aurora.cluster-czlew7njenbe.us-east-1.rds.amazonaws.com, user='main', passwd='lab-password', db='COVID19', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')


