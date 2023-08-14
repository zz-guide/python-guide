class VariableCache:
    """
    此类保存全局变量
    """
    database = None

    # 窗体实例
    main_widget = None
    login_widget = None
    register_widget = None
    # pwd_book 密码本
    pwd_book_table_widget = None
    pwd_book_create_widget = None
    pwd_book_update_widget = None

    # 信号
    signal_bus = None
