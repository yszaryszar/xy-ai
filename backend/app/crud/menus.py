from app.db.session import get_db_connection


def get_menu():
    connection = get_db_connection()  # 获取数据库连接
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, parent_id, name, url, icon, `order` FROM menus"
            cursor.execute(sql)  # 执行 SQL 查询
            result = cursor.fetchall()  # 获取所有查询结果
            # 构建菜单字典
            menu_dict = {}
            for row in result:
                menu_dict[row[0]] = {
                    "id": row[0],
                    "parent_id": row[1],
                    "name": row[2],
                    "url": row[3],
                    "icon": row[4],
                    "order": row[5],
                    "children": [],  # 初始化子菜单列表
                }

            # 构建嵌套菜单结构
            menu_tree = []
            for menu in menu_dict.values():
                if menu["parent_id"] is None:
                    menu_tree.append(menu)  # 顶级菜单
                else:
                    parent = menu_dict.get(menu["parent_id"])
                    if parent:
                        parent["children"].append(menu)  # 添加到父菜单的子菜单列表中

            return menu_tree  # 返回嵌套菜单结构
    finally:
        connection.close()  # 关闭数据库连接
