import psycopg2

def search_for_email(host, port, database, location, user, password, email_to_find, colname):

	str_sql = "SELECT * from {} where {} = '{}';".format(location, colname, email_to_find)

	try:
		result = ''
		connector = psycopg2.connect(database=database, user=user, password=password, host=host, port=port, sslmode='require')
		cur = connector.cursor()
		cur.execute(str_sql)
		#connector.commit()
		rows = cur.fetchall()
		for row in rows:
			result += str(row) + '</br>'
		return (result, str_sql)
	except Exception as err:
		print(err)
		return (str(err), str_sql)