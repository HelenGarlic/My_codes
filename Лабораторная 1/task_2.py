# TODO Найдите количество книг, которое можно разместить на дискете
colvo_bytes_for_one_book = 100 * 50 * 25
weight_of_one_book = colvo_bytes_for_one_book * 4
v_of_disketa = 1.44 * 1024 * 1024


print("Количество книг, помещающихся на дискету:", int(v_of_disketa // weight_of_one_book))
