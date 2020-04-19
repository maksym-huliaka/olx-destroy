from modules.database.connection_factory import connect


def save(table, columns, values):
    connection = connect()
    cursor = connection.cursor()
    columns_string = ''
    values_string = ''
    for column, value in zip(columns, values):
        columns_string = columns_string + column + ", "
        values_string = values_string + "'" + value + "'" + ", "
    columns_string = columns_string[:-2]
    values_string = values_string[:-2]
    cursor.execute('INSERT INTO ' + table + ' (' + columns_string + ')' + ' VALUES ' + '(' + values_string + ');')
    connection.commit()
    cursor.close()
    connection.close()


def get(table, columns):
    connection = connect()
    cursor = connection.cursor()
    columns_string = ' '
    for column in columns:
        columns_string = columns_string + column + ", "

    columns_string = columns_string[:-2]
    cursor.execute('SELECT ' + columns_string + ' FROM ' + table + ';')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def get_by(table, columns, by, value):
    connection = connect()
    cursor = connection.cursor()
    columns_string = ' '
    for column in columns:
        columns_string = columns_string + column + ", "

    columns_string = columns_string[:-2]
    cursor.execute('SELECT ' + columns_string + ' FROM ' + table + ' WHERE ' + by + " = '" + value + "';")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def delete(table, column, value):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('delete from ' + table + ' WHERE ' + column + " = '" + value + "'")
    connection.commit()
    cursor.close()
    connection.close()


def delete_all(table):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('delete from ' + table + ";")
    connection.commit()
    cursor.close()
    connection.close()
