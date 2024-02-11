# TODO Найдите количество книг, которое можно разместить на дискете
colvo_pages_in_one_book = 100
colvo_strok_on_page = 50
colvo_symbols_in_stroka = 25
weight_of_one_symbol = 4

colvo_bytes_for_one_book = colvo_pages_in_one_book * colvo_strok_on_page * colvo_symbols_in_stroka
weight_of_one_book = colvo_bytes_for_one_book * weight_of_one_symbol
v_of_disketa = 1.44 * 1024 * 1024


print("Количество книг, помещающихся на дискету:", int(v_of_disketa // weight_of_one_book))
