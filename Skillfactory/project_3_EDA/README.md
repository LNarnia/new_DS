# Проект Project_3_Booking. 

## Оглавление

[1. Описание проекта](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Какой-кейс-решаем?)

[3. Краткая информация о данных](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Этапы-работы-над-проектом)

[5. Результат](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Результат)

### Описание проекта
Построение модели, которая предсказывает рейтинг отеля. Поучаствовать в соревновании на Kaggle.

:arrow_up: [к оглавлению](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Оглавление)

### Какой кейс решаем?
Выявить нечестные отели, которые накручивают себе рейтинг. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

:arrow_up: [к оглавлению](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Оглавление)

### Краткая информация о данных

Файлы для соревнования:

- hotels_train.csv - набор данных для обучения [здесь](https://www.kaggle.com/competitions/sf-booking/data?select=hotels_train.csv)
- hotels_test.csv - набор данных для оценки качества [здесь](https://www.kaggle.com/competitions/sf-booking/data?select=hotels_test.csv)
- submission.csv - файл сабмишна в нужном формате [здесь](https://www.kaggle.com/competitions/sf-booking/data?select=submission.csv)

Признаки:
- hotel_address — адрес отеля;
- review_date — дата, когда рецензент разместил соответствующий отзыв;
- average_score — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
- hotel_name — название отеля;
- reviewer_nationality — страна рецензента;
- negative_review — отрицательный отзыв, который рецензент дал отелю;
- review_total_negative_word_counts — общее количество слов в отрицательном отзыв;
- positive_review — положительный отзыв, который рецензент дал отелю;
- review_total_positive_word_counts — общее количество слов в положительном отзыве.
- reviewer_score — оценка, которую рецензент поставил отелю на основе своего опыта;
- total_number_of_reviews_reviewer_has_given — количество отзывов, которые рецензенты дали в прошлом;
- total_number_of_reviews — общее количество действительных отзывов об отеле;
- tags — теги, которые рецензент дал отелю;
- days_since_review — количество дней между датой проверки и датой очистки;
- additional_number_of_scoring — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
- lat — географическая широта отеля;
- lng — географическая долгота отеля.

:arrow_up: [к оглавлению](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Оглавление)

### Этапы работы над проектом
- знакомство с данными;
- предварительный анализ данных;
- создание признаков;
- кодирование признаков;
- отбор призанков;
- создание и обучение модели;
- оценка качества модели.

:arrow_up: [к оглавлению](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Оглавление)

### Результат

Произведен предварительный анализ данных, их очистка, создание, преобразование и отбор признаков, создана и обучена модель, произведена оченка ее качества. Созданное решение участвует в соревановании на Kaggle. Наилучший достигнутый результат ...


Итоговый ноутбук на GitHub [здесь](https://github.com/LNarnia/new_DS/blob/main/Skillfactory/project_3_EDA/project-3-booking-ready.ipynb)

Итоговый ноутбук на Kaggle [здесь](https://www.kaggle.com/code/lnarnia/project-3-booking-ready)


:arrow_up: [к оглавлению](https://github.com/LNarnia/new_DS/tree/main/Skillfactory/project_3_EDA#Оглавление)
